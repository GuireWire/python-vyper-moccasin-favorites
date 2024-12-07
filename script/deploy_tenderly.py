from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites_tenderly() -> VyperContract:
    active_network = get_active_network()

    # Ensure correct network settings
    if getattr(active_network, "name", "") == "sepolia-tenderly":
        print("Using Tenderly network settings...")
        active_network.gas_limit = None  # Let Tenderly manage gas
        active_network.gas_price = None  # Let Tenderly manage gas

    # Debug: Print network configuration
    print(f"Active network config: {active_network}")

    # Deploy the contract with debug logging
    print("Deploying Favorites contract...")
    try:
        favorites_contract: VyperContract = favorites.deploy()
        print(f"Deployed contract at: {favorites_contract.address}")
    except Exception as e:
        print("Error during deployment:", e)
        raise

    # Verify deployment
    starting_number: int = favorites_contract.retrieve()
    print(f"The starting number is {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"The ending number is {ending_number}")

    if active_network.has_explorer():
        print("Verifying contract...")
        active_network.moccasin_verify(favorites_contract)

    return favorites_contract

def moccasin_main() -> VyperContract:
    deploy_favorites_tenderly()
