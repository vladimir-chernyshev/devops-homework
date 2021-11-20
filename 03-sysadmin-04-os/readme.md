Домашнее задание к занятию "3.4. Операционные системы, лекция 2"
===
1. Используя знания из лекции по systemd, создайте самостоятельно простой unit-файл для node_exporter.
---

Установка **node_exporter** согласно [документа](https://prometheus.io/docs/guides/node-exporter/):

		$wget https://github.com/prometheus/node_exporter/releases/download/v1.3.0/node_exporter-1.3.0.linux-amd64.tar.gz
		$ tar xzf node_exporter-1.3.0.linux-amd64.tar.gz
		$ sudo mv node_exporter-1.3.0.linux-amd64/node_exporter /usr/local/bin/

		$ sudo mkdir /etc/systemd/system/node_exporter.service.d
		$ sudo vi /etc/systemd/system/node_exporter.service

>	[Unit]
>
>	Description=Prometheus exporter
>
>	Documentation=https://github.com/prometheus/node_exporter
>
>	[Install]
>
>	WantedBy=multi-user.target
>
>	[Service]
>
>	ExecStart=/usr/local/bin/node_exporter

		$ sudo systemctl enable node_exporter
		$ sudo systemctl start node_exporter
		$ systemctl status node_exporter
		$ sudo reboot
		$ systemctl status node_exporter

>● node_exporter.service - Prometheus exporter
>
>     Loaded: loaded (/etc/systemd/system/node_exporter.service; enabled; vendor)
>
>     Active: active (running) since Fri 2021-11-19 22:41:58 UTC; 22min ago
>
>       Docs: https://github.com/prometheus/node_exporter
>
>   Main PID: 610 (node_exporter)
>
>      Tasks: 4 (limit: 1071)
>
>     Memory: 13.8M
>
>     CGroup: /system.slice/node_exporter.service
>
>             └─610 /usr/local/bin/node_exporter

		$ sudo systemctl stop node_exporter

2. Ознакомьтесь с опциями **node_exporter** и выводом */metrics* по-умолчанию. Приведите несколько опций, которые вы бы выбрали для базового мониторинга хоста по CPU, памяти, диску и сети.
---

		$ curl http://localhost:9100/metrics | egrep ^node_
		[..]
		$ /usr/local/bin/node_exporter --help

Немного [Google-fu](https://askubuntu.com/questions/659267/how-do-i-override-or-configure-systemd-services):

		$ sudo systemctl edit node_exporter

>	[Service]
>
>	ExecStart=
>
>	ExecStart=/usr/local/bin/node_exporter --collector.disable-defaults --collector.netstat --collector.meminfo --collector.cpu --collector.filesystem

		$ sudo systemctl daemon-reload


