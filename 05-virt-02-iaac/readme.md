Домашнее задание к занятию "5.2. Применение принципов IaaC в работе с виртуальными машинами"
===
1. Опишите своими словами основные преимущества применения на практике IaaC паттернов. Какой из принципов IaaC является основополагающим?
---

 Согласно [Wikipedia](https://en.wikipedia.org/wiki/Infrastructure_as_code), IaaC (автоматизация инфраструктуры) имеет три преимущества:
 - уменьшение стоимости обслуживания инфраструктуры;
 - увеличение скорости выполнения операций;
 - снижение риска человеческой ошибки.

Основопологающий принцип Iaac - идемпонентность, то есть неизменность результата безотносительно количества повторов операций.

2. Чем Ansible выгодно отличается от других систем управление конфигурациями? Какой, на ваш взгляд, метод работы систем конфигурации более надёжный, *push* или *pull?*

 Преимущество ansible заключается в возможности его запуска без установки специального программного обеспечения (agentless). Для работы ansible на целевом хосте требуется только интерпретатор Python, который тоже можно установить с помощью ansible.  
 У обоих подходов есть множество преимуществ и недостатков, и кроме того, судя по [Wikipedia](https://en.wikipedia.org/wiki/Pull_technology),  с помощью *pull* можно сэмулировать *push*.

3. Установить на личный компьютер *VirtualBox*, *vagrant*, *ansible*. Зайти внутрь ВМ, убедиться, что Docker установлен с помощью команды *docker ps*

---
 - VirtualBox
>	$ sudo dnf install VirtualBox-6.1
>	Last metadata expiration check: 0:00:22 ago on Wed 19 Jan 2022 12:06:45 AM +05.
>	Package VirtualBox-6.1-6.1.30_148432_fedora33-1.x86_64 is already installed.
>	Dependencies resolved.
>	Nothing to do.
>	Complete!

 - Vagrant

>	$ sudo dnf install vagrant
>	Last metadata expiration check: 0:02:50 ago on Wed 19 Jan 2022 12:06:45 AM +05.
>	Package vagrant-2.2.19-1.x86_64 is already installed.
>	Dependencies resolved.
>	Nothing to do.
>	Complete!

 - Ansible

>	$ sudo dnf install ansible
>	Last metadata expiration check: 0:04:13 ago on Wed 19 Jan 2022 12:06:45 AM +05.
>	Dependencies resolved.
>	================================================================================
>	 Package                    Arch        Version              Repository    Size
>	================================================================================
>	Installing:
>	 ansible                    noarch      2.9.27-1.fc35        updates       15 M
>	Installing dependencies:
>	 python3-babel              noarch      2.9.1-4.fc35         fedora       5.8 M
>	 python3-bcrypt             x86_64      3.2.0-1.fc35         fedora        43 k
>	 python3-jinja2             noarch      3.0.1-2.fc35         fedora       529 k
>	 python3-jmespath           noarch      0.10.0-4.fc35        fedora        46 k
>	 python3-ntlm-auth          noarch      1.5.0-4.fc35         fedora        53 k
>	 python3-pynacl             x86_64      1.4.0-4.fc35         fedora       108 k
>	 python3-pytz               noarch      2021.3-1.fc35        updates       47 k
>	 python3-pyyaml             x86_64      5.4.1-4.fc35         fedora       191 k
>	 python3-requests_ntlm      noarch      1.1.0-16.fc35        fedora        18 k
>	 python3-xmltodict          noarch      0.12.0-13.fc35       fedora        22 k
>	Installing weak dependencies:
>	 python3-paramiko           noarch      2.9.1-1.fc35         updates      295 k
>	 python3-pyasn1             noarch      0.4.8-7.fc35         fedora       134 k
>	 python3-winrm              noarch      0.4.1-4.fc35         fedora        80 k
>	
>	Transaction Summary
>	================================================================================
>	Install  14 Packages
>	
>	Total download size: 23 M
>	Installed size: 130 M
>	Is this ok [y/N]: y
>	Downloading Packages:
>	(1/14): python3-bcrypt-3.2.0-1.fc35.x86_64.rpm   61 kB/s |  43 kB     00:00    
>	(2/14): python3-jmespath-0.10.0-4.fc35.noarch.r 306 kB/s |  46 kB     00:00    
>	(3/14): python3-ntlm-auth-1.5.0-4.fc35.noarch.r 200 kB/s |  53 kB     00:00    
>	(4/14): python3-jinja2-3.0.1-2.fc35.noarch.rpm  395 kB/s | 529 kB     00:01    
>	(5/14): python3-pyasn1-0.4.8-7.fc35.noarch.rpm  287 kB/s | 134 kB     00:00    
>	(6/14): python3-pynacl-1.4.0-4.fc35.x86_64.rpm  322 kB/s | 108 kB     00:00    
>	(7/14): python3-pyyaml-5.4.1-4.fc35.x86_64.rpm  480 kB/s | 191 kB     00:00    
>	(8/14): python3-requests_ntlm-1.1.0-16.fc35.noa  44 kB/s |  18 kB     00:00    
>	(9/14): python3-winrm-0.4.1-4.fc35.noarch.rpm   125 kB/s |  80 kB     00:00    
>	(10/14): python3-xmltodict-0.12.0-13.fc35.noarc  28 kB/s |  22 kB     00:00    
>	(11/14): python3-babel-2.9.1-4.fc35.noarch.rpm  1.8 MB/s | 5.8 MB     00:03    
>	(12/14): python3-paramiko-2.9.1-1.fc35.noarch.r 521 kB/s | 295 kB     00:00    
>	(13/14): python3-pytz-2021.3-1.fc35.noarch.rpm  176 kB/s |  47 kB     00:00    
>	(14/14): ansible-2.9.27-1.fc35.noarch.rpm       2.6 MB/s |  15 MB     00:05    
>	--------------------------------------------------------------------------------
>	Total                                           1.7 MB/s |  23 MB     00:13     
>	Running transaction check
>	Transaction check succeeded.
>	Running transaction test
>	Transaction test succeeded.
>	Running transaction
>	  Preparing        :                                                        1/1 
>	  Installing       : python3-pytz-2021.3-1.fc35.noarch                     1/14 
>	  Installing       : python3-babel-2.9.1-4.fc35.noarch                     2/14 
>	  Installing       : python3-jinja2-3.0.1-2.fc35.noarch                    3/14 
>	  Installing       : python3-xmltodict-0.12.0-13.fc35.noarch               4/14 
>	  Installing       : python3-pyyaml-5.4.1-4.fc35.x86_64                    5/14 
>	  Installing       : python3-pynacl-1.4.0-4.fc35.x86_64                    6/14 
>	  Installing       : python3-pyasn1-0.4.8-7.fc35.noarch                    7/14 
>	  Installing       : python3-ntlm-auth-1.5.0-4.fc35.noarch                 8/14 
>	  Installing       : python3-requests_ntlm-1.1.0-16.fc35.noarch            9/14 
>	  Installing       : python3-winrm-0.4.1-4.fc35.noarch                    10/14 
>	  Installing       : python3-jmespath-0.10.0-4.fc35.noarch                11/14 
>	  Installing       : python3-bcrypt-3.2.0-1.fc35.x86_64                   12/14 
>	  Installing       : python3-paramiko-2.9.1-1.fc35.noarch                 13/14 
>	  Installing       : ansible-2.9.27-1.fc35.noarch                         14/14 
>	  Running scriptlet: ansible-2.9.27-1.fc35.noarch                         14/14 
>	  Verifying        : python3-babel-2.9.1-4.fc35.noarch                     1/14 
>	  Verifying        : python3-bcrypt-3.2.0-1.fc35.x86_64                    2/14 
>	  Verifying        : python3-jinja2-3.0.1-2.fc35.noarch                    3/14 
>	  Verifying        : python3-jmespath-0.10.0-4.fc35.noarch                 4/14 
>	  Verifying        : python3-ntlm-auth-1.5.0-4.fc35.noarch                 5/14 
>	  Verifying        : python3-pyasn1-0.4.8-7.fc35.noarch                    6/14 
>	  Verifying        : python3-pynacl-1.4.0-4.fc35.x86_64                    7/14 
>	  Verifying        : python3-pyyaml-5.4.1-4.fc35.x86_64                    8/14 
>	  Verifying        : python3-requests_ntlm-1.1.0-16.fc35.noarch            9/14 
>	  Verifying        : python3-winrm-0.4.1-4.fc35.noarch                    10/14 
>	  Verifying        : python3-xmltodict-0.12.0-13.fc35.noarch              11/14 
>	  Verifying        : ansible-2.9.27-1.fc35.noarch                         12/14 
>	  Verifying        : python3-paramiko-2.9.1-1.fc35.noarch                 13/14 
>	  Verifying        : python3-pytz-2021.3-1.fc35.noarch                    14/14 
>	
>	Installed:
>	  ansible-2.9.27-1.fc35.noarch                                                  
>	  python3-babel-2.9.1-4.fc35.noarch                                             
>	  python3-bcrypt-3.2.0-1.fc35.x86_64                                            
>	  python3-jinja2-3.0.1-2.fc35.noarch                                            
>	  python3-jmespath-0.10.0-4.fc35.noarch                                         
>	  python3-ntlm-auth-1.5.0-4.fc35.noarch                                         
>	  python3-paramiko-2.9.1-1.fc35.noarch                                          
>	  python3-pyasn1-0.4.8-7.fc35.noarch                                            
>	  python3-pynacl-1.4.0-4.fc35.x86_64                                            
>	  python3-pytz-2021.3-1.fc35.noarch                                             
>	  python3-pyyaml-5.4.1-4.fc35.x86_64                                            
>	  python3-requests_ntlm-1.1.0-16.fc35.noarch                                    
>	  python3-winrm-0.4.1-4.fc35.noarch                                             
>	  python3-xmltodict-0.12.0-13.fc35.noarch                                       
>	
>	Complete!

4. Создать виртуальную машину.
---

		$ egrep -v "#|^$" Vagrantfile
>	Vagrant.configure("2") do |config|
>	  config.vm.define "ubuntu" do |ubt|
>	    ubt.vm.box = "bento/ubuntu-20.04"
>	  end
>	  config.vm.define "rocky" do |rck|
>	    rck.vm.box = "bento/rockylinux-8"  
>	  end
>	 config.vm.network "private_network", type: "dhcp"
>	 config.vm.network "forwarded_port", guest: 22, host: 2222, auto_correct: true
>	 config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
>	 config.vm.network "forwarded_port", guest: 443, host: 8443, auto_correct: true
>	 config.vm.provider "virtualbox" do |v|
>	  v.memory = 1024
>	  v.cpus = 2
>	 end
>	end

		$ vagrant up rocky
>	Bringing machine 'rocky' up with 'virtualbox' provider...
>	==> rocky: Checking if box 'bento/rockylinux-8' version '202112.19.0' is up to date...
>	==> rocky: Clearing any previously set forwarded ports...
>	==> rocky: Clearing any previously set network interfaces...
>	==> rocky: Preparing network interfaces based on configuration...
>	    rocky: Adapter 1: nat
>	    rocky: Adapter 2: hostonly
>	==> rocky: Forwarding ports...
>	    rocky: 22 (guest) => 2222 (host) (adapter 1)
>	    rocky: 80 (guest) => 8080 (host) (adapter 1)
>	    rocky: 443 (guest) => 8443 (host) (adapter 1)
>	    rocky: 22 (guest) => 2222 (host) (adapter 1)
>	==> rocky: Running 'pre-boot' VM customizations...
>	==> rocky: Booting VM...
>	==> rocky: Waiting for machine to boot. This may take a few minutes...
>	    rocky: SSH address: 127.0.0.1:2222
>	    rocky: SSH username: vagrant
>	    rocky: SSH auth method: private key
>	==> rocky: Machine booted and ready!
>	==> rocky: Checking for guest additions in VM...
>	==> rocky: Configuring and enabling network interfaces...
>	==> rocky: Mounting shared folders...
>	    rocky: /vagrant => /home/v
>	==> rocky: Machine already provisioned. Run `vagrant provision` or use the `--provision`
>	==> rocky: flag to force provisioning. Provisioners marked to run always will still run.

		$ vagrant ssh rocky
>	
>	This system is built by the Bento project by Chef Software
>	More information can be found at https://github.com/chef/bento
>	Last login: Sun Jan 16 18:35:21 2022 from 10.0.2.2

		[vagrant@localhost ~]$ sudo dnf install docker
>	Rocky Linux 8 - AppStream                       1.8 kB/s | 4.8 kB     00:02    
>	Rocky Linux 8 - AppStream                       1.4 MB/s | 8.7 MB     00:06    
>	Rocky Linux 8 - BaseOS                          2.8 kB/s | 4.3 kB     00:01    
>	Rocky Linux 8 - BaseOS                          1.2 MB/s | 4.6 MB     00:03    
>	Rocky Linux 8 - Extras                          4.6 kB/s | 3.5 kB     00:00    
>	Rocky Linux 8 - Extras                          7.9 kB/s |  10 kB     00:01    
>	Hashicorp Stable - x86_64                       1.1 kB/s | 1.4 kB     00:01    
>	Hashicorp Stable - x86_64                       394 kB/s | 668 kB     00:01    
>	Dependencies resolved.
>	================================================================================
>	 Package            Arch   Version                              Repo       Size
>	================================================================================
>	Installing:
>	 podman-docker      noarch 3.3.1-9.module+el8.5.0+710+4c471e88  appstream  54 k
>	Installing dependencies:
>	 conmon             x86_64 2:2.0.29-1.module+el8.5.0+710+4c471e88
>	                                                                appstream  51 k
>	 container-selinux  noarch 2:2.167.0-1.module+el8.5.0+710+4c471e88
>	                                                                appstream  53 k
>	 containernetworking-plugins
>	                    x86_64 1.0.0-1.module+el8.5.0+710+4c471e88  appstream  19 M
>	 containers-common  noarch 2:1-2.module+el8.5.0+710+4c471e88    appstream  78 k
>	 criu               x86_64 3.15-3.module+el8.5.0+710+4c471e88   appstream 517 k
>	 fuse-common        x86_64 3.2.1-12.el8                         baseos     20 k
>	 fuse-overlayfs     x86_64 1.7.1-1.module+el8.5.0+710+4c471e88  appstream  71 k
>	 fuse3              x86_64 3.2.1-12.el8                         baseos     49 k
>	 fuse3-libs         x86_64 3.2.1-12.el8                         baseos     93 k
>	 libnet             x86_64 1.1.6-15.el8                         appstream  66 k
>	 libslirp           x86_64 4.4.0-1.module+el8.5.0+710+4c471e88  appstream  69 k
>	 podman             x86_64 3.3.1-9.module+el8.5.0+710+4c471e88  appstream  12 M
>	 podman-catatonit   x86_64 3.3.1-9.module+el8.5.0+710+4c471e88  appstream 339 k
>	 protobuf-c         x86_64 1.3.0-6.el8                          appstream  36 k
>	 runc               x86_64 1.0.2-1.module+el8.5.0+710+4c471e88  appstream 3.1 M
>	 slirp4netns        x86_64 1.1.8-1.module+el8.5.0+710+4c471e88  appstream  50 k
>	Enabling module streams:
>	 container-tools           rhel8                                               
>	
>	Transaction Summary
>	================================================================================
>	Install  17 Packages
>	
>	Total download size: 36 M
>	Installed size: 124 M
>	Is this ok [y/N]: y
>	Downloading Packages:
>	(1/17): container-selinux-2.167.0-1.module+el8.  66 kB/s |  53 kB     00:00    
>	(2/17): conmon-2.0.29-1.module+el8.5.0+710+4c47  52 kB/s |  51 kB     00:00    
>	(3/17): containers-common-1-2.module+el8.5.0+71 191 kB/s |  78 kB     00:00    
>	(4/17): fuse-overlayfs-1.7.1-1.module+el8.5.0+7 488 kB/s |  71 kB     00:00    
>	(5/17): libnet-1.1.6-15.el8.x86_64.rpm          483 kB/s |  66 kB     00:00    
>	(6/17): criu-3.15-3.module+el8.5.0+710+4c471e88 1.0 MB/s | 517 kB     00:00    
>	(7/17): libslirp-4.4.0-1.module+el8.5.0+710+4c4 522 kB/s |  69 kB     00:00    
>	(8/17): podman-catatonit-3.3.1-9.module+el8.5.0 457 kB/s | 339 kB     00:00    
>	(9/17): podman-docker-3.3.1-9.module+el8.5.0+71 147 kB/s |  54 kB     00:00    
>	(10/17): protobuf-c-1.3.0-6.el8.x86_64.rpm      319 kB/s |  36 kB     00:00    
>	(11/17): runc-1.0.2-1.module+el8.5.0+710+4c471e 2.4 MB/s | 3.1 MB     00:01    
>	(12/17): slirp4netns-1.1.8-1.module+el8.5.0+710 118 kB/s |  50 kB     00:00    
>	(13/17): fuse-common-3.2.1-12.el8.x86_64.rpm    136 kB/s |  20 kB     00:00    
>	(14/17): fuse3-3.2.1-12.el8.x86_64.rpm          236 kB/s |  49 kB     00:00    
>	(15/17): fuse3-libs-3.2.1-12.el8.x86_64.rpm     262 kB/s |  93 kB     00:00    
>	(16/17): podman-3.3.1-9.module+el8.5.0+710+4c47 1.7 MB/s |  12 MB     00:07    
>	(17/17): containernetworking-plugins-1.0.0-1.mo  26 kB/s |  19 MB     12:42    
>	--------------------------------------------------------------------------------
>	Total                                            48 kB/s |  36 MB     12:44     
>	Running transaction check
>	Transaction check succeeded.
>	Running transaction test
>	Transaction test succeeded.
>	Running transaction
>	  Preparing        :                                                        1/1 
>	  Running scriptlet: container-selinux-2:2.167.0-1.module+el8.5.0+710+4    1/17 
>	  Installing       : container-selinux-2:2.167.0-1.module+el8.5.0+710+4    1/17 
>	  Running scriptlet: container-selinux-2:2.167.0-1.module+el8.5.0+710+4    1/17 
>	  Installing       : fuse3-libs-3.2.1-12.el8.x86_64                        2/17 
>	  Running scriptlet: fuse3-libs-3.2.1-12.el8.x86_64                        2/17 
>	  Installing       : fuse-common-3.2.1-12.el8.x86_64                       3/17 
>	  Installing       : fuse3-3.2.1-12.el8.x86_64                             4/17 
>	  Installing       : fuse-overlayfs-1.7.1-1.module+el8.5.0+710+4c471e88    5/17 
>	  Running scriptlet: fuse-overlayfs-1.7.1-1.module+el8.5.0+710+4c471e88    5/17 
>	  Installing       : protobuf-c-1.3.0-6.el8.x86_64                         6/17 
>	  Installing       : libslirp-4.4.0-1.module+el8.5.0+710+4c471e88.x86_6    7/17 
>	  Installing       : slirp4netns-1.1.8-1.module+el8.5.0+710+4c471e88.x8    8/17 
>	  Installing       : libnet-1.1.6-15.el8.x86_64                            9/17 
>	  Running scriptlet: libnet-1.1.6-15.el8.x86_64                            9/17 
>	  Installing       : criu-3.15-3.module+el8.5.0+710+4c471e88.x86_64       10/17 
>	  Installing       : runc-1.0.2-1.module+el8.5.0+710+4c471e88.x86_64      11/17 
>	  Installing       : containers-common-2:1-2.module+el8.5.0+710+4c471e8   12/17 
>	  Installing       : containernetworking-plugins-1.0.0-1.module+el8.5.0   13/17 
>	  Installing       : conmon-2:2.0.29-1.module+el8.5.0+710+4c471e88.x86_   14/17 
>	  Installing       : podman-catatonit-3.3.1-9.module+el8.5.0+710+4c471e   15/17 
>	  Installing       : podman-3.3.1-9.module+el8.5.0+710+4c471e88.x86_64    16/17 
>	  Installing       : podman-docker-3.3.1-9.module+el8.5.0+710+4c471e88.   17/17 
>	  Running scriptlet: container-selinux-2:2.167.0-1.module+el8.5.0+710+4   17/17 
>	  Running scriptlet: podman-docker-3.3.1-9.module+el8.5.0+710+4c471e88.   17/17 
>	  Verifying        : conmon-2:2.0.29-1.module+el8.5.0+710+4c471e88.x86_    1/17 
>	  Verifying        : container-selinux-2:2.167.0-1.module+el8.5.0+710+4    2/17 
>	  Verifying        : containernetworking-plugins-1.0.0-1.module+el8.5.0    3/17 
>	  Verifying        : containers-common-2:1-2.module+el8.5.0+710+4c471e8    4/17 
>	  Verifying        : criu-3.15-3.module+el8.5.0+710+4c471e88.x86_64        5/17 
>	  Verifying        : fuse-overlayfs-1.7.1-1.module+el8.5.0+710+4c471e88    6/17 
>	  Verifying        : libnet-1.1.6-15.el8.x86_64                            7/17 
>	  Verifying        : libslirp-4.4.0-1.module+el8.5.0+710+4c471e88.x86_6    8/17 
>	  Verifying        : podman-3.3.1-9.module+el8.5.0+710+4c471e88.x86_64     9/17 
>	  Verifying        : podman-catatonit-3.3.1-9.module+el8.5.0+710+4c471e   10/17 
>	  Verifying        : podman-docker-3.3.1-9.module+el8.5.0+710+4c471e88.   11/17 
>	  Verifying        : protobuf-c-1.3.0-6.el8.x86_64                        12/17 
>	  Verifying        : runc-1.0.2-1.module+el8.5.0+710+4c471e88.x86_64      13/17 
>	  Verifying        : slirp4netns-1.1.8-1.module+el8.5.0+710+4c471e88.x8   14/17 
>	  Verifying        : fuse-common-3.2.1-12.el8.x86_64                      15/17 
>	  Verifying        : fuse3-3.2.1-12.el8.x86_64                            16/17 
>	  Verifying        : fuse3-libs-3.2.1-12.el8.x86_64                       17/17 
>	
>	Installed:
>	  conmon-2:2.0.29-1.module+el8.5.0+710+4c471e88.x86_64                          
>	  container-selinux-2:2.167.0-1.module+el8.5.0+710+4c471e88.noarch              
>	  containernetworking-plugins-1.0.0-1.module+el8.5.0+710+4c471e88.x86_64        
>	  containers-common-2:1-2.module+el8.5.0+710+4c471e88.noarch                    
>	  criu-3.15-3.module+el8.5.0+710+4c471e88.x86_64                                
>	  fuse-common-3.2.1-12.el8.x86_64                                               
>	  fuse-overlayfs-1.7.1-1.module+el8.5.0+710+4c471e88.x86_64                     
>	  fuse3-3.2.1-12.el8.x86_64                                                     
>	  fuse3-libs-3.2.1-12.el8.x86_64                                                
>	  libnet-1.1.6-15.el8.x86_64                                                    
>	  libslirp-4.4.0-1.module+el8.5.0+710+4c471e88.x86_64                           
>	  podman-3.3.1-9.module+el8.5.0+710+4c471e88.x86_64                             
>	  podman-catatonit-3.3.1-9.module+el8.5.0+710+4c471e88.x86_64                   
>	  podman-docker-3.3.1-9.module+el8.5.0+710+4c471e88.noarch                      
>	  protobuf-c-1.3.0-6.el8.x86_64                                                 
>	  runc-1.0.2-1.module+el8.5.0+710+4c471e88.x86_64                               
>	  slirp4netns-1.1.8-1.module+el8.5.0+710+4c471e88.x86_64                        
>	
>	Complete!

		[vagrant@localhost ~]$ docker ps
>	Emulate Docker CLI using podman. Create /etc/containers/nodocker to quiet msg.
>	CONTAINER ID  IMAGE       COMMAND     CREATED     STATUS      PORTS       NAMES

