import subprocess


def createDockerfile(modules,remote):
    for module in modules:
        subprocess.run("mkdir "+ module.name, shell= True)
        end = '\n'
        f = open( "./"+module.name+"/Dockerfile",mode='w' )
        f.write("FROM ubuntu: 20.04\n")
        f.write("RUN apt-get update -y && apt-get upgrade -y\n")
        f.write("RUN apt-get install nginx git\n")
        f.write("RUN git clone " + module.giturl +end)
        runs = 'RUN'
        mrrs = module.install.split("\n")
        for s in mrrs:
            f.write(runs+ s+end)
        mers = module.execute
        f.write("CMD "+ mers + end)
        f.write("EXPOSE 80")
        f.close()
        query = 'docker built -t ksun4131/' + str(remote.id) + module.name  + " . && cd .."
        subprocess.run(query, shell= True)
        query = "docker pull ksun4131/{}".format(str(remote.id) +module.name)
        subprocess.run(query, shell= True)
def createYAMLfile(modules,remote):
    for module in modules:
        subprocess.run("mkdir "+ module.name)
        end = '\n'
        temp = str(remote.id) + module.name
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
        image: ksun4131/{}
        ports:
        - containerPort: 80'''.format(temp,temp,temp,temp,temp,temp)
        f = open( "./"+module.name+"/deployment.yaml",mode                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ,,,mmmmmmkllllllj                 ='w' )
        f.write(scripts)
        f.close()
        query = 'sshpass -p {} scp -r {} root@{}:~/'.format(remote.rootpw,"~/Autonomic-Fog-Comgputing-/Controller/controller/remote/"+ temp, remote.ip)
        subprocess.run(query, shell= True)

def runDockerfile(modules, remote):
    for module in modules:
        query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip,  "docker run -d --name {} -p {}:80 ksun4131/{}".format(module.name, 80 + module.priority, str(remote.id) + "/"+module.name ))
        subprocess.run(query, shell= True)
    
