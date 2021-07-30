from netmiko import ConnectHandler
from getpass import getpass

#username = input('Enter your SSH username: ')
#password = getpass()
username = ('cisco')
password = ('cisco')

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

all_devices1 = []
all_devices = [R2, S2]

for devices in all_devices1:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices))
    config_commands = ['do show version']
    output = net_connect.send_config_set(config_commands)
    #print (output.strip())
    parsed1 = (output.find('Version'))
    print (parsed1)

for devices in all_devices1:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices))
    config_commands = ['do show ip interface brief']
    output = net_connect.send_config_set(config_commands)
    #print (output.strip())
    parsed1 = (output.count('Giga'))
    print (output)
    print (parsed1)

for devices in all_devices1:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices))
    config_commands = ['do show version']
    output = net_connect.send_config_set(config_commands)
    #print (output.strip())
    parsed1 = (output.index('Version'))
    parsed2 = (output.index(',', parsed1))
    #print (parsed1)
    #print (parsed2)
    print (output[parsed1: parsed1 + (parsed2 - parsed1)])



for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    print ("Connecting to device... " + str(devices))
    config_commands = ['do show version']
    output = net_connect.send_config_set(config_commands)
    #print (output.strip())
    parsed1 = (output.index('Version'))
    parsed2 = (output.index(',', parsed1))
    #print (parsed1)
    #print (parsed2)
    print (output[parsed1: parsed1 + (parsed2 - parsed1)])