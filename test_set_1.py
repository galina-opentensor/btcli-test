import pytest
from btcli_test.config import WALLET_PATH
from command_runner import CommandRunner
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

# Test to remove wallet
@pytest.mark.parametrize("wallet_name", [
    ("wallet1"),
    ("wallet2"),
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

# Parameterized test to create a coldkey and store the mnemonic
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
    ("wallet2", "hotkey2"),
])
def test_create_coldkey(cr, mnemonic_storage, wallet_name, hotkey): 
    wallet_path = f"{WALLET_PATH}"
    btclitest = BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
        hotkey=hotkey
    )
    mnemonic = btclitest.create_coldkey()

    # Save mnemonic in mnemonic_storage for later use
    mnemonic_storage[f"{wallet_name}_coldkey_mnemonic"] = mnemonic
    assert mnemonic is not None, "Failed to create coldkey and extract mnemonic."

# Parameterized test to create a hotkey
@pytest.mark.parametrize("wallet_name, hotkey", [
    ("wallet1", "hotkey1"),
    ("wallet2", "hotkey2"),
])
def test_create_hotkey(cr, mnemonic_storage, wallet_name, hotkey):
    wallet_path = f"{WALLET_PATH}"
    btclitest = BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
        hotkey=hotkey
    )
    mnemonic = btclitest.create_hotkey()

    # Save mnemonic in mnemonic_storage for later use
    mnemonic_storage[f"{wallet_name}_hotkey_mnemonic"] = mnemonic
    assert mnemonic is not None, "Failed to create hotkey and extract mnemonic."


# Test to check wallet list
def test_check_wallet_list(cr):
    wallet_path = WALLET_PATH  # Use a default path or modify as needed
    btclitest = BtcliTest(cr, wallet_path=wallet_path)
    btclitest.check_wallet_list()


def test_regen_coldkey(cr, mnemonic_storage):
    wallet_name = "wallet1" 
    wallet_path = f"{WALLET_PATH}"
    hotkey = "hotkey1"  

    # Retrieve the mnemonic from the mnemonic_storage
    coldkey_mnemonic = mnemonic_storage.get(f"{wallet_name}_coldkey_mnemonic")
    
    assert coldkey_mnemonic is not None, "Mnemonic not found. Ensure test_create_coldkey runs first."
    
    # Initialize BtcliTest with wallet_name and other details
    btclitest = BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
        hotkey=hotkey
    )

    # Regenerate coldkey using the saved mnemonic
    result = btclitest.regen_coldkey(coldkey_mnemonic)
    
    # Validate that the regen process completed
    assert result is not None, "Failed to regenerate coldkey using the mnemonic."

def test_regen_hotkey(cr, mnemonic_storage):
    wallet_name = "wallet1" 
    wallet_path = f"{WALLET_PATH}"
    hotkey = "hotkey1"  

    # Retrieve the mnemonic from the mnemonic_storage
    hotkey_mnemonic = mnemonic_storage.get(f"{wallet_name}_hotkey_mnemonic")
    
    assert hotkey_mnemonic is not None, "Mnemonic not found. Ensure test_create_hotkey runs first."
    
    # Initialize BtcliTest with wallet_name and other details
    btclitest = BtcliTest(
        cr,
        wallet_name=wallet_name,
        wallet_path=wallet_path,
        hotkey=hotkey
    )

    # Regenerate coldkey using the saved mnemonic
    result = btclitest.regen_hotkey(hotkey_mnemonic)
    
    # Validate that the regen process completed
    assert result is not None, "Failed to regenerate coldkey using the mnemonic."