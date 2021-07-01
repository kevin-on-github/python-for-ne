from netmiko import ConnectHandler


S1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': 'cisco',
    'password': 'cisco'
}
S2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.202',
    'username': 'cisco',
    'password': 'cisco'
}

S3 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.203',
    'username': 'cisco',
    'password': 'cisco'
}

S4 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.204',
    'username': 'cisco',
    'password': 'cisco'
}

S5 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.205',
    'username': 'cisco',
    'password': 'cisco'
}
S6 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.206',
    'username': 'cisco',
    'password': 'cisco'
}

all_devices = [S1, S2, S3, S4, S5, S6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,21):
       print ("Creating VLAN " + str(n))
       config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
       output = net_connect.send_config_set(config_commands)
       print (output)