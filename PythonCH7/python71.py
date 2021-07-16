import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('10.0.1.3', 'cisco', 'cisco')
iosvl2.open()

print ('10.0.1.3')
iosvl2.load_merge_candidate(filename='acl1.txt')
iosvl2.commit_config()
iosvl2.close()

