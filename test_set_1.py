import pytest
from btcli_test.config import WALLET_NAME, WALLET_PATH, HOTKEY, PASSWORD
from command_runner import CommandRunner
from btcli_test.general import BtcliTest

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(wd="/Users/galina/repos/btcli-test", output=output)

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

# Test to run faucet for wallet
def test_faucet_wallet(cr):
    btclitest = BtcliTest(cr)
    btclitest.faucet_wallet()

# Test config set setting
def test_config_set(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_set()

# Test config get setting
def test_config_get(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_get()

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

# Test to create a subnet
def test_create_subnet(cr):
    btclitest = BtcliTest(cr)
    btclitest.create_subnet()

# Test to list subnets
def test_list_subnets(cr):
    btclitest = BtcliTest(cr)
    btclitest.list_subnets()

# Test to view subnetwork creation cost
def test_view_lock_cost(cr):
    btclitest = BtcliTest(cr)
    btclitest.view_lock_cost()

# Test to display metagraph
def test_display_metagraph(cr):
    btclitest = BtcliTest(cr)
    btclitest.display_metagraph()

# Test to register neuron by recycling TAO tokens
def test_register_neuron(cr):
    btclitest = BtcliTest(cr)
    btclitest.register_neuron()

# Test to register a neuron
def test_root_register_neuron(cr):
    btclitest = BtcliTest(cr)
    btclitest.root_register_neuron()

# Test to list root network members
def test_list_root_network_members(cr):
    btclitest = BtcliTest(cr)
    btclitest.list_root_network_members()

