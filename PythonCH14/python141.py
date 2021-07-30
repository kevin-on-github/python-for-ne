from netmiko import ConnectHandler
from getpass import getpass

username = input('Enter your SSH username: ')
password = getpass()

R2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.2',
    'username': (username),
    'password': (password)
}
S2 = {
    'device_type': 'cisco_ios',
    'ip': '10.0.1.202',
    'username': (username),
    'password': (password)
}

all_devices = [R2, S2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices['ip']))
    getver_command = ['do show version']
    getint_command = ['do show ip interface brief | exclude unassigned']
    output = net_connect.send_config_set(getver_command)
    output2 = net_connect.send_config_set(getint_command)
    parsedver1 = (output.index('Version'))
    parsedver2 = (output.index(',', parsedver1))
    parsedint1 = (output2.find('Interface'))
    print (output[parsedver1: parsedver1 + (parsedver2 - parsedver1)])
    print (output2[parsedint1: parsedint1 + 163])
