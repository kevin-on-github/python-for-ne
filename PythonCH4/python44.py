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


with open('access-design-guide.txt') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [S4, S5, S6]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('core-design-guide.txt') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [S3, S2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)


with open('mgmt-design-guide.txt') as f:
    lines = f.read().splitlines()
print (lines)


all_devices = [S1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
