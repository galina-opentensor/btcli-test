import pytest
from btcli_test.general import BtcliTest

# Test to register a neuron
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_root_register_neuron(btcli_test):
    btcli_test.root_register_neuron()

# Test to boost the root network
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_boost_root_network(btcli_test):
    btcli_test.boost_root_network()

# Test to get root network weights
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_get_root_network_weights(btcli_test):
    btcli_test.get_root_network_weights()

# Test to set root network weights
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_set_root_network_weights(btcli_test):
    btcli_test.set_root_network_weights()

# Test to slash the root network
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_slash_root_network(btcli_test):
    btcli_test.slash_root_network()

# Test to delegate stak
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
], indirect=True)
def test_delegate_stake(btcli_test, ):
    btcli_test.delegate_stake()


# # Test to list root network delegates
# def test_list_root_network_delegates(cr):
#     btclitest = BtcliTest(cr)
#     btclitest.list_root_network_delegates()

# # Test to set senate take
# def test_set_senate_take(cr):
#     btclitest = BtcliTest(cr)
#     btclitest.set_senate_take()

# # Test to undelegate stake
# def test_undelegate_stake(cr):
#     btclitest = BtcliTest(cr)
#     btclitest.undelegate_stake()

# # Test to list root network members
# def test_list_root_network_members(cr):
#     btclitest = BtcliTest(cr)
#     btclitest.list_root_network_members()