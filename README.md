# `btcli-test` Repository

## Overview

The `btcli-test` repository contains a suite of tests for the Bittensor `btcli` command-line interface. These tests aim to ensure the correctness and functionality of various `btcli` commands used for managing wallets and performing operations on the Bittensor network.


# Bittensor `config` Commands
- **`config set`**: Sets values in the configuration file.
  - **`--wallet-name`, `--name`, `--wallet_name`**: Sets the wallet name.
  - **`--wallet-path`, `--wallet_path`, `--path`, `-p`**: Sets the wallet path.
  - **`--wallet-hotkey`, `--hotkey`, `--wallet_hotkey`, `-k`**: Sets the wallet hotkey.
  - **`--network`, `--subtensor.network`, `-n`**: Sets the network.
  - **`--chain`, `--subtensor.chain_endpoint`, `-c`**: Sets the chain endpoint.
  - **`--no-cache`**: Disables caching of certain commands.
  - **`--help`**: Show this message and exit.

- **`config get`**: Prints the current configuration file in a table.
  - **`--help`**: Show this message and exit.

- **`config clear`**: Clears items from the configuration file.
  - **`--wallet-name`**: Clears the wallet name.
  - **`--wallet-path`**: Clears the wallet path.
  - **`--wallet-hotkey`**: Clears the wallet hotkey.
  - **`--network`**: Clears the network setting.
  - **`--chain`**: Clears the chain endpoint.
  - **`--no-cache`**: Clears the cache setting.
  - **`--all`**: Clears all configuration settings.
  - **`--help`**: Show this message and exit.

- **`config metagraph`**: Updates the configuration for metagraph columns.
  - **`--reset`**: Restores the configuration for metagraph columns to its default setting (all enabled).
  - **`--help`**: Show this message and exit.

# Bittensor `wallet` Commands
- **`wallet balance`**: Check the balance of the wallet on the Bittensor network. This provides a detailed view of the wallet's coldkey balances, including free and staked balances.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None]
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None]
  - **`--all`, `-a`**: Whether to display the balances for all wallets.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--help`**: Show this message and exit.

- **`wallet history`**: Fetch the latest transfers of the provided wallet on the Bittensor network. This provides a detailed view of the transfers carried out on the wallet.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None]
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None]
  - **`--help`**: Show this message and exit.

- **`wallet inspect`**: Detailed report of a user's wallet pairs (coldkey, hotkey) on the Bittensor network.
  - **`--all`, `--all-wallets`, `-a`**: Inspect all wallets within the specified path.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None]
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None]
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--netuids`, `-n`**: NetUIDs to filter by (e.g., `0 1 2`).
  - **`--help`**: Show this message and exit.

- **`wallet overview`**: Presents a detailed overview of the user's registered accounts on the Bittensor network.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None]
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None]
  - **`--all`, `-a`**: View overview for all wallets.
  - **`--sort-by`**: Sort the hotkeys by the specified column title (e.g., name, uid, axon). [default: None]
  - **`--sort-order`**: Sort the hotkeys in the specified ordering (ascending/asc or descending/desc/reverse). [default: None]
  - **`--netuids`, `-n`**: Set the NetUIDs to filter by (e.g., `0 1 2`).
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--help`**: Show this message and exit.

- **`wallet check-swap`**: Check the scheduled swap status of a coldkey.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None]
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None]
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--help`**: Show this message and exit.

- **`wallet regen-coldkey`**: Regenerates a coldkey for a wallet on the Bittensor network.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None]
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root

# Bittensor `root` Commands
- **`root list`**: Display the members of the root network (Netuid = 0) on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--help`**: Show this message and exit.

- **`root register`**: Register a neuron on the Bittensor network by recycling some TAO (the network's native token).
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--help`**: Show this message and exit.

- **`root boost`**: Not currently working with new implementation.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--amount`, `--increase`, `-a`**: Amount (float) to boost, e.g., 0.01 [default: None].
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--help`**: Show this message and exit.

- **`root get-weights`**: Retrieve the weights set for the root network on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--limit-min-col`, `--min`**: Limit left display of the table to this column. [default: None].
  - **`--limit-max-col`, `--max`**: Limit right display of the table to this column. [default: None].
  - **`--reuse-last`**: Reuse the metagraph data you last retrieved. Only use this if you have already retrieved metagraph data.
  - **`--html`**: Display the table as HTML in the browser, rather than in the Terminal.
  - **`--help`**: Show this message and exit.

- **`root set-weights`**: Set the weights for the root network on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--netuid`**: Netuids, e.g., `-n 0 -n 1 -n 2` ... [default: None].
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--help`**: Show this message and exit.

- **`root slash`**: Decrease the weights for a specific subnet within the root network on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--help`**: Show this message and exit.

- **`root delegate-stake`**: Stakes TAO to a specified delegate on the Bittensor network.
  - **`--delegate-ss58key`**: The `SS58` address of the delegate to stake to. [default: None].
  - **`--amount`**: The amount of TAO to stake. Do not specify if using `--all` [default: None].
  - **`--all`, `-a`**: If specified, the command stakes all available TAO. Do not specify if using `--amount`.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--help`**: Show this message and exit.

- **`root list-delegates`**: Displays a table of Bittensor network delegates, providing a comprehensive overview of delegate statistics and information.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--help`**: Show this message and exit.

