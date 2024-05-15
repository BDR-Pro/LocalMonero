from monero.wallet import Wallet  # type: ignore
from monero.backends.jsonrpc import JSONRPCWallet # type: ignore
from django.conf import settings

MONERO_RPC_HOST= settings.MONERO_RPC_HOST
MONERO_RPC_PORT= settings.MONERO_RPC_PORT
MONERO_RPC_USER= settings.MONERO_RPC_USER
MONERO_RPC_PASSWORD= settings.MONERO_RPC_PASSWORD

def get_website_address():
    return Wallet(JSONRPCWallet(host=MONERO_RPC_HOST,
                              port=MONERO_RPC_PORT, user=MONERO_RPC_USER,
                              password=MONERO_RPC_PASSWORD))

def create_address():
    return get_website_address().create_address().address

"""def withdraw(address, amount):
    tx = wallet.transfer([(address, amount)])
    return tx.tx_hash"""