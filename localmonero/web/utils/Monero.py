from monero.wallet import Wallet  
from monero.backends.jsonrpc import JSONRPCWallet 
from django.conf import settings

MONERO_RPC_HOST= settings.MONERO_RPC_HOST
MONERO_RPC_PORT= settings.MONERO_RPC_PORT
MONERO_RPC_USER= settings.MONERO_RPC_USER
MONERO_RPC_PASSWORD= settings.MONERO_RPC_PASSWORD

MONERO_RPC_HOST= "143.198.77.250"
MONERO_RPC_PORT= 28082
MONERO_RPC_USER= "admin"
MONERO_RPC_PASSWORD= "admin"


def get_wallet():
    return Wallet(JSONRPCWallet(host=MONERO_RPC_HOST,
                              port=MONERO_RPC_PORT, user=MONERO_RPC_USER,
                              password=MONERO_RPC_PASSWORD))


def create_address():
    return get_wallet().new_address()[0]

def withdraw(from_address, to_address, amount):
    wallet = get_wallet()
    wallet.refresh()
    tx = wallet.transfer([(to_address, amount)], account=from_address)
    return tx.tx_hash

def check_monero_payment(address, amount):
    transactions = get_wallet.transfers(in_=True)
    for tx in transactions:
        if tx.destination == address and tx.amount == amount and tx.confirmations > 0:
            return True
    return False

def check_balance_by_address(address):
    wallet = get_wallet()
    wallet.refresh()
    return wallet.balance(address)