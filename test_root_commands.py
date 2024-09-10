# test_root.py

import subprocess
import pexpect
from colorama import Fore, Style, init
from config import NETWORK, CHAIN_ENDPOINT, WALLET_NAME, WALLET_PATH, HOTKEY, PASSWORD, NETUID, AMOUNT
from btcli_runner import run_btcli_command, run_interactive_btcli_command

def list_root_network_members():
    """
    List root network members.
    """
    return run_btcli_command(
        f"btcli root list --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "List root network members"
    )


def register_neuron(PASSWORD):
    """
    Register a neuron.
    """
    command = f"btcli root register --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}"
    print(f"Running command: {command}")

    # Spawn the command
    child = pexpect.spawn(command)

    # Wait for the yes/no prompt and respond with 'y'
    child.sendline('y')

    # Wait for the password prompt and send the password
    child.expect("Enter password to unlock key:")
    child.sendline(PASSWORD)  # Replace with your actual password
    # Print the output
    child.interact()



def boost_root_network():
    """
    Boost the root network.
    """
    command = f"btcli root boost --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuid {NETUID} --amount {AMOUNT}"
    print(f"Running command: {command}")
    child = pexpect.spawn(command)
    
    child.expect("Enter password to unlock key:")
    child.sendline(PASSWORD) 
    child.interact()
    child.expect("Do you want to set these root weights? [y/n]:")
    child.sendline('y')
    child.interact()


def get_root_network_weights():
    """
    Get root network weights.
    """
    return run_btcli_command(
        f"btcli root get-weights --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Get root network weights"
    )

def set_root_network_weights(value):
    """
    Set root network weights.
    """
    return run_btcli_command(
        f"btcli root set-weights --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuid {NETUID} --value {value}",
        "Set root network weights"
    )

def slash_root_network():
    """
    Slash the root network.
    """
    return run_btcli_command(
        f"btcli root slash --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --netuid {NETUID}",
        "Slash root network"
    )

def delegate_stake(delegate_ss58key, amount):
    """
    Delegate stake.
    """
    return run_btcli_command(
        f"btcli root delegate-stake --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --delegate-ss58key {delegate_ss58key} --amount {amount} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}",
        "Delegate stake"
    )

def list_root_network_delegates():
    """
    List root network delegates.
    """
    return run_btcli_command(
        f"btcli root list-delegates --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "List root network delegates"
    )

def set_senate_take(take):
    """
    Set senate take.
    """
    return run_btcli_command(
        f"btcli root set-take --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --take {take}",
        "Set senate take"
    )

def undelegate_stake(delegate_ss58key, amount):
    """
    Undelegate stake.
    """
    return run_btcli_command(
        f"btcli root undelegate-stake --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --delegate-ss58key {delegate_ss58key} --amount {amount} --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY}",
        "Undelegate stake"
    )

def test_btcli_root_commands():
    #list_root_network_members()
    #register_neuron(PASSWORD)
    boost_root_network()
    #get_root_network_weights()
    #set_root_network_weights(1, 0.5)
   # slash_root_network(1)
    #delegate_stake("<delegate-ss58key>", 10)
    #list_root_network_delegates()
    #set_senate_take(0.5)
    #undelegate_stake("<delegate-ss58key>", 5)

if __name__ == "__main__":
    test_btcli_root_commands()