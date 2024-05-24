from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from django.conf import settings

# Configuration for connecting to the Bitcoin RPC server
import os
"""path: localmonero/web/utils/btc.py

function: get_blockchain_info
function: get_balance
function: send_to_address
function: get_new_address
function: get_transaction
function: check_btc_payment
function: check_balance_by_address
function: get_blockchain_info
function: get_balance << of all addresses
"""

BTC_RPC_HOST= settings.BTC_RPC_HOST
BTC_RPC_PORT= settings.BTC_RPC_PORT
BTC_RPC_USER= settings.BTC_RPC_USER
BTC_RPC_PASSWORD= settings.BTC_RPC_PASSWORD


rpc_user = "admin"
rpc_password = "admin"
rpc_port = 18332
rpc_host = "143.198.77.250"

# Create a connection to the Bitcoin RPC server
rpc_url = f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}'
rpc_connection = AuthServiceProxy(rpc_url)

def get_blockchain_info():
    """
    Retrieves blockchain information from the Bitcoin RPC server.
    
    Returns:
        dict: Blockchain information if successful, None otherwise.
    """
    try:
        blockchain_info = rpc_connection.getblockchaininfo()
        return blockchain_info
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def get_balance():
    """
    Retrieves the balance of the wallet from the Bitcoin RPC server.
    
    Returns:
        float: Wallet balance if successful, None otherwise.
    """
    try:
        balance = rpc_connection.getbalance()
        return balance
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None
    
def send_to_address(from_add, to, amount):
    """
    Sends Bitcoin from one address to another.
    
    Args:
        from_add (str): The address to send Bitcoin from.
        to (str): The address to send Bitcoin to.
        amount (float): The amount of Bitcoin to send.
    
    Returns:
        str: The transaction ID if successful, None otherwise.
    """
    try:
        txid = rpc_connection.sendfrom(from_add, to, amount)
        return txid
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None


def get_new_address():
    """
    Generates a new Bitcoin address.
    
    Returns:
        str: New Bitcoin address if successful, None otherwise.
    """
    try:
        address = rpc_connection.getnewaddress()
        return address
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def get_transaction(txid):
    """
    Retrieves information about a specific transaction.
    
    Args:
        txid (str): The transaction ID.
    
    Returns:
        dict: Transaction information if successful, None otherwise.
    """
    try:
        transaction = rpc_connection.gettransaction(txid)
        return transaction
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def check_btc_payment(address, amount):
    """
    Checks if a specific amount has been received at a given address.
    
    Args:
        address (str): The Bitcoin address to check.
        amount (float): The amount to check for.
    
    Returns:
        bool: True if the payment is found and confirmed, False otherwise.
    """
    try:
        transactions = rpc_connection.listtransactions("*", 1000)
        for tx in transactions:
            if tx['address'] == address and tx['amount'] == amount and tx['confirmations'] > 0:
                return True
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
    return False


def check_balance_by_address(address):
    """
    Check the balance of a Bitcoin address.
    
    Args:
        address (str): The Bitcoin address to check.
    
    Returns:
        float: The balance of the address if successful, None otherwise.
    """
    try:
        balance = rpc_connection.getreceivedbyaddress(address)
        return balance
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None