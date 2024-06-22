# ddns-name.com
Script to update dns register in name.com domain

You need to define a credentials.py file that has a name variable defined as an object as follow:

```python 
#!/usr/bin/env python3

name = {
    "records": [
        {"domain": "example1.com", "id": "id_record_1", "type": "A"},
        {"domain": "example2.com", "id": "id_record_2", "type": "A"}
    ],
    "username": "my_username",
    "token": {
        "production": "prod_token",
        "dev": "dev_token"
    },
    "domain": "example.com"
}

```

name["domain"] is used by the script check_records.py to print all the records in that domain
name["records"] is an array of objects pointed to the records you want to update the ip with script main.py
name["username"] and name["token"] are the credentials provided by name.com to use its API
