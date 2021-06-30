import getpass
import telnetlib

HOST = "192.168.1.202"
MASK = " 255.255.255.0"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")

# This is the loop section. Concatenate the text with the string variables in the range n
# I am using the string twice as the IP address, and inserting a network mask.
# These vlans are not tied to an interface, so even with the no shut they won't be active
#    until 'switchport access vlan #' is configured.

for n in range (2,11):
    tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
    tn.write(b"int vlan " + str(n).encode('ascii') + b"\n")
    tn.write(b"ip addr 1.1." + str(n).encode('ascii') + b".1" + str(MASK).encode('ascii') + b"\n")


tn.write(b"int range vlan 1 - 10\n")
tn.write(b"no shut\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))