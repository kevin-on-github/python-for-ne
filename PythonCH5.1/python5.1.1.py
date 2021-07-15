import json
from napalm import get_network_driver

rtrdb = ['10.0.1.1', '10.0.1.2', '10.0.1.3', '10.0.1.4', '10.0.1.5', '10.0.1.6', '10.0.1.7', '10.0.1.8']
rtrbgpdb = ['10.0.1.3', '10.0.1.6']

for ip_address in rtrdb:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'cisco', 'cisco')
    iosv_router.open()

    output = iosv_router.get_interfaces_ip()
    print (json.dumps(output, indent=4))

    output = iosv_router.get_interfaces_counters()
    print (json.dumps(output, sort_keys=True, indent=4))

for ip_address in rtrbgpdb:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'cisco', 'cisco')
    iosv_router.open()
    output = iosv_router.get_bgp_neighbors()
    print (json.dumps(output, indent=4))