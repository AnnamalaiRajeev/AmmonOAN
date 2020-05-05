import requests
from Ofctl_statistics_mappings import *
from ryu import *
import json
import redis


def add_flow(vlan_tag, priority=65535, dpid=None, ipv4_src=None, table_id=None):

    with open('Push_vlan.json', 'r') as f:
        data_1 = json.load(f)
    with open('forward_traffic.json', 'r') as f:
        data_2 = json.load(f)
        data_1['actions'][1] = vlan_tag
        if ipv4_src:
            data_1['match']['ipv4_src'] = ipv4_src
        if priority:
            data_1['priority'] = priority
        if dpid:
            data_1['dpid'] = dpid
        if table_id:
            data_1['table_id'] = table_id
    print(data_1,data_2)
    _add_flow = requests.post(url='http://192.168.56.104:8080/stats/flowentry/add', data=json.dumps(data_1))
    _add_flow = requests.post(url='http://192.168.56.104:8080/stats/flowentry/add', data=json.dumps(data_2))
    if _add_flow.ok:
        return _add_flow
    else:
        print(_add_flow.content)
        return False


def create_redis_clinet(server_ip,port=None):
    if port == None:
        client = redis.Redis(server_ip, port=6379)
    else:
        client = redis.Redis(server_ip,port=port)
    return client


def wrap_requests(func):
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        if return_value.ok:
            print(return_value.json())
            print(return_value.status_code)
        if return_value:
            return return_value
        else:
            return None
    return wrapper


def request_get(Content_To_Retrieve):
    response = requests.get('http://192.168.56.104:8080/{}'.format(Content_To_Retrieve))
    return response


if __name__ == '__main__':
    response = request_get('stats/flow/{}')
    print(response.content)
    assert response






























'''
    response = request_get(Switch_Table_Features)
    response = request_get(Switch_Port_Stats)
    client = create_redis_clinet('192.168.56.104')

    _customers = client.hgetall(name='AuthenticationTable')  # {b'10.0.0.1': b'True'}
    print(_customers)
    for _customer in _customers:
        _customer = _customer.decode()
        print(_customer)
        # (vlan_tag, priority=65535, dpid=None, ipv4_src=None, table_id=None):
        results = map(add_flow, [62000], [1], [_customer], [0], [4]) #lazy iterator
        for result in results:
            print("yo")
            print(result)
#


'''


