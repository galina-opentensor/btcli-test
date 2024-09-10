import re
import subprocess
import pexpect
from config import NETWORK, CHAIN_ENDPOINT, WALLET_NAME, WALLET_PATH, HOTKEY, USE_PASSWORD, PASSWORD
from btcli_runner import run_btcli_command, run_interactive_btcli_command


# Function to extract mnemonic from command output
def extract_mnemonic(output, key_type):
    """
    Extracts the mnemonic from the btcli command output based on key type (coldkey or hotkey).
    """
    mnemonic_pattern = re.compile(rf"The mnemonic to the new {key_type} is:\n\n(.+)\n")
    match = mnemonic_pattern.search(output)
    if match:
        mnemonic = match.group(1)
        print(f"Mnemonic extracted: {mnemonic}")
        return mnemonic
    else:
        print(f"Mnemonic not found in the output for {key_type}.")
        return None

# Reusable btcli wallet command functions
def create_coldkey():
    return run_btcli_command(
        f"btcli wallet new-coldkey --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} {USE_PASSWORD} --n-words 12",
        "Create new coldkey"
    )

def create_hotkey():
    return run_btcli_command(
        f"btcli wallet new-hotkey --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} {USE_PASSWORD} --n-words 12 --verbose",
        "Create new hotkey"
    )

def check_wallet_list():
    return run_btcli_command(
        f"btcli wallet list --wallet-path {WALLET_PATH}",
        "Check wallet list"
    )

def check_wallet_balance():
    return run_btcli_command(
        f"btcli wallet balance --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Check wallet balance"
    )

def check_wallet_history():
    return run_btcli_command(
        f"btcli wallet history --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}",
        "Check wallet transaction history"
    )

def inspect_wallet():
    return run_btcli_command(
        f"btcli wallet inspect --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Inspect wallet"
    )

def wallet_overview():
    return run_btcli_command(
        f"btcli wallet overview --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Get wallet overview"
    )

def check_wallet_swap():
    return run_btcli_command(
        f"btcli wallet check-swap --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Get wallet check-swap"
    )

def faucet_wallet():
    return run_interactive_btcli_command(
        f"btcli wallet faucet --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        PASSWORD,
        "Run wallet faucet"
    )


def regen_coldkey(mnemonic, PASSWORD):
    command = f'btcli wallet regen-coldkey --mnemonic "{mnemonic}" --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}'
    print(f"Running command: {command}")
    child = pexpect.spawn(command)  # Disable timeout

    try:
        # Provide password for key encryption
        child.expect("Specify password for key encryption:")
        child.sendline(PASSWORD)

        # Retype the password
        child.expect("Retype your password:")
        child.sendline(PASSWORD)

        child.sendline('y')
        child.sendline('y')
        child.interact()
        print(child.before)  # Output from the command

    except pexpect.TIMEOUT:
        print("Command timed out.")
    except pexpect.EOF:
        print("Command ended unexpectedly.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    print("-" * 50)

def remove_wallet():
    return run_btcli_command(
        f"rm -rf ~/.bittensor/wallets/{WALLET_NAME}",
        "Remove wallet"
    )

def test_btcli_wallet_commands():
    coldkey_output, _ = create_coldkey()
    coldkey_mnemonic = extract_mnemonic(coldkey_output, "coldkey")

    hotkey_output, _ = create_hotkey()
    hotkey_mnemonic = extract_mnemonic(hotkey_output, "hotkey")

    #check_wallet_list()
    #faucet_wallet()
    #check_wallet_balance()
    #check_wallet_history()
    #inspect_wallet()
    #wallet_overview()
    #check_wallet_swap()
    

    if coldkey_mnemonic:
        regen_coldkey(coldkey_mnemonic, PASSWORD)
    
    if hotkey_mnemonic:
        regen_hotkey(hotkey_mnemonic)

    remove_wallet()

if __name__ == "__main__":
    test_btcli_wallet_commands()
