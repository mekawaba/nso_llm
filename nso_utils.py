#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
import json

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

# credentials for CSR1000v
HOST = '192.168.4.41'
PORT = 8090  # 環境によって異なる
USER = 'admin'
PASS = 'admin'


def getLoopback(hostname):
    # url string to issue request
    url = "http://{h}:{p}/restconf/data/tailf-ncs:devices/device={hostname}/config/tailf-ned-cisco-ios-xr:interface/Loopback=0/ipv4/address/ip".format(h=HOST, p=PORT,hostname=hostname)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {}

    # this statement performs a PUT on the specified url
    """
    response = requests.get(url, auth=(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    """ 

    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)
    
    data = response.json()
    # print the json that is returned
    # print(data['tailf-ned-cisco-ios-xr:ip'])
    return data['tailf-ned-cisco-ios-xr:ip']

if __name__ == '__main__':
    getLoopback("xr-2")
