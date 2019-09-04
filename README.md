# simple_network_scanner
This is basic network scanner that can scan the all devices which are in the connected network and give their ip address and mac address.
Follow the isntructions
clone the repository and go into the reposistory folder.
install python dependencies using requirements,txt with the follwing command.


pip3 install -r requirements.txt

sudo python network_scanner.py



Traceback (most recent call last):
  File "network_scanner.py", line 1, in <module>
    import scapy.all as scapy
ModuleNotFoundError: No module named 'scapy'
 If you had this problem download scapy from this command
  sudo apt-get install python-scapy
