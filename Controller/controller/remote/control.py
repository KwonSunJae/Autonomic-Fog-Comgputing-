import subprocess


def initFog( remote):
    query = 'sshpass -p {} scp {} root@{}:~/'.format(remote.rootpw, "~/Autonomic-Fog-Comgputing-/SelfConfiguring/fog_setup.sh", remote.ip)
    sc = subprocess.run(query, shell= True)
    query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip, ". fog_setup.sh")
    subprocess.run(query, shell= True)

def initEdge( remote ):
    query = 'sshpass -p {} scp {} root@{}:~/'.format(remote.rootpw,"~/Autonomic-Fog-Comgputing-/SelfConfiguring/edge_setup.sh", remote.ip)
    sc = subprocess.run(query, shell= True)
    query = "sshpass -p {} ssh root@{} '{}'".format(remote.rootpw, remote.ip, ". edge_setup.sh")
    subprocess.run(query, shell= True)