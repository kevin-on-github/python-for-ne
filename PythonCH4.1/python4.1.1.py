from netmiko import ConnectHandler

vIOS1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.1',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS3 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.3',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS4 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.4',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS5 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.5',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS6 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.6',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS7 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.7',
    'username': 'cisco',
    'password': 'cisco'
}

vIOS8 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.8',
    'username': 'cisco',
    'password': 'cisco'
}

all_devices = [vIOS1, vIOS2, vIOS3, vIOS4, vIOS5, vIOS6, vIOS7, vIOS8]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command('show ip int brief')
    print (output)
    