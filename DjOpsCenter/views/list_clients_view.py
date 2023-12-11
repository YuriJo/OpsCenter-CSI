from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from DjOpsCenter.models import Clients

@login_required
def list_clients_view(request):
    if request.method == 'POST':
        clients = Clients.objects.all().order_by('name')
        clients_list = [client.name for client in clients]
        return JsonResponse({'clients': clients_list})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
