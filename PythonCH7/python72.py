import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosv = driver('10.0.1.3', 'cisco', 'cisco')
iosv.open()

print ('Accessing 10.0.1.3')
iosv.load_merge_candidate(filename='acl1.txt')

diffs = iosv.compare_config()
if len(diffs) > 0:
    print(diffs)
    iosv.commit_config()
else:
    print('No changes required.')
    iosv.discard_config()
