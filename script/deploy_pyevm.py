from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites_to_pyevm() -> VyperContract:
    """
    Deploy the Favorites contract to the pyevm network and perform basic operations.
    """
    print("Deploying Favorites contract to the pyevm network...")

    # Deploy the contract
    favorites_contract: VyperContract = favorites.deploy()

    # Interact with the deployed contract
    starting_number: int = favorites_contract.retrieve()
    print(f"The starting number is {starting_number}")

    favorites_contract.store(77)
    ending_number: int = favorites_contract.retrieve()
    print(f"The ending number is {ending_number}")

    # Verify the contract on the network, if applicable
    active_network = get_active_network()
    if active_network.has_explorer():
        print("Verifying the contract...")
        result = active_network.moccasin_verify(favorites_contract)
        print(f"Verification result: {result}")

    print("Deployment to pyevm completed successfully.")
    return favorites_contract

def moccasin_main() -> VyperContract:
    """
    Entry point for the Moccasin deployment script.
    """
    return deploy_favorites_to_pyevm()
