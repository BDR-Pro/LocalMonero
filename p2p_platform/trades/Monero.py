from monero.wallet import Wallet  # type: ignore
from monero.backends.jsonrpc import JSONRPCWallet # type: ignore
from django.conf import settings

MONERO_RPC_HOST= settings.MONERO_RPC_HOST
MONERO_RPC_PORT= settings.MONERO_RPC_PORT
MONERO_RPC_USER= settings.MONERO_RPC_USER
MONERO_RPC_PASSWORD= settings.MONERO_RPC_PASSWORD

def get_wallet():
    return Wallet(JSONRPCWallet(host=MONERO_RPC_HOST,
                              port=MONERO_RPC_PORT, user=MONERO_RPC_USER,
                              password=MONERO_RPC_PASSWORD))


def create_address():
    return get_wallet().addresses()[0]

def withdraw(from_address, to_address, amount):
    wallet = get_wallet()
    wallet.refresh()
    tx = wallet.transfer([(to_address, amount)], account=from_address)
    return tx.tx_hash
