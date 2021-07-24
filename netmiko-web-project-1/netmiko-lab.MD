## Use NETMIKO to backup Cisco networking devices.

 - For this lab make sure you have an environment with a couple Cisco IOS devices. This could be some physical hardware, or an emulated environment such as Cisco Modeling Labs, EVE-NG, or GNS3.
 - My setup for this lab consists of a Ubuntu-LTS 20.04 automation server. I use several extensions within VS Code to connect to the automation VM to dev the lab. I suggest you use whatever you are comfortable with.
 - Git is another tool I use on the VM for keeping track of where I am. Definitely worth learning git as a devops and automation tool.

### Login to your lab and build the network.

 - First thing I do is deploy a cloud network for communication outside the lab.
 - Then I add the Automation VM. This is Ubuntu 20.04-LTS custom built with python 3.9, git, az-cli, python3-venv, and pip. I like to keep a virtual python environment for each project. Keep the system clean as possible.
 - Now add one IOSv-L2 switch1, and connect the Cloud network and the Ubuntu VM.
 - Add some Cisco IOSv-L2 switches. I'll just toss 5 on the page. Link these 5 switches as a full mesh. Let's call them switch2-switch6.
 - Now link the switch1 to the LAST port of switch2-switch6. Consider this the 'MANAGEMENT' port for automation.
 - Lab should look similar to my picture above. Start all the devices, and verify connectivity. Cisco devices may ask to run an automatic setup... just type no and let them boot to a prompt.
 ![Lab Network](https://github.com/kevin-on-github/kevin-on-github.github.io/raw/main/images/post1_img_screenshot1.png)

 ### Login to each of your network devices and assign basic configs to establish communication.
  - I setup the Automaation VM with a static IP. Will make this 10.0.1.25/24 via netplan.
  - Here are some basic options to program onto the switches. Just enough to establish IP and SSH. \
  ```
  enable
  configure terminal
  hostname switchX

  ! Create a username and password for automation and access. This is a lab, not a security demonstration. Do a better setup in production.
  username cisco privilege 15 password cisco
  
  ! Assign a domain name so a crypto key can generate.
  ip domain-name eve-ng.net

  ! Minimum for SSH2.0 is 768, so choose anything higher than that.
  crypto key generate rsa modulus 2048
  
  ! I'll use 10.0.1.202-206 for my switches.
  interface vlan 1
   ip address 10.0.1.X 255.255.255.0
   no shutdown

  !Here we enable ssh and telnet on the vty lines.
  line vty 0 4
   login local
   login transport all

   ```
   At this point each network device should be pingable from the Automation server.

   ```
   cisco@ubuntu:~$ ip addr | grep -i ens3
2: ens3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    inet 10.0.1.25/24 brd 10.0.1.255 scope global ens3
cisco@ubuntu:~$ 
   ```
   ```
 cisco@ubuntu:~$ for ip in $(seq 202 206); do ping -c 1 10.0.1.$ip | grep "bytes from"; done
64 bytes from 10.0.1.202: icmp_seq=1 ttl=255 time=8.18 ms
64 bytes from 10.0.1.203: icmp_seq=1 ttl=255 time=12.6 ms
64 bytes from 10.0.1.204: icmp_seq=1 ttl=255 time=6.95 ms
64 bytes from 10.0.1.205: icmp_seq=1 ttl=255 time=7.19 ms
64 bytes from 10.0.1.206: icmp_seq=1 ttl=255 time=12.8 ms
   ```

### Now we can make sure that SSH logins work. You may want to create an alias for the SSH command to enable some outdated IOSv images. It's a limitation of the Cisco Modeling Lab images, but there is an easy workaround. It's not required for Netmiko, only for SSH commands from my Automation machine.

 - So if you get an error like this...
 
 ```
 cisco@ubuntu:~$ ssh cisco@10.0.1.202
Unable to negotiate with 10.0.1.202 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1
```
 - Copy/past this into a termina...

`echo 'alias ssh="ssh -oKexAlgorithms=+diffie-hellman-group14-sha1"' >> ~/.bashrc
`

 - Re-apply your .bashrc file

`source ~/.bashrc`

 - Now it's good to go.

 ```
 cisco@ubuntu:~$ ssh cisco@10.0.1.202

**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
Password: ****************************************************************
Password:
```

### Now we can setup our python environment and install the necessary modules.

 - First let's get logged into our Automation server. I just use SSH. Accessing through the EVE-NG remote tools don't always have copy/paste support. Use whatever you like though.
 - Update your references. Upgrade is recommended but not necessary.
 ```
 cisco@ubuntu:~$ sudo apt-get update && sudo apt-get upgrade -y
 ```
 - Now lets add some packages.
 ```
 sudo apt-get install python3 python3-pip python3-setuptools python3-venv
 ```
  - Python virtual environments are important to keep a system clean. The first line sets up the venv location, second line links the terminal to the virtual environment. We will install our modules into this venv. Notice how the prompt changes to indicate the venv.
  ```
  cisco@ubuntu:~$ python3 -m venv ~/pyenv/python-for-ne
cisco@ubuntu:~$ source ~/pyenv/python-for-ne/bin/activate
(python-for-ne) cisco@ubuntu:~$ 

  ```
 - Now lets use pip to add the modules. I've included a uri with the modules for this lab. Will take a few minutes, there will be some errors, however they are not relevant for Netmiko with Cisco equipment.
 - There is a deprecated module that gets installed with simple-crypt. You may have to pip uninstall 'pycrypto' and reinstall 'pycryptodome'. It's been an issue for a while now, so be aware may have to tshoot it.
 ```
(python-for-ne) cisco@ubuntu:~$ pip install -r https://raw.githubusercontent.com/kevin-on-github/python-for-ne/main/requirements.txt
```
### Now grab [netmiko-lab.py](netmiko-lab.py) and copy/paste the contents to a similarly named file on the Automation server. Now with Python we can automate securely connecting to the devices, loop through a simple database of devices, try and connect, and export the config to a text file in the local directory.
```
(python-for-ne) cisco@ubuntu:~/pyenv/python-for-ne/scripts$ python3 netmiko-lab.py
Enter your SSH username: cisco
Password: 
Connecting to device" 10.0.1.202
---- Getting configuration from device
---- Writing configuration:  config-10.0.1.202
Connecting to device" 10.0.1.203
---- Getting configuration from device
---- Writing configuration:  config-10.0.1.203
Connecting to device" 10.0.1.204
---- Getting configuration from device
---- Writing configuration:  config-10.0.1.204
Connecting to device" 10.0.1.205
---- Getting configuration from device
---- Writing configuration:  config-10.0.1.205
Connecting to device" 10.0.1.206
---- Getting configuration from device
---- Writing configuration:  config-10.0.1.206
(python-for-ne) cisco@ubuntu:~/pyenv/python-for-ne/scripts$ ls
config-10.0.1.202  config-10.0.1.204  config-10.0.1.206
config-10.0.1.203  config-10.0.1.205  netmiko-lab.py
(python-for-ne) cisco@ubuntu:
```

### This completes the lab. Congratulations you did it.