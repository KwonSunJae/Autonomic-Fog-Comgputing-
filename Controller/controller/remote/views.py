from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Remote,ModuleField
from .serializers import RemoteSerializer
from .control import initEdge, initFog
from .creater import runDockerfile,runYAMLfile,stopEdgeModule,stopFogModule,healEdgeModule,createDockerfile,createYAMLfile
import json
import subprocess
import time
# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    initEdge(Remote(type=0, ip='117.16.136.172',rootpw= 'dmslab',cloud='0.0.0.0', name='test'))
    return Response("hello world!")

@api_view(['GET'])
def checkAPI(request):
    temp = Remote.objects.all()
    serial = RemoteSerializer(temp, many = True)
    return Response(serial.data)
@api_view(['POST'])
def automodeON(request):
    temp = Remote.objects.all()
    modules = ModuleField.objects.all()
    selectremote= Remote()
    selectfog = Remote()
    selectmodules = []
    data = json.loads(request.body.decode('utf-8'))
    for s in temp:
        if s.ip == data['edgeIp']:
            selectremote = s
            for m in modules:

                if m.remote_id == s:
                    selectmodules.append(m)
        if s.ip == data['fogIp']:
            selectfog = s
    

    runYAMLfile(selectmodules,selectfog)
    for m in selectmodules:
        stopEdgeModule(m,selectremote)
    
    return Response(status=200)
@api_view(['POST'])
def automodeOFF(request):
    temp = Remote.objects.all()
    modules = ModuleField.objects.all()
    selectremote= Remote()
    selectfog = Remote()
    selectmodules = []
    data = json.loads(request.body.decode('utf-8'))
    for s in temp:
        if s.ip == data['edgeIp']:
            selectremote = s
            for m in modules:

                if m.remote_id == s:
                    selectmodules.append(m)
        if s.ip == data['fogIp']:
            selectfog = s
    
    for m in selectmodules:
        stopYAMLfile(m,selectfog)
    for m in selectmodules:
        healEdgeModule(m,selectremote)
    
    return Response(status=200)
@api_view(['POST'])
def edge2fog(request):
    temp = Remote.objects.all()
    modules = ModuleField.objects.all()
    selectremote= Remote()
    selectupper= Remote()
    selectmodule= ModuleField()
    data = json.loads(request.body.decode('utf-8'))
    for s in temp:
        if s.ip == data['edgeIp']:
            selectremote = s
            
        if s.ip == data['fogIp']:
            selectupper = s
    for m in modules:
        if m.name == data['moduleName']:
            selectmodule =m
            break
    runYAMLfile([selectmodule],selectupper)
    time.sleep(5)
    healEdgeModule(selectmodule,selectremote)
    return Response(status=200)

@api_view(['POST'])
def fog2edge(request):
    temp = Remote.objects.all()
    modules = ModuleField.objects.all()
    selectremote= Remote()
    selectupper= Remote()
    selectmodule= ModuleField()
    data = json.loads(request.body.decode('utf-8'))
    for s in temp:
        if s.ip == data['edgeIp']:
            selectremote = s
            
        if s.ip == data['fogIp']:
            selectupper = s
    for m in modules:
        if m.name == data['moduleName']:
            selectmodule =m
            break
    stopFogModule(selectmodule,selectupper)
    return Response(status=200)


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
    modules =[]
    for i in data['modules']:
        modules.append(ModuleField(name= i['name'],remote_id=remote,giturl=i['giturl'],execute= i['execute'], install=['install'], env=i['env'],priority=i['priority']))
    if remote.type == 0:
        initFog(remote)
        createDockerfile(modules,remote)
        createYAMLfile(modules,remote)
        runYAMLfile(modules,remote)
    else:
        initEdge(remote)
        createDockerfile(modules,remote)
        createYAMLfile(modules,remote)
        runDockerfile(modules, remote)

    return Response(status=200)
