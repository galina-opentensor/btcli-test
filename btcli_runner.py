# btcli_runner.py

import subprocess
import pexpect
from colorama import Fore, Style, init
from config import PASSWORD

# Initialize colorama to support colored text in all platforms
init(autoreset=True)

def run_btcli_command(command, description=""):
    """
    Runs a btcli command and prints the result, including both stdout and stderr.
    Captures outputs even if the command fails.
    """
    print(f"{Fore.CYAN}Running: {description}")
    print(f"{Fore.YELLOW}Command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"{Fore.GREEN}Output (stdout):\n{result.stdout}")
        print(f"{Fore.RED}Error (stderr):\n{result.stderr}")
        return result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Command failed with error:\n{e}\n{e.stderr}")
        return None, e.stderr
    print(f"{Style.RESET_ALL}{'-' * 50}")

def run_interactive_btcli_command(command, input_value, description=""):
    """
    Runs an interactive btcli command and passes the input_value when prompted.
    """
    print(f"{Fore.CYAN}Running interactive command: {description}")
    print(f"{Fore.YELLOW}Command: {command}")
    child = pexpect.spawn(command, encoding='utf-8', timeout=None)  # Disable timeout

    try:
        child.expect("Enter password to unlock key:")
        child.sendline(PASSWORD)  # Replace with your actual password

        child.expect("Enter mnemonic, seed, or json file location:")
        child.sendline(input_value)  # Send the mnemonic

        child.expect(pexpect.EOF)  # Wait for command to complete
        print(f"{Fore.GREEN}{child.before}")  # Output from the command
    except pexpect.TIMEOUT:
        print(f"{Fore.RED}Command timed out.")
    except pexpect.EOF:
        print(f"{Fore.RED}Command ended.")
    print(f"{Style.RESET_ALL}{'-' * 50}")
