Курсовая работа по итогам модуля "DevOps и системное администрирование"
===
1. Создайте виртуальную машину Linux.
 Добавим вторую вирутальную машину в Vagrantfile согласно [документации](https://www.vagrantup.com/docs/multi-machine):
Vagrantfile:

>Vagrant.configure("2") do |config|  
>  config.vm.define "ubuntu" do |ubt|  
>    ubt.vm.box = "bento/ubuntu-20.04"  
>  end  
>  config.vm.define "rocky" do |rck|  
>    rck.vm.box = "bento/rockylinux-8"  
>  end  
> config.vm.network "private_network", type: "dhcp"  
> config.vm.network "forwarded_port", guest: 22, host: 2222, auto_correct: true  
> config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true  
> config.vm.network "forwarded_port", guest: 443, host: 8443, auto_correct: true  
>end  

	$vagrant up rocky
	$vagrant ssh rocky

2. Установите ufw и разрешите к этой машине сессии на порты 22 и 443, при этом трафик на интерфейсе localhost (lo) должен ходить свободно на все порты.
---

В Телеграмм-чате курса был задан вопрос и эксперт уточнил, что использование конкретно *ufw* не принципиально, буду использовать *firewalld* - связано со спецификой основной работы.

	$ sudo systemctl enable firewalld
	$ sudo systemctl start firewalld  
	$ sudo firewall-cmd --get-zone-of-interface=lo
	no zone
	$ sudo firewall-cmd --get-active-zones
	public
	  interfaces: eth0 eth1
	$ sudo firewall-cmd --info-zone=public
	public (active)
	  target: default
	  icmp-block-inversion: no
	  interfaces: eth0 eth1
	  sources: 
	  services: cockpit dhcpv6-client ssh
	  ports: 
	  protocols: 
	  forward: no
	  masquerade: no
	  forward-ports: 
	  source-ports: 
	  icmp-blocks: 
	  rich rules: 
	$ sudo firewall-cmd --add-service=https
	$ sudo firewall-cmd --remove-service=cockpit --remove-service=dhcpv6-client
	$ sudo firewall-cmd --info-zone=public
	public (active)
	  target: default
	  icmp-block-inversion: no
	  interfaces: eth0 eth1
	  sources: 
	  services: https ssh
	  ports: 
	  protocols: 
	  forward: no
	  masquerade: no
	  forward-ports: 
	  source-ports: 
	  icmp-blocks: 
	  rich rules: 
	$ sudo firewall-cmd --runtime-to-permanent


