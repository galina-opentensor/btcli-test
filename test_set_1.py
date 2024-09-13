import pytest
from btcli_test.config import WALLET_NAME, WALLET_PATH, HOTKEY, PASSWORD
from command_runner import CommandRunner
from btcli_test.general import BtcliTest
import os

# Fixture to initialize the CommandRunner
@pytest.fixture
def cr():
    output = open("/dev/stdout", "a")  # Directing output to stdout for logging
    return CommandRunner(output=output)

# Fixture to store mnemonic between tests
@pytest.fixture(scope="session")
def mnemonic_storage():
    return {}

# test_hello.py
def test_hello_world():
    greeting = "Hello, World!"
    assert greeting == "Hello, World!"

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

# Test to get wallet overview
def test_wallet_overview(cr):
    btclitest = BtcliTest(cr)
    btclitest.wallet_overview()
