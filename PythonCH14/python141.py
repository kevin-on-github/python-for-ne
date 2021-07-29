from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter your SSH username: ')
password = getpass()

S1 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': (username),
    'password': (password)
}
S2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.3',
    'username': (username),
    'password': (password)
}

all_devices = [S1, S2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices))
    config_commands = ['do show version | include Version'] + ['do sho ip interface brief | exclude unassigned']
    output = net_connect.send_config_set(config_commands)
    print (output.strip())
