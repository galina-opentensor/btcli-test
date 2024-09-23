import pytest
from btcli_test.general import BtcliTest


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


# Test to view subnetwork creation cost
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_view_lock_cost(btcli_test):
    btcli_test.view_lock_cost()

# Test to list subnets
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_list_subnets(btcli_test):
    btcli_test.list_subnets()

# Test to display metagraph
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_display_metagraph(btcli_test):
    btcli_test.display_metagraph()

# # Test to register neuron using Proof of Work
# # def test_pow_register(cr):
# #     btclitest = BtcliTest(cr)
# #     btclitest.pow_register()