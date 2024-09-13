import pytest
import os
from btcli_test.config import WALLET_NAME, WALLET_PATH, HOTKEY, PASSWORD
from command_runner import CommandRunner
from btcli_test.general import BtcliTest

@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(output=output)

# Fixture to store mnemonic between tests
@pytest.fixture(scope="session")
def mnemonic_storage():
    return {}

# Test to remove wallet
def test_remove_wallet(cr):
    btclitest = BtcliTest(cr)
    btclitest.remove_wallet()

# Test to create a coldkey and store the mnemonic
def test_create_coldkey(cr, mnemonic_storage):
    btclitest = BtcliTest(cr)
    mnemonic = btclitest.create_coldkey()
    
    # Save mnemonic in mnemonic_storage for later use
    mnemonic_storage["coldkey_mnemonic"] = mnemonic
    assert mnemonic is not None, "Failed to create coldkey and extract mnemonic."

# Test to create a hotkey
def test_create_hotkey(cr):
    btclitest = BtcliTest(cr)
    btclitest.create_hotkey()

# Test to check wallet list
def test_check_wallet_list(cr):
    btclitest = BtcliTest(cr)
    btclitest.check_wallet_list()

# Test to check wallet balance
def test_check_wallet_balance(cr):
    btclitest = BtcliTest(cr)
    btclitest.check_wallet_balance()

# Test to check wallet transaction history
def test_check_wallet_history(cr):
    btclitest = BtcliTest(cr)
    btclitest.check_wallet_history()

# Test to inspect wallet
def test_inspect_wallet(cr):
    btclitest = BtcliTest(cr)
    btclitest.inspect_wallet()

# Test to get wallet overview
def test_wallet_overview(cr):
    btclitest = BtcliTest(cr)
    btclitest.wallet_overview()

# Test to check wallet swap
# def test_check_wallet_swap(cr):
#     btclitest = BtcliTest(cr)
#     btclitest.check_wallet_swap()

# Test to run faucet for wallet
def test_faucet_wallet(cr):
    btclitest = BtcliTest(cr)
    btclitest.faucet_wallet()

# Test to regenerate coldkey using the mnemonic from the first test
def test_regen_coldkey(cr, mnemonic_storage):
    btclitest = BtcliTest(cr)
    
    # Retrieve the mnemonic from the first test
    coldkey_mnemonic = mnemonic_storage.get("coldkey_mnemonic")
    
    assert coldkey_mnemonic is not None, "Mnemonic not found. Ensure test_create_coldkey runs first."
    
    # Regenerate coldkey using the saved mnemonic
    btclitest.regen_coldkey(coldkey_mnemonic)

# Test to remove wallet
def test_remove_wallet(cr):
    btclitest = BtcliTest(cr)
    btclitest.remove_wallet()
