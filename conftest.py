import pytest
from command_runner import CommandRunner
from btcli_test.config import WALLET_PATH, NETWORK, CHAIN_ENDPOINT
from btcli_test.general import BtcliTest

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(output=output)

# Fixture to store mnemonic between tests
@pytest.fixture(scope="session")
def mnemonic_storage():
    return {}

# Fixture to store mnemonic between tests
@pytest.fixture(scope="session")
def ss58_address_storage():
    return {}

# Fixture to provide wallet names
@pytest.fixture
def wallet_name(request):
    return request.param

@pytest.fixture
def hotkey(request):
    return request.param

@pytest.fixture
def netuid(request):
    return request.param

@pytest.fixture
def network():
    return NETWORK  # Use the default or customize as needed

# Fixture for chain_endpoint
@pytest.fixture
def chain_endpoint():
    return CHAIN_ENDPOINT

# Fixture to initialize the BtcliTest object
@pytest.fixture
def btcli_test(cr, wallet_name, hotkey, network, chain_endpoint):
    wallet_path = f"{WALLET_PATH}"
    return BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
        hotkey=hotkey,
        network=network,
        chain_endpoint=chain_endpoint,
    )

