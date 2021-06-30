import getpass
import telnetlib

HOST = "192.168.1.202"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# During the class it was stated this is not how programs should be written, this is more difficult than
# just programming the devices directly. As the first code lab though it does show how the telnetlib and
# getpass modules work. Additional labs will build upon these basic samples.
    
tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"int vlan 2\n")
tn.write(b"ip address 1.1.1.1 255.255.255.0\n")
tn.write(b"int vlan 3\n")
tn.write(b"ip address 2.2.2.2 255.255.255.0\n")
tn.write(b"int gi0/2\n")
tn.write(b"switchport access vlan 2\n")
tn.write(b"int gi0/3\n")
tn.write(b"switchport access vlan 3\n")
tn.write(b"int ra vlan 2 - 3\n")
tn.write(b"no shut\n")
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
