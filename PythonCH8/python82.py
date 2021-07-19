from netmiko import ConnectHandler

with open('commands_file') as f:
    commands_to_send = f.read().splitlines()

ios_devices = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.1',
    'username': 'cisco',
    'password': 'cisco',
}

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(commands_to_send)
    print (output) 