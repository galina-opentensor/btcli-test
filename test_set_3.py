import pytest
from btcli_test.general import BtcliTest


# Test to create a subnet
# @pytest.mark.parametrize("wallet_name, hotkey", [
#     ("wallet1", "hotkey1"),
# ], indirect=True)
# def test_create_subnet(btcli_test):
#     btcli_test.create_subnet()

# @pytest.mark.parametrize("wallet_name, hotkey", [
#     ("wallet1", "hotkey1"),
# ], indirect=True)
# # Test to register neuron by recycling TAO tokens
# def test_register_neuron(btcli_test):
#     btcli_test.register_neuron()

@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
# Test to view subnetwork creation cost
def test_view_lock_cost(btcli_test):
    btcli_test.view_lock_cost()


@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
# Test to list subnets
def test_list_subnets(btcli_test):
    btcli_test.list_subnets()

@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
# Test to display metagraph
def test_display_metagraph(btcli_test):
    btcli_test.display_metagraph()

# # Test to register neuron using Proof of Work
# # def test_pow_register(cr):
# #     btclitest = BtcliTest(cr)
# #     btclitest.pow_register()