from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Remote
from .serializers import RemoteSerializer
import json

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def checkAPI(request,id):
    temp = Remote.objects.all()
    serial = RemoteSerializer(temp, many = True)
    return Response(serial.data)

@api_view(['POST'])
def registerMachine(request):

    data = json.loads(request.body.decode('utf-8'))
    remote = Remote()
    remote.type = data['type'] 
    remote.name = data['name']
    remote.ip = data['ip']
    remote.cloud = data['cloud']
    remote.rootpw = data['rootpw']
    remote.save()

    
    return Response(status=200)
