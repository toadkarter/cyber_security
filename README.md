# Cyber Security Exercises
This repository contains assorted scripts and general exercises relating to ethical hacking. 
The concepts for the creation of this content were learned by reviewing the excellent Free Code Camp tutorial on penetration testing ([link here](https://www.youtube.com/watch?v=3Kq1MIfTWCE&t=14807s)).

### 1. Port Scanner
---
This short Python script will review the ports of a particular network and will output a list of the ports that are currently open. 

This is achieved by opening an IPv4 TCP connection with said host and using Python's in-built "socket" module to check if any of the ports are open for traffic. 

If testing against your own router, the ports that will most likely be open are:
* **Port 53**: This port is used for the DNS protocol; and
* **Port 80**: This port is used for HTTP communication. 

This script can be run on the command line with a singular argument representing the desired IP address that the user wishes to scan. 

For example: python3 port_scanner.py 0.0.0.0
