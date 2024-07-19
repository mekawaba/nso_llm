#!/usr/bin/python
import requests
from requests.auth import HTTPBasicAuth
import json

# disable warnings from SSL/TLS certificates
requests.packages.urllib3.disable_warnings()

HOST = '192.168.4.41'
PORT = 8090  # 環境によって異なる
USER = 'admin'
PASS = 'admin'


def getLoopback(hostname):
    # url string to issue request
    url = "http://{h}:{p}/restconf/data/tailf-ncs:devices/device={hostname}/config/tailf-ned-cisco-ios-xr:interface/Loopback=0/ipv4/address/ip".format(h=HOST, p=PORT,hostname=hostname)

   #print(url)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    response = requests.get(url, auth=HTTPBasicAuth(USER, PASS), headers=headers, verify=False)

    #print(response.status_code)
    #print(response)

    if response.status_code == 200:
        res = response.json()['tailf-ned-cisco-ios-xr:ip']
    else:
        res = "No Config"
    
    # print the json that is returned
    #print(data['tailf-ned-cisco-ios-xr:ip'])
    #return data['tailf-ned-cisco-ios-xr:ip']
    print(res)
    return res


def configBGPcheck(hostname, addr):
    # url string to issue request
    url = "http://{h}:{p}/restconf/operations/custom-actions/configBGPcheck".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {
        "input":
            {
                "hostname": hostname,
                "addr": addr
            }
    }

    # this statement performs a PUT on the specified url
    response = requests.post(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    
    #print(response.status_code)
    #print(response)

    if response.status_code == 200:
        data = response.json()['checkstatus:output']['result']
    else:
        data = "Error"
    
    print(data)
    
    return data


def checkBGPstatus(hostname, addr):
    # url string to issue request
    url = "http://{h}:{p}/restconf/operations/custom-actions/checkBGPstatus".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {
        "input":
            {
                "hostname": hostname,
                "nbr-addr": addr
            }
    }

    # this statement performs a PUT on the specified url
    response = requests.post(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    
    #print(response.status_code)
    #print(response)

    if response.status_code == 200:
        data = response.json()['checkstatus:output']['result']
    else:
        data = "Error"
    
    print(data)
    
    return data


def pingCheck(hostname, addr):
    # url string to issue request
    url = "http://{h}:{p}/restconf/operations/custom-actions/pingCheck".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {
        "input":
            {
                "hostname": hostname,
                "addr": addr
            }
    }

    # this statement performs a PUT on the specified url
    response = requests.post(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    
    #print(response.status_code)
    #print(response)

    if response.status_code == 200:
        data = response.json()['checkstatus:output']['result']
    else:
        data = "Error"
    
    print(data)
    
    return data



def dryrunBGPconfig(dev1, dev2, dev1loop, dev2loop, asnum):
    # url string to issue request
    url = "http://{h}:{p}/restconf/data/bgpmgr:bgpmgr?dry-run=native".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {
        "bgpmgr:bgpmgr": [
        {
        "name": "mytest",
        "dev1": dev1,
        "dev2": dev2,
        "as": asnum,
        "dev1-loop": dev1loop,
        "dev2-loop": dev2loop
        }
        ]
    }

    # this statement performs a PUT on the specified url
    response = requests.patch(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    
    #print(response.status_code)
    #print(response)

    data = response.json()['dry-run-result']['native']['device']
    #print(data[0])
    #print(data[1])

    i=0
    while i < len(data):
        print(data[i]['name'])
        print(data[i]['data'])
        i += 1

    return data


def setBGPconfig(dev1, dev2, dev1loop, dev2loop, asnum):
    # url string to issue request
    url = "http://{h}:{p}/restconf/data/bgpmgr:bgpmgr".format(h=HOST, p=PORT)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # RESTCONF doby for new ACL
    body_data = {
        "bgpmgr:bgpmgr": [
        {
        "name": "mytest",
        "dev1": dev1,
        "dev2": dev2,
        "as": asnum,
        "dev1-loop": dev1loop,
        "dev2-loop": dev2loop
        }
        ]
    }

    # this statement performs a PUT on the specified url
    response = requests.patch(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, data=json.dumps(body_data), verify=False)
    
    #print(response)
    if response.ok:
        res = "Service: mytest created!"
    else:
        res = "Error"
    
    print(res)
    
    return res


def delBGPconfig(servicename):
    # url string to issue request
    url = "http://{h}:{p}/restconf/data/bgpmgr:bgpmgr={s}".format(h=HOST, p=PORT, s=servicename)

    # RESTCONF media types for REST API headers
    headers = {'Content-Type': 'application/yang-data+json',
               'Accept': 'application/yang-data+json'}

    # this statement performs a PUT on the specified url
    response = requests.delete(url, auth=HTTPBasicAuth(USER, PASS),
                            headers=headers, verify=False)
    
    if response.ok:
        res = "Service: mytest deleted!"
    else:
        res = "Error"
    
    print(res)
    
    return res


if __name__ == '__main__':
    '''
    ### Create Service ###
    print("PRE-CHECK")
    getLoopback("xr-1")
    getLoopback("xr-2")
    pingCheck("xr-1", "2.2.2.2")
    pingCheck("xr-2", "1.1.1.1")
    configBGPcheck("xr-1", "2.2.2.2")
    configBGPcheck("xr-2", "1.1.1.1") 

    print("\n")
    print("CREATE SERVICE")
    dryrunBGPconfig("xr-1", "xr-2", "1.1.1.1", "2.2.2.2", "100")
    setBGPconfig("xr-1", "xr-2", "1.1.1.1", "2.2.2.2", "100")

    print("\n")
    print("POST CHECK")
    configBGPcheck("xr-1", "2.2.2.2")
    configBGPcheck("xr-2", "1.1.1.1") 
    checkBGPstatus("xr-1", "2.2.2.2")
    checkBGPstatus("xr-2", "1.1.1.1") 
    '''

    ### Delete Service ###
    '''
    print("DELETE SERVICE")
    delBGPconfig("mytest")
    configBGPcheck("xr-1", "2.2.2.2")
    configBGPcheck("xr-2", "1.1.1.1") 
    '''

