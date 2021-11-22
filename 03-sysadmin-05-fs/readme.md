Домашнее задание к занятию "3.5. Файловые системы"
===
2. Могут ли файлы, являющиеся жесткой ссылкой на один объект, иметь разные права доступа и владельца? Почему?
---
Не могут, потому что жесткие ссылки не являются файлами, а являются элементами файловой системы, а права доступа и владелец это атрибуты файла, на который и указывают жесткие ссылки, см. *link(2)*.

3. Пересоздание виртуальной машины:
---

		$ vagrant destroy
>	    default: Are you sure you want to destroy the 'default' VM? [y/N] y
>	==> default: Forcing shutdown of VM...
>	==> default: Destroying VM and associated drives...

		$ vi Vagrantfile
		$ vagrant up

		vagrant@vagrant:~$ lsblk

>	NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT

>	sda                    8:0    0   64G  0 disk 

>	├─sda1                 8:1    0  512M  0 part /boot/efi

>	├─sda2                 8:2    0    1K  0 part 

>	└─sda5                 8:5    0 63.5G  0 part 

>	  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /

>	  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]

>	sdb                    8:16   0  2.5G  0 disk 

>	sdc                    8:32   0  2.5G  0 disk 

