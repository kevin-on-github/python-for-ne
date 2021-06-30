import getpass
import telnetlib

user = input('Enter your telnet username: ')
password = getpass.getpass()

# This script will telnet to each switch contained in the 'myswitches.txt'
# and retrieves the running configuration of the device. The output is sent
# to a local direcory txt file.

f = open('myswitches.txt')

for IP in f:
    IP=IP.strip()
    print ('Get running config from Switch ' + (IP))
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')  
    tn.write(b"terminal length 0\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"show run\n")
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput =  open("switch" + HOST + ".txt", "w")
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write("\n")
    saveoutput.close