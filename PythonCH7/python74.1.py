import json
from napalm import get_network_driver

devicelist = ['10.0.1.2',
              '10.0.1.3'
              ]

for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    print ("Configure ACLs on " + "1.1.1." + ip_address[-1])
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'cisco', 'cisco')
    
    iosv.open()
    iosv.load_merge_candidate(filename='acl1.txt')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No ACL changes required.')
        iosv.discard_config()

    iosv.load_merge_candidate(filename='ospf1.txt')
    print ("Configure OSPF on " + "1.1.1." + ip_address[-1])
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No OSPF changes required.')
        iosv.discard_config()

devicelist = ['10.0.1.2']

for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    print ("Configure BGP on " + "1.1.1." + ip_address[-1])
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'cisco', 'cisco')
    iosv.open()
    iosv.load_merge_candidate(filename='bgp2.txt')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No BGP changes required.')
        iosv.discard_config()
    

devicelist = ['10.0.1.3']

for ip_address in devicelist:
    print ("Connecting to " + str(ip_address))
    print ("Configure BGP on " + "1.1.1." + ip_address[-1])
    driver = get_network_driver('ios')
    iosv = driver(ip_address, 'cisco', 'cisco')
    iosv.open()
    iosv.load_merge_candidate(filename='bgp3.txt')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print('No BGP changes required.')
        iosv.discard_config()
    