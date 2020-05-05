import json
import requests


def add_flow():

    with open('Push_vlan.json', 'r') as f:
        data_1 = json.load(f)
    with open('forward_traffic.json', 'r') as f:
        data_2 = json.load(f)

    print(data_1,data_2)
    _add_flow = requests.post(url='http://192.168.56.104:8080/stats/flowentry/add', data=json.dumps(data_1))
    _add_flow = requests.post(url='http://192.168.56.104:8080/stats/flowentry/add', data=json.dumps(data_2))
    if _add_flow.ok:
        return _add_flow
    else:
        print(_add_flow.content)
        return False

add_flow()

'''
_ip = {'10.0.0.1':10,'10.0.0.2':320,'10.0.0.3':620}
for ip in _ip:
    add_flow(_ip[ip], 65535, _ip)
'''