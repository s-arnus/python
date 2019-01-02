#!/usr/bin/python3
#This script takes input IP's and hostnames or FQDN's from an input file and outputs pairs of IP:FQDN
#There is a list of predefined domains, that are checked used when only a machine name is given without a domain. Can be benefician in company intranet.
import sys, os
import socket
import re

#Domains to check in case only hostname is given and it is not resolved
domains = [".domain.ee", ".google.com", ".google.ee", ".test.local.org"]

#Read in input from a file
def load_input(arg1):
    #print("Starting to read input from: " + full_path)
    with open(arg1, "r") as file:  
        line = file.readline()
        while line:
            #print("Starting to process line: " + line.strip())
            identify_input(line.strip())
            line = file.readline()
#Input can be either a hostname or an IP
#Check which one is provided and act accordingly
def identify_input(arg1):
    #arg1 should be either IPv4, hostname or FQDN
    #print("Checking if",arg1,"is IPv4, FQDN or hostname")
    try:
        #Check if it is IP
        socket.inet_aton(arg1)
        #print(arg1, "is an IP")
        reverse_dns_lookup(arg1)
    except socket.error:
        #print("Not an IP:",arg1)
        #Remove trailing .
        if arg1[-1] == ".":
            arg1 = arg1[:-1]
        #Check if it is just a hostname. Example: host 
        if re.match(r"^[A-Z][A-Z\d-]{1,63}$", arg1.upper()) is not None:
            #print(arg1.upper(),"is a hostname")
            resolve_hostname(arg1.upper())
        #Check if it is a domain or FQDN. Example: host.domain.com
        elif re.match(r"^[A-Z]([A-Z\d-]{1,63})?([.A-Z\d-]{1,63})$", arg1.upper()) is not None:
            #print(arg1.upper(),"is a FQDN")
            resolve_fqdn(arg1.upper())
        else:
            print("ERROR, not sure what",arg1.upper(),"is")

def resolve_fqdn(fqdn):
    try:
        ip = socket.gethostbyname(fqdn)
        print(ip+":"+fqdn)
    except:
        print("Unresolvable FQDN",fqdn)

def resolve_hostname(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print(ip+":"+hostname)
        return
    except:
        #Add a domain name to the hostname to see if it can be resolved to IP
        for domain in domains:
            try:
                ip = socket.gethostbyname(hostname+domain)
                print(ip+":"+hostname+domain)
                #finish with this function as a value was found
                return
            except:
                continue
        print("Unresolvable hostname",hostname)

def reverse_dns_lookup(ip):
    try:
        fqdn = socket.getfqdn(ip).upper()
        if fqdn == ip:
            print("Unresolvable ip",ip)
            return
        print(ip+":"+fqdn)
    except:
        print("Unresolvable ip",ip)

#A module’s __name__ is set equal to '__main__' when read from standard input, a script, or from an interactive prompt.
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("IP to hostname and hostname to IP resolving script needs an input file that contains either IP's, hostnames, FQDN, or all of them")
        print(sys.argv[0] + str(" input_file.txt "))
        sys.exit(-1)
    #Accepting only one argument, the input file
    if len(sys.argv) == 2:
        if not os.path.isfile(sys.argv[1]):
            print("Please retry with a different argument " + sys.argv[1])
            sys.exit(-1)
        #full_path = /home/user/file.txt
        full_path = os.path.abspath(sys.argv[1])
        #sys.argv[1] = file.txt
        load_input(sys.argv[1])