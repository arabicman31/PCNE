from ncclient import manager
xe= {
"ip_address": "192.168.255.133",
"netconf_port": "830",
"username": "cisco",
"password": "cisco"
}
with manager.connect(
    host=xe["ip_address"], 
    port=xe["netconf_port"], 
    username=xe["username"],
    password=xe["password"],
    hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print capability