from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import Pass, PassManager
import json

@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pass_obj = PassManager().create_pass(
                data['coordinates'],
                data['elevation'],
                data['name'],
                data['photos'],
                data['user_name'],
                data['user_email'],
                data['user_phone']
            )
            return JsonResponse({'state': 1, 'message': 'Success'})
        except IntegrityError:
            return JsonResponse({'state': 0, 'message': 'Integrity error'})
        except KeyError:
            return JsonResponse({'state': 0, 'message': 'Missing fields'})
    return HttpResponse(status=405)

def get_data(request, id):
    if request.method == 'GET':
        try:
            pass_obj = Pass.objects.get(id=id)
            data = {
                'id': pass_obj.id,
                'coordinates': pass_obj.coordinates,
                'elevation': pass_obj.elevation,
                'name': pass_obj.name,
                'photos': pass_obj.photos,
                'user_name': pass_obj.user_name,
                'user_email': pass_obj.user_email,
                'user_phone': pass_obj.user_phone,
                'status': pass_obj.status
            }
            return JsonResponse(data)
        except Pass.DoesNotExist:
            return JsonResponse({'state': 0, 'message': 'Not found'})
    return HttpResponse(status=405)

@csrf_exempt
def update_data(request, id):
    if request.method == 'PATCH':
        try:
            pass_obj = Pass.objects.get(id=id)
            if pass_obj.status != 'new':
                return JsonResponse({'state': 0, 'message': 'Cannot edit non-new pass'})
            data = json.loads(request.body)
            pass_obj.coordinates = data.get('coordinates', pass_obj.coordinates)
            pass_obj.elevation = data.get('elevation', pass_obj.elevation)
            pass_obj.name = data.get('name', pass_obj.name)
            pass_obj.photos = data.get('photos', pass_obj.photos)
            # Не редактировать user поля
            pass_obj.save()
            return JsonResponse({'state': 1, 'message': 'Updated'})
        except Pass.DoesNotExist:
            return JsonResponse({'state': 0, 'message': 'Not found'})
    return HttpResponse(status=405)

def get_data_by_user(request):
    if request.method == 'GET':
        email = request.GET.get('user__email')
        if not email:
            return JsonResponse({'state': 0, 'message': 'Email required'})
        passes = Pass.objects.filter(user_email=email)
        data = []
        for p in passes:
            data.append({
                'id': p.id,
                'coordinates': p.coordinates,
                'elevation': p.elevation,
                'name': p.name,
                'photos': p.photos,
                'user_name': p.user_name,
                'user_email': p.user_email,
                'user_phone': p.user_phone,
                'status': p.status
            })
        return JsonResponse(data, safe=False)
    return HttpResponse(status=405)
