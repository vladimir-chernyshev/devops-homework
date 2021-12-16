Домашнее задание к занятию "4.3. Языки разметки JSON и YAML"
===
1. Нужно найти и исправить все ошибки:
---
		{ "info" : "Sample JSON output from our service\t",
		    "elements" :[
		        { "name" : "first",
		        "type" : "server",
		        "ip" : 7175 
		        },
		        { "name" : "second",
		        "type" : "proxy",
		        "ip : 71.78.22.43
		        }
		    ]
		}

 В 1-й строке не экранирован символ "\"
 В 9-й строке пропущена закрывающая кавычка после ключа "ip"
 Для проверки синтаксиса можно использовать функцию **json.loads()**

                { "info" : "Sample JSON output from our service\\t",
                    "elements" : [
                        { "name" : "first",
                        "type" : "server",
                        "ip" : 7175
                        },
                        { "name" : "second",
                        "type" : "proxy",
                        "ip" : "71.78.22.43"
                        }
                    ]
                }

2. Добавить в скрипт из задания 4 4.2 возможность записи JSON и YAML файлов, описывающих опрашиваемые сервисы. Формат записи JSON по одному сервису: { "имя сервиса" : "его IP"}. Формат записи YAML по одному сервису: - имя сервиса: его IP. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.
---

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


Вывод:

>{  
>    "drive.google.com": [  
>        "64.233.163.194"  
>    ],  
>    "mail.google.com": [  
>        "216.58.209.197"  
>    ],  
>    "google.com": [  
>        "216.58.210.142"  
>    ],  
>    "localhost.localdomain.": [  
>        "127.0.0.1"  
>    ]  
>}  

>drive.google.com:  
>- 64.233.163.194  
>google.com:  
>- 216.58.210.142  
>localhost.localdomain.:  
>- 127.0.0.1  
>mail.google.com:  
>- 216.58.209.197  

