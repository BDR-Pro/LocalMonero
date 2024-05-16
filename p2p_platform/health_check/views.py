from django.http import JsonResponse
from django.conf import settings
from monero.daemon import Daemon

MONERO_RPC_HOST= settings.MONERO_RPC_HOST
MONERO_RPC_PORT= settings.MONERO_RPC_PORT
MONERO_RPC_USER= settings.MONERO_RPC_USER
MONERO_RPC_PASSWORD= settings.MONERO_RPC_PASSWORD


def health_check(request):
    return JsonResponse({'status': 'UP'})

def isMoneroUp(request):
    #ping rpc server
    try:
        daemon = Daemon(
            host=MONERO_RPC_HOST,
            port=MONERO_RPC_PORT,
            user=MONERO_RPC_USER,
            password=MONERO_RPC_PASSWORD
        )
        info = daemon.info()
        return JsonResponse(info)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=503)