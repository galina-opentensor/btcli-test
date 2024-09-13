import pytest
from btcli_test.config import NETWORK, CHAIN_ENDPOINT, WALLET_NAME, WALLET_PATH, HOTKEY, USE_PASSWORD, PASSWORD, NETUID, VALUE, DELEGATE_SS58KEY, AMOUNT
from command_runner import CommandRunner
from btcli_test.general import BtcliTest

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")
    return CommandRunner(output=output)

# Test to register a neuron
def test_root_register_neuron(cr):
    btclitest = BtcliTest(cr)
    btclitest.root_register_neuron()

# Test to boost the root network
def test_boost_root_network(cr):
    btclitest = BtcliTest(cr)
    btclitest.boost_root_network()

# Test to get root network weights
def test_get_root_network_weights(cr):
    btclitest = BtcliTest(cr)
    btclitest.get_root_network_weights()

# Test to set root network weights
def test_set_root_network_weights(cr):
    btclitest = BtcliTest(cr)
    btclitest.set_root_network_weights()

# Test to slash the root network
def test_slash_root_network(cr):
    btclitest = BtcliTest(cr)
    btclitest.slash_root_network()

# Test to delegate stak
def test_delegate_stake(cr):
    btclitest = BtcliTest(cr)
    btclitest.delegate_stake()

# Test to list root network delegates
def test_list_root_network_delegates(cr):
    btclitest = BtcliTest(cr)
    btclitest.list_root_network_delegates()

# Test to set senate take
def test_set_senate_take(cr):
    btclitest = BtcliTest(cr)
    btclitest.set_senate_take()

# Test to undelegate stake
def test_undelegate_stake(cr):
    btclitest = BtcliTest(cr)
    btclitest.undelegate_stake()

# Test to list root network members
def test_list_root_network_members(cr):
    btclitest = BtcliTest(cr)
    btclitest.list_root_network_members()