# import the modules for script
import sqlite3
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from jinja2 import Template

def tryexcept():
    # Exception errors from netmiko
    try:
        net_connect = ConnectHandler(**device)
    except (AuthenticationException):
        print ('Authentication failure: ' + name)
        pass
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + name)
        pass
    except (EOFError):
        print ('End of file while attempting device ' + name)
        pass
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled? ' + name)
        pass
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        pass

# connect to the sqlite database and select table and columns
con=sqlite3.connect ('sqlite.db')
cur = con.cursor()
sqlite = cur.execute('select name, ip_addr, device_type, username, password, net_role from eveng')

for item in sqlite:
    name = (item[0])
    role = (item[5])
    device = {
              'ip': (item[1]),
              'device_type': (item[2]),
              'username': (item[3]),
              'password': (item[4]),
            }
  
    # run a while loop based on device role and apply a configuration
    while (role == 'router' and name == 'R2'):
        net_connect = ConnectHandler(**device)
        rtr_file = open('rtr-design-guide.txt').read()
        rtr_template = Template(rtr_file)
        rtr_commands = rtr_template.render(name = name).splitlines()
        tryexcept()
        print ("Connecting to device... " + (name))
        config_commands = ['do write memory']
        output = net_connect.send_config_set(rtr_commands)
        output2 = net_connect.send_config_set(config_commands)
        print ('---- Getting configuration from device')
        config_data = net_connect.send_command('show run')
        config_filename = 'config-' + name + '-' + device['ip'] + '.txt' # Important - create unique configuration file name
        print ('---- Writing configuration: ', config_filename)
        with open( config_filename, 'w' ) as config_out:  config_out.write( config_data )
        break
    
    # run a while loop based on device role and apply a configuration
    while (role == 'switch' and name == 'S2'):
        net_connect = ConnectHandler(**device)
        sw_file = open('sw-design-guide.txt').read()
        sw_template = Template(sw_file)
        sw_commands = sw_template.render(name = name).splitlines()
        tryexcept()
        print ("Connecting to device... " + (name))
        config_commands = ['do write memory']
        output = net_connect.send_config_set(sw_commands)
        output2 = net_connect.send_config_set(config_commands)
        print ('---- Getting configuration from device')
        config_data = net_connect.send_command('show run')
        config_filename = 'config-' + name + '-' + device['ip'] + '.txt'  # Important - create unique configuration file name
        print ('---- Writing configuration: ', config_filename)
        with open( config_filename, 'w' ) as config_out:  config_out.write( config_data )
        break
    