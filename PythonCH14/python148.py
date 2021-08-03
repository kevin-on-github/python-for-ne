# import the modules for script
import sqlite3
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


# connect to the sqlite database and select table and columns
con=sqlite3.connect ('sqlite.db')
cur = con.cursor()
sqlite = cur.execute('select name, ip_addr, device_type, username, password, net_role from eveng')

def netmiko_con():
    ''' This function builds the netmiko connection profile'''
    return {
        'ip': ip_addr,
        'device_type': 'cisco_ios',
        'username': username,
        'password': password
        }
  

for item in sqlite:
    name = item[0]
    ip_addr = item[1]
    username = item[3]
    password = item[4]
    role = item[5]
    while (name == 'R2' or name == 'S2'):
        iosv = netmiko_con()
        print ('Connecting to ' + str(iosv))
        net_con = ConnectHandler(**iosv)
        output = net_con.send_command('sho ip interface brief')
        print(output)




