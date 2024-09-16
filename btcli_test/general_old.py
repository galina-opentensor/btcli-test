import pexpect
import re
from btcli_test.config import (
    NETWORK, 
    CHAIN_ENDPOINT, 
    WALLET_NAME,
    WALLET_PATH, 
    HOTKEY, 
    USE_PASSWORD, 
    PASSWORD, 
    NETUID, 
    VALUE, 
    DELEGATE_SS58KEY, 
    AMOUNT, 
    TAKE
)
from command_runner import CommandRunner

class BtcliTest:
    def __init__(self, cr: CommandRunner):
        self.cr = cr

    ## Wallet commands
    # Create coldkey
    def create_coldkey(self):
        output = self.cr.run(
            f"btcli wallet new-coldkey --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} {USE_PASSWORD} --n-words 12",
            "Create new coldkey"
        )
        return self.extract_mnemonic(output, "coldkey")

    # Create hotkey
    def create_hotkey(self):
        self.cr.run(
            f"btcli wallet new-hotkey --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} {USE_PASSWORD} --n-words 12 --verbose",
            "Create new hotkey"
        )

    # Check wallet list
    def check_wallet_list(self):
        self.cr.run(
            f"btcli wallet list --wallet-path {WALLET_PATH}",
            "Check wallet list"
        )

    # Check wallet balance
    def check_wallet_balance(self):
        self.cr.run(
            f"btcli wallet balance --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "Check wallet balance"
        )

    # Check wallet transaction history
    def check_wallet_history(self):
        self.cr.run(
            f"btcli wallet history --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}",
            "Check wallet transaction history"
        )

    # Inspect wallet
    def inspect_wallet(self):
        self.cr.run(
            f"btcli wallet inspect --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "Inspect wallet"
        )

    # Get wallet overview
    def wallet_overview(self):
        self.cr.run(
            f"btcli wallet overview --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "Get wallet overview"
        )

    # Check wallet swap status
    def check_wallet_swap(self):
        self.cr.run(
            f"btcli wallet check-swap --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "Check wallet swap status"
        )

    # Faucet wallet
    def faucet_wallet(self):
        cmd = f"btcli wallet faucet --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        return self.cr.run(cmd)

    # Function to extract mnemonic from command output
    def extract_mnemonic(self, output, key_type):
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

    def regen_coldkey(self, coldkey_mnemonic):
        cmd = f'btcli wallet regen-coldkey --mnemonic "{coldkey_mnemonic}" --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}'

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Specify password for key encryption:": PASSWORD,   # Enter the password for encryption
            r"Retype your password:": PASSWORD,                 # Retype the password            
            r"File .*coldkey already exists. Overwrite\? \(y/N\)": "y",        # Respond 'yes' to overwrite coldkey
            r"File .*coldkeypub.txt already exists. Overwrite\? \(y/N\)": "y", # Respond 'yes' to overwrite coldkeypub
        }

        return self.cr.run_interactive(cmd, prompts_responses)


    # Remove wallet
    def remove_wallet(self):
        self.cr.run(
            f"rm -rf {WALLET_PATH}/{WALLET_NAME}",
            "Remove wallet"
        )

    ## Subnet-specific commands
    # Create subnet
    def create_subnet(self):
        cmd = f"btcli subnets create --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        child = pexpect.spawn(cmd)
        try:
            child.sendline('y')
            child.expect("Specify password for key encryption:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    def create_subnet2(self):
        cmd = f"btcli subnets create --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Specify password for key encryption:": PASSWORD,  # Enter the password for encryption
            r"Retype your password:": PASSWORD,                # Retype the password            
            r"File .*subnet already exists. Overwrite\? \(y/N\)": "y",  # Respond 'yes' to overwrite subnet
        }

        return self.cr.run_interactive(cmd, prompts_responses)


    # View subnetwork creation cost
    def view_lock_cost(self):
        self.cr.run(
            f"btcli subnets lock-cost --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "View subnetwork creation cost"
        )

    # List subnets
    def list_subnets(self, reuse_last=False, html=False):
        cmd = f"btcli subnets list --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        if reuse_last:
            cmd += " --reuse-last"
        if html:
            cmd += " --html"
        self.cr.run(cmd, "List subnets")

    # Display metagraph
    def display_metagraph(self, netuid=NETUID, reuse_last=False, html=False):
        cmd = f"btcli subnets metagraph --network {NETWORK} --netuid {netuid} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        if reuse_last:
            cmd += " --reuse-last"
        if html:
            cmd += " --html"
        self.cr.run(cmd, "Display metagraph")

    # Register neuron using Proof of Work
    def pow_register(self, netuid=NETUID, num_processors=None, update_interval=50, output_in_place=False, use_cuda=False, dev_id=0, threads_per_block=256):
        cmd = f"btcli subnets pow-register --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --netuid {netuid} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        if num_processors:
            cmd += f" --processors {num_processors}"
        cmd += f" --update-interval {update_interval}"
        if not output_in_place:
            cmd += " --no-output-in-place"
        if use_cuda:
            cmd += " --use-cuda"
        else:
            cmd += " --no-use-cuda"
        cmd += f" --dev-id {dev_id} --threads-per-block {threads_per_block}"
        self.cr.run(cmd)
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)   
        
    # Register neuron by recycling TAO tokens
    def register_neuron(self, netuid=NETUID, prompt=True):
        cmd = f"btcli subnets register --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --netuid {netuid}"
        if not prompt:
            cmd += " --no-prompt"
        print(cmd)
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

   ## Root-specific commands
   # List root network members
    def list_root_network_members(self):
        cmd = f"btcli root list --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
        self.cr.run(cmd)

    # Register a root neuron
    def root_register_neuron(self):
        cmd = f"btcli root register --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    # Boost the root network
    def boost_root_network(self):
        cmd = f"btcli root boost --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuid {NETUID} --amount {AMOUNT}"
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)
        

    # Get root network weights
    def get_root_network_weights(self):
        self.cr.run(
            f"btcli root get-weights --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "Get root network weights"
        )

    # Set root network weights
    def set_root_network_weights(self):
        cmd = f"btcli root set-weights --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuids {NETUID}" # --value {VALUE}
        print(cmd, "Set root network weights")
        child = pexpect.spawn(cmd)

        try:
            child.sendline('0.01')
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    # Slash the root network
    def slash_root_network(self):
        cmd =f"btcli root slash --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuid {NETUID} --amount {AMOUNT}"
        print(cmd)
        child = pexpect.spawn(cmd)

        try:
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    # Delegate stake
    def delegate_stake(self):
        cmd = f"btcli root delegate-stake --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --delegate-ss58key {DELEGATE_SS58KEY} --amount {AMOUNT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
        print(cmd)
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.interact()
            print(child.before.decode("utf-8"))  # Output from the command

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    # List root network delegates
    def list_root_network_delegates(self):
        self.cr.run(
            f"btcli root list-delegates --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
            "List root network delegates"
        )

    # Set senate take
    def set_senate_take(self):
        cmd = f"btcli root set-take --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --take {TAKE}"
        print(cmd)
        child = pexpect.spawn(cmd)

        try:
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    # Undelegate stake
    def undelegate_stake(self):
        cmd = f"btcli root undelegate-stake --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --delegate-ss58key {DELEGATE_SS58KEY} --amount {AMOUNT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
        print(cmd, "Undelegate stake")
        child = pexpect.spawn(cmd)

        try:
            child.expect("Enter password to unlock key:")
            child.sendline(PASSWORD)
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        print("-" * 50)

    ## Config-specific commands
    # Test config set setting
    def test_config_set(self):
        cmd = f"btcli config set --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
        self.cr.run(cmd)
        
    # Test config get setting
    def test_config_get(self):
        cmd = f"btcli config get"
        self.cr.run(cmd)
    
    # Test config clear setting
    def test_config_clear(self):
        cmd = f"btcli config clear --wallet-name --wallet-path  --wallet-hotkey --network --subtensor.chain_endpoint "
        child = pexpect.spawn(cmd)

        try:
            child.sendline('y')
            child.sendline('y')
            child.sendline('y')
            child.sendline('y')
            child.sendline('y')
            child.interact()
            print(child.before.decode("utf-8"))

        except pexpect.TIMEOUT:
            print("Command timed out.")
        except pexpect.EOF:
            print("Command ended unexpectedly.")
        except Exception as e:
            print(f"Unexpected error: {e}")

        
    # Test config metagraph setting
    def test_config_metagraph(self):
        cmd = f"btcli config metagraph --reset"
        self.cr.run(cmd)

