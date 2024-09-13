import pytest
from btcli_test.config import WALLET_NAME, WALLET_PATH, HOTKEY, NETWORK, CHAIN_ENDPOINT
from command_runner import CommandRunner
from btcli_test.general import BtcliTest

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(output=output)

# Test to create a subnet
def test_create_subnet(cr):
    btclitest = BtcliTest(cr)
    btclitest.create_subnet()

# Test to view subnetwork creation cost
def test_view_lock_cost(cr):
    btclitest = BtcliTest(cr)
    btclitest.view_lock_cost()

# Test to list subnets
def test_list_subnets(cr):
    btclitest = BtcliTest(cr)
    btclitest.list_subnets()

# Test to display metagraph
def test_display_metagraph(cr):
    btclitest = BtcliTest(cr)
    btclitest.display_metagraph()

# Test to register neuron using Proof of Work
def test_pow_register(cr):
    btclitest = BtcliTest(cr)
    btclitest.pow_register()

# Test to register neuron by recycling TAO tokens
def test_register_neuron(cr):
    btclitest = BtcliTest(cr)
    btclitest.register_neuron()
