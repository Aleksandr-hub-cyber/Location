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
