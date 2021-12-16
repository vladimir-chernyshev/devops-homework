#!/usr/bin/env python3

hosts = ['drive.google.com', 'mail.google.com', 'google.com', 'localhost.localdomain.']

import socket, sys, json, yaml

prev_ips = dump_ips = {}
count = 2
while count > 0:
    for host in hosts:
        # resolve DNS
        try:
            junk1, junk2, ips = socket.gethostbyname_ex(host)
        except:
            print("Can not resolve", host)
            continue
        # if of IPs NEQ previous set
        if host in prev_ips and set(ips) != set(prev_ips[host]):
            print("[ERROR]", host," IP mismatch:", prev_ips, ips)
        for ip in ips:
            try:
                # https://docs.python.org/3/howto/sockets.html
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                print(host, ip, "OK")
                s.close()
            except:  # Can't connect()
                print("[ERROR]", host, ip, "FAIL")
        prev_ips[host] = dump_ips[host] = ips
    f = open(sys.argv[0]+'.json', 'w')
    json.dump(dump_ips, f, indent=4)
    f.close()
    f = open(sys.argv[0]+'.yaml', 'w')
    yaml.dump(dump_ips, f)
    f.close()
    count -= 1
