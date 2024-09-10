import pexpect
import subprocess

def run_btcli_command(command, description=""):
    """
    Runs a btcli command and prints the result.
    """
    print(f"Running: {description}")
    print(f"Command: {command}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"Output:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}\n{e.stderr}")
    print("-" * 50)

def run_interactive_btcli_command(command, description=""):
    """
    Runs an interactive btcli command and handles prompts without timing out.
    """
    print(f"Running interactive command: {description}")
    print(f"Command: {command}")
    child = pexpect.spawn(command, encoding='utf-8', timeout=None)  # Disable timeout

    try:
        child.expect("Enter password to unlock key:")
        child.sendline('Strong!')  # Replace with your actual password

        child.expect(pexpect.EOF)  # Wait for command to complete
        print(child.before)  # Output from the command
    except pexpect.TIMEOUT:
        print("Command timed out.")
    except pexpect.EOF:
        print("Command ended.")
    print("-" * 50)

def test_btcli_wallet_commands():
    """
    A series of tests for btcli wallet commands.
    """
    wallet_name = "test-wallet-Alice"
    subtensor_chain = "wss://dev.chain.opentensor.ai:443"  # Substitute with the actual chain endpoint
    wallet_path = "~/.bittensor/wallets/"  # Substitute with the actual path to wallets
    hotkey = "default"  # Substitute with the actual hotkey if needed
    network = "devnet"  # Substitute with the actual network if needed
    use_password = "--no-use-password"  # or "--no-use-password" depending on the requirement
    
    # Test creating a cold hotkey
    run_btcli_command(
        f"btcli wallet new-coldkey --wallet-name {wallet_name} --wallet-path {wallet_path} --hotkey {hotkey} {use_password}  --n-words 12",
        "Create new coldkey"
    )
    
    # Test creating a new hotkey
    run_btcli_command(
        f"btcli wallet new-hotkey --wallet-name {wallet_name} --wallet-path {wallet_path} --hotkey {hotkey} {use_password}  --n-words 12  --verbose",
        "Create new hotkey"
    )

    # Test wallet list
    run_btcli_command(
        f"btcli wallet list --wallet-path {wallet_path}",
        "Check wallet list"
    )

    # Test wallet balance
    run_btcli_command(
        f"btcli wallet balance --wallet-name {wallet_name} --subtensor.chain_endpoint {subtensor_chain}",
        "Check wallet balance"
    )

    # Test wallet history
    run_btcli_command(
        f"btcli wallet history --wallet-name {wallet_name} --wallet-path {wallet_path} --hotkey {hotkey} --verbose",
        "Check wallet transaction history"
    )

    # Test wallet inspection
    run_btcli_command(
        f"btcli wallet inspect --wallet-name {wallet_name} --subtensor.chain_endpoint {subtensor_chain}",
        "Inspect wallet"
    )

    # Test wallet overview
    run_btcli_command(
        f"btcli wallet overview --wallet-name {wallet_name} --subtensor.chain_endpoint {subtensor_chain}",
        "Get wallet overview"
    )

    # Test wallet check-swap
    run_btcli_command(
        f"btcli wallet check-swap --wallet-name {wallet_name} --subtensor.chain_endpoint {subtensor_chain}",
        "Get wallet check-swap"
    )
    
    # Test wallet faucet with additional parameters
    run_interactive_btcli_command(
        f"btcli wallet faucet --wallet-name {wallet_name} --wallet-path {wallet_path} --hotkey {hotkey} --subtensor.chain_endpoint {subtensor_chain} ",
        "Run wallet faucet"
    )

    # Remove the created walled with hotkey
    run_btcli_command(
        f"rm -rf ~/.bittensor/wallets/{wallet_name}",
        "Remove coldkey"
    )


if __name__ == "__main__":
    test_btcli_wallet_commands()
