from src import favorites
from moccasin.boa_tools import VyperContract
from moccasin.config import get_active_network

def deploy_favorites() -> VyperContract:

    active_network = get_active_network()
    favorites_contract = favorites.at("0xE2CE98701bc87eF75F52039E4a048f26C570D97B")
    if active_network.has_explorer():
        result = active_network.moccasin_verify(favorites_contract)
        result.wait_for_verification()
    return favorites_contract

def moccasin_main() -> VyperContract:
    deploy_favorites()