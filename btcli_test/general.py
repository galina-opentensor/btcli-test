import re
from btcli_test.config import USE_PASSWORD, PASSWORD, NETWORK, CHAIN_ENDPOINT
from command_runner import CommandRunner

class BtcliTest:
    def __init__(
        self, 
        cr: CommandRunner,
        wallet_name: str = "",
        wallet_path: str = "",
        hotkey: str = "",
        netuid: str = "",
        password: str = PASSWORD,
        use_password: str = USE_PASSWORD,
        network: str = NETWORK,
        chain_endpoint: str = CHAIN_ENDPOINT,  
    ):
        self.cr = cr
        self.wallet_name = wallet_name
        self.wallet_path = wallet_path
        self.hotkey = hotkey
        self.netuid = netuid
        self.password = password
        self.use_password = use_password
        self.network = network
        self.chain_endpoint = chain_endpoint

    # Create coldkey
    def create_coldkey(self):
        cmd = (
            f"btcli wallet new-coldkey" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            #f" --hotkey {self.hotkey}"
            f" {self.use_password}"
            f" --n-words 12"
        )
        output = self.cr.run(cmd)
        return self.extract_mnemonic(output, "coldkey")

    # Create hotkey
    def create_hotkey(self):
        cmd = (
            f"btcli wallet new-hotkey" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" {self.use_password}"
            f" --n-words 12"
        )
        output = self.cr.run(cmd)
        return self.extract_mnemonic(output, "hotkey")


    # Function to extract mnemonic from command output
    def extract_mnemonic(self, output, key_type):
        """
        Extracts the mnemonic from the btcli command output based on key type (coldkey or hotkey).
        """
        mnemonic_pattern = re.compile(rf"The mnemonic to the new {key_type} is:\s*(.+)")
        match = mnemonic_pattern.search(output)
        if match:
            mnemonic = match.group(1)
            print(f"Mnemonic extracted: {mnemonic}")
            return mnemonic
        else:
            print(f"Mnemonic not found in the output for {key_type}.")
            return None
        
    def extract_ss58_address(self, output, hotkey_name):
        """
        Extracts the ss58 address from the btcli command output based on hotkey name.
        """
        address_pattern = re.compile(rf"Hotkey {hotkey_name}\s+ss58_address\s+(\S+)")
        match = address_pattern.search(output)
        
        if match:
            ss58_address = match.group(1)
            print(f"{hotkey_name} ss58_address extracted: {ss58_address}")
            return ss58_address
        else:
            print(f"{hotkey_name} ss58_address not found in the output.")
            return None


    # Remove wallet
    def remove_wallet(self):
        cmd = f"rm -rf {self.wallet_path}/{self.wallet_name}"
        print(cmd)
        self.cr.run(cmd)


    # Regenerate coldkey using a mnemonic
    def regen_coldkey(self, mnemonic):
        cmd = (
            f"btcli wallet regen-coldkey" 
            f" --mnemonic \"{mnemonic}\""
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
        )

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Specify password for key encryption:": self.password,   # Enter the password for encryption
            r"Retype your password:": self.password,                 # Retype the password            
            r"File .*coldkey already exists. Overwrite\? \(y/N\)": "y",        # Respond 'yes' to overwrite coldkey
            r"File .*coldkeypub.txt already exists. Overwrite\? \(y/N\)": "y", # Respond 'yes' to overwrite coldkeypub
        }

        return self.cr.run_interactive(cmd, prompts_responses)


    # Regenerate hotkey using a mnemonic
    def regen_hotkey(self, mnemonic):
        cmd = (
            f"btcli wallet regen-hotkey" 
            f" --mnemonic \"{mnemonic}\""
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
        )

        # Expected prompts and their respective responses
        prompts_responses = {       
            r"File .* already exists. Overwrite\? \(y/N\)": "y",
        }

        return self.cr.run_interactive(cmd, prompts_responses)
    

    # Check wallet list
    def check_wallet_list(self):
        cmd = (
            f"btcli wallet list" 
            f" --wallet-path {self.wallet_path}"
        )
        output = self.cr.run(cmd)
    
        ss58_address = self.extract_ss58_address(output, "hotkey1")
        return ss58_address

    # Check wallet balance
    def check_wallet_balance(self):
        cmd = (
            f"btcli wallet balance" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)

    # Check wallet transaction history
    def check_wallet_history(self):
        cmd = (
            f"btcli wallet history" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
        )
        self.cr.run(cmd)

    # Inspect wallet
    def inspect_wallet(self):
        cmd = (
            f"btcli wallet inspect" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)
    
    # Get wallet overview
    def wallet_overview(self):
        cmd = (
            f"btcli wallet overview" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)

    # Check wallet swap 
    def check_wallet_swap(self):
        cmd = (
            f"btcli wallet swap-hotkey" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)

    # Faucet wallet
    def faucet_wallet(self):
        cmd = (
            f"btcli wallet faucet" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Enter password to unlock key:": self.password,
        }
        return self.cr.run_interactive(cmd, prompts_responses)
    
    ## Subnet-specific commands
    def create_subnet(self):
        cmd = (
            f"btcli subnet create"
            f" --wallet-name {self.wallet_name}"
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            " --no-prompt"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )

        # Expected prompts and their respective responses
        prompts_responses = {
            r"Enter password to unlock key:": self.password,  # Respond to password prompt
        }

        return self.cr.run_interactive(cmd, prompts_responses)

    
    # Register neuron by recycling TAO tokens
    def register_neuron(self, netuid="3"):
        cmd = (
            f"btcli subnet register"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --netuid {netuid}"
            f" --network {self.network}"
            " --no-prompt"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )

        prompts_responses = {
            r"Enter password to unlock key:": self.password,
        }

        return self.cr.run_interactive(cmd, prompts_responses)


    
    # View subnetwork creation cost
    def view_lock_cost(self):
        cmd = (
            f"btcli subnets lock-cost"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"

        )
        return self.cr.run(cmd)

    # List subnets
    def list_subnets(self, reuse_last=False, html=False):
        cmd = (
            f"btcli subnets list" 
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        if reuse_last:
            cmd += " --reuse-last"
        if html:
            cmd += " --html"
        return self.cr.run(cmd)
    
    # Display metagraph
    def display_metagraph(self, netuid = '1', reuse_last=False, html=False):
        cmd = (
            f"btcli subnets metagraph" 
            f" --netuid {netuid}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        if reuse_last:
            cmd += " --reuse-last"
        if html:
            cmd += " --html"
        return self.cr.run(cmd)

    # Register neuron using Proof of Work
    def pow_register(self, num_processors=None, update_interval=50, output_in_place=False, use_cuda=False, dev_id=0, threads_per_block=256):
        cmd = (
            f"btcli subnets pow-register"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --netuid {self.netuid}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
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
                # Expected prompts and their respective responses
        prompts_responses = {
            r"Enter password to unlock key:": self.password,
        }
        return self.cr.run_interactive(cmd, prompts_responses)

        
## Root-specific commands
   # List root network members
    def list_root_network_members(self):
        cmd = (
            f"btcli root list" 
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)

    # Register a root neuron
    def root_register_neuron(self):
        cmd = (
            f"btcli root register"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            " --no-prompt"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )

        prompts_responses = {
            r"Enter password to unlock key:": self.password,
        }
        return self.cr.run_interactive(cmd, prompts_responses)


    # Boost the root network
    def boost_root_network(self, netuid='1', amount='0.01'):
        cmd = (
            f"btcli root boost" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --netuid {netuid}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
            f" --amount {amount}"
            " --no-prompt"
        )
        prompts_responses = {
            r".*Enter password to unlock key:.*": self.password,
        }
        return self.cr.run_interactive(cmd, prompts_responses)

    # Get root network weights
    def get_root_network_weights(self):
        cmd = (
            f"btcli root get-weights" 
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
        )
        return self.cr.run(cmd)
    
    # Set root network weights
    def set_root_network_weights(self, netuid='1', amount='0.1'):
        cmd = (
            f"btcli root set-weights"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --netuids {netuid}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
            f" --weights {amount}"
            " --no-prompt"
        )

        prompts_responses = {
            r"Enter password to unlock key:": self.password,
        }
        return self.cr.run_interactive(cmd, prompts_responses)

    # Slash the root network
    def slash_root_network(self, netuid='1', amount='0.1'):
        cmd = (
            f"btcli root slash"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --netuid {netuid}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
            f" --weights {amount}"
        )

        prompts_responses = {
            r"Enter password to unlock key:": self.password,
            r".*y/n.*": "y",
        }
        return self.cr.run_interactive(cmd, prompts_responses)
    

    # Delegate stake
    def delegate_stake(self, amount='100', netuid='1'):
        # Ensure delegate_ss58key is available
        if not hasattr(self, 'delegate_ss58key') or not self.delegate_ss58key:
            # Try to extract the delegate_ss58key from the wallet list if it's not set
            print("Delegate ss58key is not set, checking wallet list to extract it.")
            self.delegate_ss58key = self.check_wallet_list()

            # If still not set, raise an error
            if not self.delegate_ss58key:
                raise ValueError("Delegate ss58key is not set. Please ensure the hotkey has been created and the ss58key is extracted.")

        cmd = (
            f"btcli root delegate-stake"
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
            f" --network {self.network}"
            f" --subtensor.chain_endpoint {self.chain_endpoint}"
            f" --amount {amount}"
            f" --delegate-ss58key {self.delegate_ss58key}"  
        )

        prompts_responses = {
            r"Enter password to unlock key:": self.password,
            r".*y/n.*": "y",
        }
        return self.cr.run_interactive(cmd, prompts_responses)



    # # List root network delegates
    # def list_root_network_delegates(self):
    #     self.cr.run(
    #         f"btcli root list-delegates --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
    #         "List root network delegates"
    #     )

    # # Set senate take
    # def set_senate_take(self):
    #     cmd = f"btcli root set-take --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --take {TAKE}"
    #     print(cmd)
    #     child = pexpect.spawn(cmd)

    #     try:
    #         child.expect("Enter password to unlock key:")
    #         child.sendline(PASSWORD)
    #         child.sendline('y')
    #         child.interact()
    #         print(child.before.decode("utf-8"))

    #     except pexpect.TIMEOUT:
    #         print("Command timed out.")
    #     except pexpect.EOF:
    #         print("Command ended unexpectedly.")
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")

    #     print("-" * 50)

    # # Undelegate stake
    # def undelegate_stake(self):
    #     cmd = f"btcli root undelegate-stake --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --delegate-ss58key {DELEGATE_SS58KEY} --amount {AMOUNT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
    #     print(cmd, "Undelegate stake")
    #     child = pexpect.spawn(cmd)

    #     try:
    #         child.expect("Enter password to unlock key:")
    #         child.sendline(PASSWORD)
    #         child.sendline('y')
    #         child.interact()
    #         print(child.before.decode("utf-8"))

    #     except pexpect.TIMEOUT:
    #         print("Command timed out.")
    #     except pexpect.EOF:
    #         print("Command ended unexpectedly.")
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")

    #     print("-" * 50)

    # ## Config-specific commands
    # # Test config set setting
    # def test_config_set(self):
    #     cmd = f"btcli config set --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
    #     self.cr.run(cmd)
        
    # # Test config get setting
    # def test_config_get(self):
    #     cmd = f"btcli config get"
    #     self.cr.run(cmd)
    
    # # Test config clear setting
    # def test_config_clear(self):
    #     cmd = f"btcli config clear --wallet-name --wallet-path  --wallet-hotkey --network --subtensor.chain_endpoint "
    #     child = pexpect.spawn(cmd)

    #     try:
    #         child.sendline('y')
    #         child.sendline('y')
    #         child.sendline('y')
    #         child.sendline('y')
    #         child.sendline('y')
    #         child.interact()
    #         print(child.before.decode("utf-8"))

    #     except pexpect.TIMEOUT:
    #         print("Command timed out.")
    #     except pexpect.EOF:
    #         print("Command ended unexpectedly.")
    #     except Exception as e:
    #         print(f"Unexpected error: {e}")

        
    # # Test config metagraph setting
    # def test_config_metagraph(self):
    #     cmd = f"btcli config metagraph --reset"
    #     self.cr.run(cmd)



