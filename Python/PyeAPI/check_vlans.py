import yaml
import pyeapi

file = open('vlans.yml', 'r')
vlan_dict = yaml.safe_load(file)

pyeapi.load_config('eapi.conf')
connect = pyeapi.connect_to('leaf3')
cmd = connect.enable('show vlan')
for vlan in cmd[0]['result']['vlans']:
    print(f"Report for vlan {vlan}")
    enable_vlan_dict = cmd[0]['result']['vlans'][vlan]['interfaces']
    for vlan_active in enable_vlan_dict:
        print(f"VLAN {vlan} is enabled on {vlan_active} ")

