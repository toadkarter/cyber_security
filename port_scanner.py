#!/bin/python3

import sys
import socket
from datetime import datetime


def check_arguments():
    if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])  # Translates the host name to IPv4.
    else:
        print("Invalid argument about, please try again.")
        sys.exit()
    return target


def show_welcome_text(target):
    print("-" * 50)
    print(f"Scanning target {target}")
    print(f"Time started: {str(datetime.now())}")
    print("-" * 50)


def check_all_ports_in_range(target):
    try:
        for port in range(50, 85):
            check_port(target)
            sys.exit()

    # If quitting the program.
    except KeyboardInterrupt:
        print("\nExiting program...")
        sys.exit()

    # If hostname could not be resolved.
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()

    # If no connection.
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()


def check_port(target):
    # The below creates a new socket with the following parameters:
    # AF_INET: IPv4
    # SOCK_STREAM: TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # If the port isn't open, it will move on.
    socket.setdefaulttimeout(1.0)
    # Returns an error indicator if there is a failure to connect.
    # Otherwise, will return 0.
    # Note that connect_ex take a tuple as argument.
    result = s.connect_ex((target, port))
    print(f"Checking port {str(port)}")
    if result == 0:
        print(f"Port {str(port)} is open.")


target = check_arguments()
show_welcome_text(target)
check_all_ports_in_range(target)

