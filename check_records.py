#!/usr/bin/env python3

import json
import http.client
from base64 import b64encode
from credentials import name

# Variables
name_api = "api.name.com" # Production
name_token = name["token"]["production"]
name_user = name["username"]
domain = name["domain"]

# Authorization token: we need to base 64 encode it and then decode it to acsii as python 3 stores it as a byte string
def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

# Check records
connection = http.client.HTTPSConnection(name_api)
headers = { 'Authorization' : basic_auth(name_user, name_token) }
connection.request("GET", "/v4/domains/" + domain + "/records", headers=headers)
res = json.loads(connection.getresponse().read())
for r in res["records"]:
    print("New record", r)
