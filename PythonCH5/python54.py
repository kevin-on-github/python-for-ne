import json
from napalm import get_network_driver

bgpdb = ['10.0.1.1', '10.0.1.2']

for ip_address in bgpdb:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'cisco', 'cisco')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    