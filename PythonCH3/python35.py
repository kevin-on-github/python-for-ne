import getpass
import telnetlib

HOST = "localhost"
f = open ('myswitches.txt')
user = input("Enter your telnet username: ")
password = getpass.getpass()



# Here we are opening a local text file containing an IP address
# per line that corresponds to a l2 switch inventory. The for loop
# is reading the IP as f: and applying a configuration.

for IP in f:
    IP = IP.strip()
    print ("Configuring Switch " + (IP))  
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"spanning-tree mode rapid-pvst\n")
    tn.write(b"vlan 2\n")
    tn.write(b"name Python_VLAN_2\n")
    tn.write(b"vlan 3\n")
    tn.write(b"name Python_VLAN_3\n")
    tn.write(b"router ospf 1\n")
    tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
