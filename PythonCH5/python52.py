import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.0.1.2', 'cisco', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
#print (ios_output)
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_arp_table()
#print (ios_output)
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.ping('192.168.1.254')
#print (ios_output)
print (json.dumps(ios_output, indent=4))