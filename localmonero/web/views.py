from django.http import JsonResponse
from django.conf import settings


from web.utils.Monero import get_wallet
from web.utils.btc import get_blockchain_info, get_balance, send_to_address, get_new_address,check_balance_by_address

MONERO_RPC_HOST= settings.MONERO_RPC_HOST
MONERO_RPC_PORT= settings.MONERO_RPC_PORT
MONERO_RPC_USER= settings.MONERO_RPC_USER
MONERO_RPC_PASSWORD= settings.MONERO_RPC_PASSWORD



def health_check(request):
    """check if the server is up

    Args:
        request 

    Returns:
        JsonResponse: status of the server
    """
    return JsonResponse({'status': 'UP'})

def isMoneroUp(request):
    #ping rpc server
    """check if the monero server is up

    Args:
        request 

    Returns:
        JsonResponse: status of the monero server
    """
    try:
        get_wallet()
        return JsonResponse({'status': 'UP'})
    except Exception as e:
        return JsonResponse({'status': 'DOWN', 'error': str(e)})
    
def isBitcoinUp(request):
    #ping rpc server
    """check if the bitcoin server is up

    Args:
        request 

    Returns:
        JsonResponse: status of the bitcoin server
    """
    try:
        info=get_blockchain_info()
        if info is not None:
            return JsonResponse({'status': 'UP',
                'blockchain_info': info})
        else:
            return JsonResponse({'status': 'DOWN'})
    except Exception as e:
        return JsonResponse({'status': 'DOWN', 'error': str(e)})
    
def getBalance(request):
    #get balance from rpc server
    """get the balance of the bitcoin wallet

    Args:
        request 

    Returns:
        JsonResponse: balance of the bitcoin wallet
    """
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    balance = get_balance()
    
    if balance is not None:
        return JsonResponse({'balance': balance})
    else:
        return JsonResponse({'error': balance}, status=500)
    
def createWalletBTC(request):
    #create wallet
    """create a new bitcoin wallet

    Args:
        request 

    Returns:
        JsonResponse: new bitcoin wallet address
    """
    address = get_new_address()
    if address is not None:
        return JsonResponse({'address': address})
    else:
        return JsonResponse({'error': address}, status=500)

def sendBTC(request):
    #send btc
    """send bitcoin to a given address

    Args:
        request 

    Returns:
        JsonResponse: transaction id
    """
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    address = request.GET.get('address')
    amount = request.GET.get('amount')
    user_address = request.user.profile.btc_address
    txid = send_to_address(user_address, address, amount)
    if txid is not None:
        return JsonResponse({'txid': txid})
    else:
        return JsonResponse({'error': txid}, status=500)
    
def checkBalanceByAddressBTC(request):
    #check balance by address
    """check the balance of the bitcoin wallet by address

    Args:
        request 

    Returns:
        JsonResponse: balance of the bitcoin wallet
    """
    if not request.user.is_superuser:
        return JsonResponse({'error': 'Unauthorized'}, status=401)
    
    address = request.GET.get('address')
    balance = check_balance_by_address(address)
    if balance is not None:
        return JsonResponse({'balance': balance})
    else:
        return JsonResponse({'error': balance}, status=500)
    
  
