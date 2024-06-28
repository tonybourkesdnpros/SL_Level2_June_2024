import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')

for switch in vlan_dict['switches']:
    print(f"Connecting to switch {switch}")
    connect = pyeapi.connect_to(switch)
    vlan_api = connect.api('vlans')
    for vlan in vlan_dict['vlans_list']:
        vlan_id = vlan['id']
        vlan_name = vlan['name']
        print(f"Adding VLAN {vlan_id} to {switch}")
        vlan_api.create(vlan_id)
        vlan_api.set_name(vlan_id, vlan_name)