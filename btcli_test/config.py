import os

## TODO: create different groups with different values   
# Bittensor network and chain endpoint configuration
NETWORK = "local"  # Substitute with the actual network if needed
CHAIN_ENDPOINT = "ws://127.0.0.1:9946"  # Substitute with the actual chain endpoint
WALLET_NAME = "test-wallet-1"
WALLET_PATH = os.path.join(os.getenv('HOME'), '.bittensor', 'wallets') 
HOTKEY = "default"  # Substitute with the actual hotkey if needed
PASSWORD ="Strong!" #Password
USE_PASSWORD = "--no-use-password" # --use-password   
NETUID = "2"
AMOUNT = "0.5"
VALUE = "0.01"
TAKE = "9"
DELEGATE_SS58KEY = "5FedQi3e7SjwHHojk5gNGCAZyZaR2TEVg8pM2riDSFJHcc7c"
#SCENARIOS = "qualification"
ENV = os.environ