- **`root set-take`**: Views active proposals for the senate.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey of wallet [default: None].
  - **`--take`**: The new take value. [default: None].
  - **`--help`**: Show this message and exit.

- **`root undelegate-stake`**: Allows users to withdraw their staked TAO from a delegate on the Bittensor network.
  - **`--delegate-ss58key`**: The `SS58` address of the delegate to unstake from. [default: None].
  - **`--amount`**: The amount of TAO to unstake. Do not specify if using `--all` [default: None].
  - **`--all`, `-a`**: If specified, the command unstake all available TAO. Do not specify if using `--amount`.
  - **`--wallet-name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets


# Bittensor `sudo` Commands
- **`sudo set`**: Sets hyperparameters for a subnet.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--param`, `--parameter`**: The subnet hyperparameter to set.
  - **`--value`**: The subnet hyperparameter value to set.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`sudo get`**: Retrieves hyperparameters of a subnet.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

# Bittensor `subnets` Commands
- **`subnets create`**: Registers a new subnetwork.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`subnets lock-cost`**: Views the cost for creating a new subnetwork.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`subnets list`**: Lists all subnets and their information.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--reuse-last`**: Reuse the metagraph data you last retrieved. Only use this if you have already retrieved metagraph data.
  - **`--html`**: Display the table as HTML in the browser, rather than in the Terminal.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`subnets metagraph`**: Displays the metagraph of a subnetwork.
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1. This is ignored when used with `--reuse-last`. [default: None].
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--reuse-last`**: Reuse the metagraph data you last retrieved. Only use this if you have already retrieved metagraph data.
  - **`--html`**: Display the table as HTML in the browser, rather than in the Terminal.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`subnets pow-register`**: Registers a neuron using Proof of Work.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--processors`, `-p`**: Number of processors to use for POW registration [default: None].
  - **`--update-interval`, `-u`**: The number of nonces to process before checking for the next block during registration [default: 50000].
  - **`--output-in-place`, `--no-output-in-place`**: Whether to output the registration statistics in-place [default: output-in-place].
  - **`--verbose`**: Whether to output the registration statistics verbosely.
  - **`--use-cuda`, `--cuda`, `--no-use-cuda`, `--no-cuda`**: Set flag to use CUDA to pow_register [default: no-use-cuda].
  - **`--dev-id`, `-d`**: Set the CUDA device id(s). Goes by the order of speed (i.e., 0 is the fastest) [default: 0].
  - **`--threads-per-block`, `-tbp`**: Set the number of Threads Per Block for CUDA [default: 256].
  - **`--help`**: Show this message and exit.

- **`subnets register`**: Registers a neuron by recycling TAO tokens.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--prompt`, `--no-prompt`**: Enable or disable interactive prompts. [default: prompt].
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

# Bittensor `weights` Commands

- **`weights commit`**: Commit weights for a specific subnet on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--uids`, `-u`**: Corresponding UIDs for the specified netuid, e.g., `-u 1 -u 2 -u 3 ...`.
  - **`--weights`, `-w`**: Corresponding weights for the specified UIDs, e.g., `-w 0.2 -w 0.4 -w 0.1 ...`.
  - **`--salt`, `-s`**: Corresponding salt for the hash function, e.g., `-s 163 -s 241 -s 217 ...`.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.

- **`weights reveal`**: Reveal weights for a specific subnet on the Bittensor network.
  - **`--network`, `--subtensor.network`**: The subtensor network to connect to. Default: finney.
  - **`--chain`, `--subtensor.chain_endpoint`**: The subtensor chain endpoint to connect to.
  - **`--wallet-name`, `--wallet_name`, `-w`**: Name of wallet [default: None].
  - **`--wallet-path`, `--wallet_path`, `-p`**: Filepath of root of wallets [default: None].
  - **`--hotkey`, `--wallet_hotkey`, `-H`**: Hotkey name of wallet [default: None].
  - **`--netuid`**: The netuid (network unique identifier) of the subnet within the root network, e.g., 1 [default: None].
  - **`--uids`, `-u`**: Corresponding UIDs for the specified netuid, e.g., `-u 1 -u 2 -u 3 ...`.
  - **`--weights`, `-w`**: Corresponding weights for the specified UIDs, e.g., `-w 0.2 -w 0.4 -w 0.1 ...`.
  - **`--salt`, `-s`**: Corresponding salt for the hash function, e.g., `-s 163 -s 241 -s 217 ...`.
  - **`--quiet`**: Do not output to the console besides critical information.
  - **`--verbose`**: Enable verbose output.
  - **`--help`**: Show this message and exit.


## Setup

### Prerequisites
- Ensure that `btcli` is installed and accessible from your command line.
```
https://github.com/opentensor/btcli.git
```
- Configure the `btcli` tool with the appropriate network and chain endpoints.
```
https://github.com/opentensor/subtensor.git
```

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/btcli-test.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd btcli-test
    ```

## Running Tests

To run the tests, simply execute the script:
```bash
pytest -s -v test_wallet.py
