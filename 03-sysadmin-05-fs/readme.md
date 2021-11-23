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
		[..]
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

4. Используя fdisk, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.
---

		$ sudo fdisk  /dev/sdb
		[..]
>	Command (m for help):  p
>	Disk /dev/sdb: 2.51 GiB, 2684354560 bytes, 5242880 sectors
>	Disk model: VBOX HARDDISK   
>	Units: sectors of 1 * 512 = 512 bytes
>	Sector size (logical/physical): 512 bytes / 512 bytes
>	I/O size (minimum/optimal): 512 bytes / 512 bytes
>	Disklabel type: dos
>	Disk identifier: 0x60f5c924
>	
>	Device     Boot   Start     End Sectors  Size Id Type
>	/dev/sdb1          2048 4196351 4194304    2G 83 Linux
>	/dev/sdb2       4196352 5242879 1046528  511M 83 Linux

