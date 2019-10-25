# simple_network_scanner
This is basic network scanner that can scan the all devices which are in the connected network and give their ip address and mac address.
Follow the isntructions
clone the repository and go into the reposistory folder.

#### Installing dependencies

install python dependencies using requirements,txt with the follwing command.

pip3 install -r requirements.txt

sudo python3 network_scanner.py -t [IP address range]

in the IP address range variable, you want to put your range in the CIDR notation(192.168.1.1/24)

```bash
Traceback (most recent call last):
  File "network_scanner.py", line 1, in <module>
    import scapy.all as scapy
ModuleNotFoundError: No module named 'scapy'
```

 If you had this problem download scapy from this command
 
 ```bash
sudo apt-get install python-scapy
```
More details can be found in https://medium.com/@cvaram96/creating-own-network-scanner-using-python-f11a50a5ff77?source=friends_link&sk=64fbe1a530bff1a6ace92d778b232a97
