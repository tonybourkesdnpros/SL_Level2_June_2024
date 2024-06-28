import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4', 'spine1', 'spine2', 'spine3', 'spine4']

pyeapi.load_config('eapi.conf')

i = 1
# print(cmd)
for switch in switches:
    i = 1
    connect = pyeapi.connect_to(switch)
    cmd = connect.enable('show isis neighbors')
    for vrf in cmd[0]['result']['vrfs']:
        for instance in cmd[0]['result']['vrfs'][vrf]['isisInstances']:
            for neighbor in cmd[0]['result']['vrfs'][vrf]['isisInstances'][instance]['neighbors']:
                i = i + 1
    print(f"There are {i} neighbors for {switch}")


        # "result": {
        #     "vrfs": {
        #         "default": {
        #             "isisInstances": {
        #                 "Osiris": {
        #                     "neighbors": {
        #                         "0000.0001.0004": {