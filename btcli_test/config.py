import os

## TODO: create different groups with different values   
# Bittensor network and chain endpoint configuration
NETWORK = "local"  # Substitute with the actual network if needed
CHAIN_ENDPOINT = "ws://127.0.0.1:9946"  # Substitute with the actual chain endpoint
WALLET_NAME = "btcli-test-3"
WALLET_PATH = os.path.join(os.getenv('HOME'), '.bittensor', 'wallets') 
HOTKEY = "btcli-test-3-hotkey"  # Substitute with the actual hotkey if needed
PASSWORD ="Strong!" #Password
USE_PASSWORD = "--no-use-password" # --use-password   
NETUID = "3"
AMOUNT = "0.5"
VALUE = "0.01"
TAKE = "9"
DELEGATE_SS58KEY = "5E7AtkoUcSP5bHpNM6tUEVsnqKAUnCxuqjBRYzwk5oneZd9L"
# Coldkey btcli-test  ss58_address 5FBtnPJhfs5xKR4M8K8THuy74Qc3WrNxBBj1YwZXqdau1dWo
#│   └── Hotkey btcli-test-hotkey  ss58_address 5E7AtkoUcSP5bHpNM6tUEVsnqKAUnCxuqjBRYzwk5oneZd9L
#SCENARIOS = "qualification"
ENV = os.environ