import subprocess


def createDockerfile(modules,remote):
    for module in modules:
        subprocess.run("mkdir "+ module.name, shell= True)
        end = '\n'
        f = open( "./"+module.name+"/Dockerfile",mode='w' )
        f.write("FROM ubuntu:20.04\n")
        f.write("RUN apt-get update -y && apt-get upgrade -y\n")
        f.write("RUN apt-get install -y git\n")
        f.write("RUN git clone " + module.giturl +end)
        runs = 'RUN '
        print(module.install)
        mrrs = module.install.split("\n")
        
        for s in mrrs:
            f.write(runs+ s+end)
        mers = module.execute
        f.write("CMD "+ mers + end)
        f.close()
        query = 'docker build -t ksun4131/' + str(module.remote_id.id) + module.name  + " ./" + module.name +"/"
        subprocess.run(query, shell= True)
        query = "docker push ksun4131/{}".format(str(module.remote_id.id) +module.name)
        subprocess.run(query, shell= True)
def createYAMLfile(modules,remote):
    for module in modules:
        temp = str(module.remote_id.id) + module.name
        subprocess.run("mkdir "+ temp,shell=True)
        end = '\n'
        
        scripts = '''apiVersion: apps/v1
kind: Deployment
metadata:
  name: {}
  labels:
    app: {}
spec:
  selector:
    matchLabels:
      app: {}
  template:
    metadata:
      labels:
        app: {}
    spec:
      containers:
      - name: {}
        image: docker.io/ksun4131/{}'''.format(temp,temp,temp,temp,temp,temp)
        f = open( "./"+temp+"/deployment.yaml",mode ='w' )
        f.write(scripts)
        f.close()
        query = 'sshpass -p {} scp -r {} root@{}:~/'.format(remote.rootpw,"~/Autonomic-Fog-Comgputing-/Controller/controller/"+ temp, remote.ip)
        subprocess.run(query, shell= True)
        subprocess.run('cd .. ',shell= True)

def runDockerfile(modules, remote):
    for module in modules:
        query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  "docker run -d --name {} ksun4131/{}".format(module.name, str(module.remote_id.id) +module.name ))
        subprocess.run(query, shell= True)

def runYAMLfile(modules, remote):
    for module in modules:
        query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  'kubectl apply -f ~/{} '.format(str(module.remote_id.id)+module.name ))
        subprocess.run(query, shell= True)
    
def stopFogModule ( module, remote):
    query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  'kubectl delete deployment {}'.format(str(module.remote_id.id)+module.name ))
    subprocess.run(query, shell= True)

def stopEdgeModule ( module, remote):
    query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  'docker stop {}'.format(module.name))
    subprocess.run(query, shell= True)

def healEdgeModule ( module, remote):
    query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  'docker restart {}'.format(module.name ))
    subprocess.run(query, shell= True)