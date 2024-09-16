import re
from btcli_test.config import USE_PASSWORD, PASSWORD
from command_runner import CommandRunner

class BtcliTest:
    def __init__(
        self, 
        cr: CommandRunner,
        wallet_name: str = "",
        wallet_path: str = "",
        hotkey: str = "",
        password: str = PASSWORD,
        use_password: str = USE_PASSWORD  
    ):
        self.cr = cr
        self.wallet_name = wallet_name
        self.wallet_path = wallet_path
        self.hotkey = hotkey
        self.password = password
        self.use_password = use_password

    # Create coldkey
    def create_coldkey(self):
        cmd = (
            f"btcli wallet new-coldkey" 
            f" --wallet-name {self.wallet_name}" 
            f" --wallet-path {self.wallet_path}"
            f" --hotkey {self.hotkey}"
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

    # Check wallet list
    def check_wallet_list(self):
        cmd = (
            f"btcli wallet list" 
            f" --wallet-path {self.wallet_path}"
        )
        self.cr.run(cmd)

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

    # Remove wallet
    def remove_wallet(self):
        cmd = f"rm -rf {self.wallet_path}/{self.wallet_name}"
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
            r"File .* already exists. Overwrite\? \(y/N\)": "y",        # Respond 'yes' to overwrite hotkey
        }

        return self.cr.run_interactive(cmd, prompts_responses)