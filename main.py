#!/usr/bin/env python3

import json
import requests
import http.client
from base64 import b64encode
from credentials import name

# Variables
records = name["records"]
public_ip_api = "https://api.ipify.org"
#name_api = "api.dev.name.com" # Development
name_api = "api.name.com" # Production
#name_token = name["token"]["dev"] # Development
name_token = name["token"]["production"] # Production
name_user = name["username"]
ip_path = "/tmp/current_ip"

# Authorization token: we need to base 64 encode it and then decode it to acsii as python 3 stores it as a byte string
def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

# Check current ip
try:
    with open(ip_path) as f: ip = f.read()
except:
    ip = ""

# Check public_ip
public_ip = requests.get(public_ip_api).text

# If they are different then update
if(public_ip != ip):
    print("Actualizar ip")
    with open(ip_path, "w") as f:
        f.write(public_ip)

    # Update records with public ip
    connection = http.client.HTTPSConnection(name_api)
    for r in records:
        headers = { 'Authorization' : basic_auth(name_user, name_token), 'type': r["type"], 'answer': public_ip }
        connection.request("PUT", "/v4/domains/" + r["domain"] + "/records/" + r["id"], headers=headers)
        res = json.loads(connection.getresponse().read())
        print("Record updated", res)

print("Current ip: ", public_ip)
