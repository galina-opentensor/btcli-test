import pytest
import time
from btcli_test.config import WALLET_PATH
from btcli_test.general import BtcliTest


# Test to create a coldkey and store the mnemonic
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_create_coldkey(btcli_test, mnemonic_storage): 
    mnemonic = btcli_test.create_coldkey()

    # Save mnemonic in mnemonic_storage for later use
    mnemonic_storage[f"{btcli_test.wallet_name}_coldkey_mnemonic"] = mnemonic
    assert mnemonic is not None, "Failed to create coldkey and extract mnemonic."

# Test to create a hotkey
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
    ("wallet1", "hotkey2"),
], indirect=True)
def test_create_hotkey(btcli_test, mnemonic_storage):
    mnemonic = btcli_test.create_hotkey()

    # Save mnemonic in mnemonic_storage for later use
    mnemonic_storage[f"{btcli_test.wallet_name}_hotkey_mnemonic"] = mnemonic
    assert mnemonic is not None, "Failed to create hotkey and extract mnemonic."
    

# Test regen coldkey
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_regen_coldkey(btcli_test, mnemonic_storage):

    # Retrieve the mnemonic from the mnemonic_storage
    coldkey_mnemonic = mnemonic_storage.get(f"{btcli_test.wallet_name}_coldkey_mnemonic")
    
    assert coldkey_mnemonic is not None, "Mnemonic not found. Ensure test_create_coldkey runs first."

    # Regenerate coldkey using the saved mnemonic
    result = btcli_test.regen_coldkey(coldkey_mnemonic)
    
    # Validate that the regen process completed
    assert result is not None, "Failed to regenerate coldkey using the mnemonic."

# Test regen hotkey
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey2"),
], indirect=True)
def test_regen_hotkey(btcli_test, mnemonic_storage):
    # Retrieve the mnemonic from the mnemonic_storage
    hotkey_mnemonic = mnemonic_storage.get(f"{btcli_test.wallet_name}_hotkey_mnemonic")
    
    assert hotkey_mnemonic is not None, "Mnemonic not found. Ensure test_create_hotkey runs first."
   
    # Regenerate coldkey using the saved mnemonic
    result = btcli_test.regen_hotkey(hotkey_mnemonic)
    
    # Validate that the regen process completed
    assert result is not None, "Failed to regenerate coldkey using the mnemonic."

# Test to check wallet list
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)

def test_check_wallet_list(btcli_test):
    btcli_test.check_wallet_list()

# Test to run faucet for wallet
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)

def test_faucet_wallet(btcli_test):
    btcli_test.faucet_wallet()
    wait_time = 420
    print(f"Waiting for {wait_time} seconds for the faucet wallet request to process...")
    time.sleep(wait_time)

# Test to check wallet balance
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)

def test_check_wallet_balance(btcli_test):
    btcli_test.check_wallet_balance()

# Test to check wallet transaction history
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)

def test_check_wallet_history(btcli_test):
    btcli_test.check_wallet_history()

# Test to inspect wallet
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
# Test to inspect wallet
def test_inspect_wallet(btcli_test):
    btcli_test.inspect_wallet()

# Test to get wallet overview
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
# Test to get wallet overview
def test_wallet_overview(btcli_test):
    btcli_test.wallet_overview()

# Test to list subnets
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_list_subnets(btcli_test):
    btcli_test.list_subnets()

#Test to create a subnet
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_create_subnet(btcli_test):
    btcli_test.create_subnet()

# Test to register neuron by recycling TAO tokens
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_register_neuron(btcli_test):
    btcli_test.register_neuron()

# Test to register a neuron
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_root_register_neuron(btcli_test):
    btcli_test.root_register_neuron()


# Test to delegate stak
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_delegate_stake(btcli_test, ):
    btcli_test.delegate_stake()

# Remove wallet
@pytest.mark.parametrize("wallet_name", [
    ("wallet1"),
])
def test_remove_wallet(cr, wallet_name):
    wallet_path = f"{WALLET_PATH}"
    print(f"I will remove {wallet_name} wallet from path:", wallet_path)
    btclitest = BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
    )
    btclitest.remove_wallet()