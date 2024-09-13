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
    def __init__(self, output: io.FileIO):
        self.output = output

    def run(self, cmd: str, ignore_failure=True, timeout=3600) -> str:
        self.print_colored(BLUE, "Executing: ", cmd)
        try:
            result = subprocess.check_output(
                cmd, shell=True, timeout=timeout
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
        
        child = pexpect.spawn(cmd, timeout=timeout, encoding='utf-8')
        
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


    def print_colored(self, color: str, *inputs):
        inputs_str = [" ".join(item) if isinstance(item, list) else str(item) for item in inputs]
        self.output.write(color + " ".join(inputs_str) + REGULAR)
