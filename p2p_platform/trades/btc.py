from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import os 
# Configuration for connecting to the Bitcoin RPC server
rpc_user = os.getenv('BTC_RPC_USER')
rpc_password = os.getenv('BTC_RPC_PASSWORD')
rpc_port = os.getenv('BTC_RPC_PORT', 8332)
rpc_host = os.getenv('BTC_RPC_HOST', 'localhost')

# Create a connection to the Bitcoin RPC server
rpc_url = f'http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}'
rpc_connection = AuthServiceProxy(rpc_url)

def get_blockchain_info():
    try:
        blockchain_info = rpc_connection.getblockchaininfo()
        return blockchain_info
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def get_balance():
    try:
        balance = rpc_connection.getbalance()
        return balance
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def send_to_address(address, amount):
    try:
        txid = rpc_connection.sendtoaddress(address, amount)
        return txid
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def get_new_address():
    try:
        address = rpc_connection.getnewaddress()
        return address
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None

def get_transaction(txid):
    try:
        transaction = rpc_connection.gettransaction(txid)
        return transaction
    except JSONRPCException as e:
        print(f"An error occurred: {e}")
        return None
    

def check_btc_payment(address, amount):
    transactions = rpc_connection.listtransactions("*", 1000)
    for tx in transactions:
        if tx['address'] == address and tx['amount'] == amount and tx['confirmations'] > 0:
            return True
    return False