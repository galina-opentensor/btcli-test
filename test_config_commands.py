import pytest
from btcli_test.config import NETWORK, CHAIN_ENDPOINT, WALLET_NAME, WALLET_PATH, HOTKEY, USE_PASSWORD, PASSWORD, NETUID, VALUE, DELEGATE_SS58KEY, AMOUNT
from command_runner import CommandRunner
from btcli_test.general import BtcliTest

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(output=output)

# Test config set setting
def test_config_set(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_set()

# Test config get setting
def test_config_get(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_get()

# Test config clear setting
def test_config_clear(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_clear()

# Test config metagraph setting
def test_config_metagraph(cr):
    btclitest = BtcliTest(cr)
    btclitest.test_config_get()