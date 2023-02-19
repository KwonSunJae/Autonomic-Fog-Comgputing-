import subprocess


def initFog( remote):
    query = 'sshpass -p {} scp {} root@{}:~/'.format(remote.rootpw, "~/Autonomic-Fog-Comgputing-/SelfConfiguring/fog_setup.sh", remote.ip)
    print(sc = subprocess.check_call(query))

def initEdge( remote ):
    query = 'sshpass -p {} scp {} root@{}:~/'.format(remote.rootpw,"~/Autonomic-Fog-Comgputing-/SelfConfiguring/edge_setup.sh", remote.ip)
    print(sc = subprocess.check_call(query))