from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import User
# Create your views here.
def ajax_request(request):
    print(request.GET['name'])


    name = request.GET['name']
    query = { 'name': name }
    
    
    #data = serialize('json', query)


    return JsonResponse(query, safe=False)

def index(request):
    return render(request, 'base.html')
