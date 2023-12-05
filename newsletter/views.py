from django.shortcuts import render
from django.http import JsonResponse
import json

from .models import Subscriber

# Create your views here.

def subscribe(request):
    response = {}
    data = json.loads(request.body)
    try:
        subscriber_exists = Subscriber.objects.filter(email=data['email']).exists()
        if(not subscriber_exists):
            Subscriber.objects.create(email=data['email'])
            response['exists'] = False
        else:
            response['exists'] = True
    except Exception as e:
        response['error'] = f"Some error occured in the server {str(e)}"
        response['success'] = False
    else:
        response['success'] = True
    return JsonResponse(response, safe=False)
