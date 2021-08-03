from netmiko import ConnectHandler


def netmiko_con(ip, password):
    return {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'cisco',
        'password': password
    }

list1= ['10.0.1.2', '10.0.1.202']

for ip_address in list1:
    iosv = netmiko_con(ip = ip_address, password = 'cisco')
    print ('Connecting to ' + str(iosv))
    net_con = ConnectHandler(**iosv)
    output = net_con.send_command('sho ip interface brief')
    print(output)