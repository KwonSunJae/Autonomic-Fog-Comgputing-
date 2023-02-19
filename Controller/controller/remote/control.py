import subprocess


def initFog( remote):
    query = 'sshpass -p {} scp {} dmslab-sj@{}:~/'.format(remote.rootpw, "~/Autonomic-Fog-Comgputing-/SelfConfiguring/fog_setup.sh", remote.ip)
    sc = subprocess.run(query)

def initEdge( remote ):
    query = 'sshpass -p {} scp {} dmslab-sj@{}:~/'.format(remote.rootpw,"~/Autonomic-Fog-Comgputing-/SelfConfiguring/edge_setup.sh", remote.ip)
    sc = subprocess.run(query)