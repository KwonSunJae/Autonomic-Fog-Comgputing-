from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Remote
from .serializers import RemoteSerializer
from .control import initEdge
import json

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    initEdge(Remote(type=0, ip='117.16.136.172',rootpw= 'dmslab',cloud='0.0.0.0', name='test'))
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
