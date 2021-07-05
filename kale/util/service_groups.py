from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "kale_harvester kale_timelord_launcher kale_timelord kale_farmer kale_full_node kale_wallet".split(),
    "node": "kale_full_node".split(),
    "harvester": "kale_harvester".split(),
    "farmer": "kale_harvester kale_farmer kale_full_node kale_wallet".split(),
    "farmer-no-wallet": "kale_harvester kale_farmer kale_full_node".split(),
    "farmer-only": "kale_farmer".split(),
    "timelord": "kale_timelord_launcher kale_timelord kale_full_node".split(),
    "timelord-only": "kale_timelord".split(),
    "timelord-launcher-only": "kale_timelord_launcher".split(),
    "wallet": "kale_wallet kale_full_node".split(),
    "wallet-only": "kale_wallet".split(),
    "introducer": "kale_introducer".split(),
    "simulator": "kale_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
