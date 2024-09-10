# test_subnets.py

import subprocess
import pexpect
from colorama import Fore, Style, init
from config import NETWORK, CHAIN_ENDPOINT, WALLET_NAME, WALLET_PATH, HOTKEY
from btcli_runner import run_btcli_command, run_interactive_btcli_command


def create_subnet():
    """
    Registers a new subnetwork.
    """
    return run_btcli_command(
        f"btcli subnets create --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "Create subnetwork"
    )

def view_lock_cost():
    """
    Views the cost for creating a new subnetwork.
    """
    return run_btcli_command(
        f"btcli subnets lock-cost --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}",
        "View subnetwork creation cost"
    )

def list_subnets(reuse_last=False, html=False):
    """
    Lists all subnets and their information.
    """
    command = f"btcli subnets list --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
    if reuse_last:
        command += " --reuse-last"
    if html:
        command += " --html"
    return run_btcli_command(command, "List subnets")

def display_metagraph(netuid=None, reuse_last=False, html=False):
    """
    Displays the metagraph of a subnetwork.
    """
    command = f"btcli subnets metagraph --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
    if netuid:
        command += f" --netuid {netuid}"
    if reuse_last:
        command += " --reuse-last"
    if html:
        command += " --html"
    return run_btcli_command(command, "Display metagraph")

def pow_register(num_processors=None, update_interval=50000, output_in_place=True, use_cuda=False, dev_id=0, threads_per_block=256):
    """
    Registers a neuron using Proof of Work.
    """
    command = f"btcli subnets pow-register --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT}"
    if num_processors:
        command += f" --processors {num_processors}"
    command += f" --update-interval {update_interval}"
    if not output_in_place:
        command += " --no-output-in-place"
    if use_cuda:
        command += " --use-cuda"
    else:
        command += " --no-use-cuda"
    command += f" --dev-id {dev_id} --threads-per-block {threads_per_block}"
    return run_btcli_command(command, "Proof of Work register")

def register_neuron(prompt=True):
    """
    Registers a neuron by recycling TAO tokens.
    """
    command = f"btcli subnets register --wallet-name {WALLET_NAME} --wallet-path {WALLET_PATH} --hotkey {HOTKEY} --network {NETWORK} --subtensor.chain_endpoint {CHAIN_ENDPOINT} --netuid 1"
    if not prompt:
        command += " --no-prompt"
    return run_interactive_btcli_command(command, "Register neuron")

def test_btcli_subnets_commands():
    create_subnet()
    view_lock_cost()
    list_subnets()
    display_metagraph(netuid=1)
    #pow_register(num_processors=4, use_cuda=False) 
    register_neuron(prompt=False)

if __name__ == "__main__":
    test_btcli_subnets_commands()