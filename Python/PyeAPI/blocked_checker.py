import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4']

pyeapi.load_config('eapi.conf')


for switch in switches:
    connect = pyeapi.connect_to(switch)
    cmd = connect.enable('show spanning-tree')
    for instance in cmd[0]['result']['spanningTreeInstances']:
        for interface in cmd[0]['result']['spanningTreeInstances'][instance]['interfaces']:
            if cmd[0]['result']['spanningTreeInstances'][instance]['interfaces'][interface]['state'] == 'discarding':
                print(f"On switch {switch} interface {interface} is blocked by STP on instance {instance}")
