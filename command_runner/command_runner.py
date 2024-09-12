import os
import io
import subprocess
import pexpect
import pytest

BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
ORANGE = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RED_BOLD_UNDERLINED = "\033[91m"
REGULAR = "\033[0m\n"


class CommandRunner(object):
    def __init__(self, wd: os.PathLike, output: io.FileIO):
        self.working_directory = wd
        self.output = output

    def run(self, cmd: str, ignore_failure=True, timeout=3600) -> str:
        self.print_colored(BLUE, "Executing: ", cmd)
        try:
            result = subprocess.check_output(
                cmd, cwd=self.working_directory, shell=True, timeout=timeout
            )
        except subprocess.CalledProcessError as e:
            self.print_colored(RED, "Failed to execute: ", cmd)
            self.print_colored(REGULAR, "Output:", e.output.decode("utf-8").strip())
            if not ignore_failure:
                pytest.fail(f"Couldn't execute '{cmd}'")
            return ""

        output = result.decode("utf-8").strip()
        self.print_colored(GREEN, "Successfully executed: ", cmd)
        self.print_colored(REGULAR, "Output: ", output)
        return output

    def run_interactive(self, cmd: str, prompts_responses: dict, timeout=3600) -> str:
        self.print_colored(BLUE, "Executing interactively: ", cmd)
        
        child = pexpect.spawn(cmd, cwd=self.working_directory, timeout=timeout, encoding='utf-8')
        
        try:
            for prompt, response in prompts_responses.items():
                index = child.expect([prompt, pexpect.TIMEOUT, pexpect.EOF], timeout=timeout)
                if index == 0:  # Prompt matched
                    self.print_colored(CYAN, "Prompt: ", prompt)
                    child.sendline(response)
                elif index == 1:  # Timeout
                    self.print_colored(RED, "Timeout while waiting for: ", prompt)
                    pytest.fail(f"Timeout while waiting for prompt: '{prompt}'")
                    return ""
                elif index == 2:  # End of File
                    self.print_colored(RED, "EOF while waiting for: ", prompt)
                    pytest.fail(f"EOF while waiting for prompt: '{prompt}'")
                    return ""
            
            child.expect(pexpect.EOF, timeout=timeout)
            output = child.before.strip()
            
            self.print_colored(GREEN, "Successfully executed interactively: ", cmd)
            self.print_colored(REGULAR, "Output: ", output)
            return output
        
        except Exception as e:
            self.print_colored(RED, "Error during interactive execution: ", str(e))
            pytest.fail(f"Error during interactive execution: {str(e)}")
            return ""

    def create_subnet(self):
        cmd = f"btcli subnets create --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Specify password for key encryption:": PASSWORD,  # Enter the password for encryption
            r"Retype your password:": PASSWORD,                # Retype the password            
            r"File .*subnet already exists. Overwrite\? \(y/N\)": "y",  # Respond 'yes' to overwrite subnet
        }

        try:
            output = self.run_interactive(cmd, prompts_responses)
            if not output:
                pytest.fail("Command failed to produce output or ended unexpectedly.")
            return output
        except Exception as e:
            pytest.fail(f"Failed to create subnet: {e}")


    def print_colored(self, color: str, *inputs):
        inputs_str = [" ".join(item) if isinstance(item, list) else str(item) for item in inputs]
        self.output.write(color + " ".join(inputs_str) + REGULAR)
