from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from .models import Pass, PassManager

@csrf_exempt
def submit_data(request):
    if request.method == 'POST':
        try:
            data = request.json
            pass = PassManager().create_pass(
                data['coordinates'],
                data['elevation'],
                data['name'],
                data['photos'],
                data['user_name'],
                data['user_email'],
                data['user_phone']
            )
            return HttpResponse(status=201)
        except IntegrityError:
            return HttpResponse(status=400)
    return HttpResponse(status=405)

@csrf_exempt
def get_data(request, id):
    if request.method == 'GET':
        try:
            pass = Pass.objects.get(id=id)
            return HttpResponse(status=200, content=pass)
        except Pass.DoesNotExist:
            return HttpResponse(status=404)
    return HttpResponse(status=405)

@csrf_exempt
def update_data(request, id):
    if request.method == 'PATCH':
        try:
            pass = Pass.objects.get(id=id)
            if pass.status == 'new':
                data = request.json
                pass.coordinates = data['coordinates']
                pass.elevation = data['elevation']
                pass.name = data['name']
                pass.photos = data['photos']
                pass.save()
                return HttpResponse(status=200, content={'state': 1, 'message': 'Successfully updated'})
            else:
                return HttpResponse(status=403, content={'state': 0, 'message': 'Cannot update data'})
        except Pass.DoesNotExist:
            return HttpResponse(status=404)
        except ValidationError as e:
            return HttpResponse(status=400, content={'state': 0, 'message': str(e)})
    return HttpResponse(status=405)

@csrf_exempt
def get_data_by_user(request):
    if request.method == 'GET':
        email = request.GET.get('user__email')
        if email:
            passes = Pass.objects.filter(user_email=email)
            return HttpResponse(status=200, content=passes)
        else:
            return HttpResponse(status=400)
    return HttpResponse(status=405)
