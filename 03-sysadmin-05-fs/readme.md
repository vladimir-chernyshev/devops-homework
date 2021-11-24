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

4. Используя **fdisk**, разбейте первый диск на 2 раздела: 2 Гб, оставшееся пространство.
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

		$ lsblk 
>	NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
>
>sda                    8:0    0   64G  0 disk 
>
>├─sda1                 8:1    0  512M  0 part /boot/efi
>
>├─sda2                 8:2    0    1K  0 part 
>
>└─sda5                 8:5    0 63.5G  0 part 
>
>  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /
>
>  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]
>
>sdb                    8:16   0  2.5G  0 disk 
>
>├─sdb1                 8:17   0    2G  0 part 
>
>└─sdb2                 8:18   0  511M  0 part 
>
>sdc                    8:32   0  2.5G  0 disk 

5. Используя **sfdisk**, перенесите данную таблицу разделов на второй диск.
---

		$ sudo sfdisk --dump /dev/sdb | sudo sfdisk /dev/sdc 

>	Checking that no-one is using this disk right now ... OK
>
>	Disk /dev/sdc: 2.51 GiB, 2684354560 bytes, 5242880 sectors
>
>	Disk model: VBOX HARDDISK   
>
>	Units: sectors of 1 * 512 = 512 bytes
>
>	Sector size (logical/physical): 512 bytes / 512 bytes
>
>	I/O size (minimum/optimal): 512 bytes / 512 bytes
>
>	>>> Script header accepted.
>
>	>>> Script header accepted.
>
>	>>> Script header accepted.
>
>	>>> Script header accepted.
>
>	>>> Created a new DOS disklabel with disk identifier 0x60f5c924.
>
>	/dev/sdc1: Created a new partition 1 of type 'Linux' and of size 2 GiB.
>
>	/dev/sdc2: Created a new partition 2 of type 'Linux' and of size 511 MiB.
>
>	/dev/sdc3: Done.
>
>	New situation:
>
>	Disklabel type: dos
>
>	Disk identifier: 0x60f5c924
>
>	Device     Boot   Start     End Sectors  Size Id Type
>
>	/dev/sdc1          2048 4196351 4194304    2G 83 Linux
>
>	/dev/sdc2       4196352 5242879 1046528  511M 83 Linux
>
>	The partition table has been altered.
>
>	Calling ioctl() to re-read partition table.
>
>	Syncing disks.

		$ lsblk 
>	NAME                 MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT

>	sda                    8:0    0   64G  0 disk 

>	├─sda1                 8:1    0  512M  0 part /boot/efi

>	├─sda2                 8:2    0    1K  0 part 

>	└─sda5                 8:5    0 63.5G  0 part 

>	  ├─vgvagrant-root   253:0    0 62.6G  0 lvm  /

>	  └─vgvagrant-swap_1 253:1    0  980M  0 lvm  [SWAP]

>	sdb                    8:16   0  2.5G  0 disk 

>	├─sdb1                 8:17   0    2G  0 part 

>	└─sdb2                 8:18   0  511M  0 part 

>	sdc                    8:32   0  2.5G  0 disk 

>	├─sdc1                 8:33   0    2G  0 part 

>	└─sdc2                 8:34   0  511M  0 part 

6. Соберите **mdadm** RAID1 на паре разделов 2 Гб.
---

		$ sudo mdadm RAID1 --create  --level=1 --raid-device=2 /dev/sdb1 /dev/sdc1

>	mdadm: Note: this array has metadata at the start and
>
>	    may not be suitable as a boot device.  If you plan to
>
>	    store '/boot' on this device please ensure that
>
>	    your boot-loader understands md/v1.x metadata, or use
>
>	    --metadata=0.90
>
>	Continue creating array? y
>	
>	mdadm: Defaulting to version 1.2 metadata
>
>	mdadm: array /dev/md/RAID1 started.

		$ lsblk
>	NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
>
>	sda                    8:0    0   64G  0 disk  
>
>	├─sda1                 8:1    0  512M  0 part  /boot/efi
>
>	├─sda2                 8:2    0    1K  0 part  
>
>	└─sda5                 8:5    0 63.5G  0 part  
>
>	  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
>
>	  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
>
>	sdb                    8:16   0  2.5G  0 disk  
>
>	├─sdb1                 8:17   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdb2                 8:18   0  511M  0 part  
>
>	sdc                    8:32   0  2.5G  0 disk  
>
>	├─sdc1                 8:33   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdc2                 8:34   0  511M  0 part  

7.Соберите **mdadm** RAID0 на второй паре маленьких разделов.
---

		$ sudo mdadm RAID0 --create  --level=0 --raid-device=2 /dev/sdb2 /dev/sdc2

>	mdadm: Defaulting to version 1.2 metadata
>
>	mdadm: array /dev/md/RAID0 started.

		$ lsblk
>	NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
>
>	sda                    8:0    0   64G  0 disk  
>
>	├─sda1                 8:1    0  512M  0 part  /boot/efi
>
>	├─sda2                 8:2    0    1K  0 part  
>
>	└─sda5                 8:5    0 63.5G  0 part  
>
>	  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
>
>	  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
>
>	sdb                    8:16   0  2.5G  0 disk  
>
>	├─sdb1                 8:17   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdb2                 8:18   0  511M  0 part  
>
>	  └─md126              9:126  0 1018M  0 raid0 
>
>	sdc                    8:32   0  2.5G  0 disk  
>
>	├─sdc1                 8:33   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdc2                 8:34   0  511M  0 part  
>
>	  └─md126              9:126  0 1018M  0 raid0 

8. Создайте 2 независимых PV на получившихся md-устройствах.
---

		$ sudo lvm pvcreate /dev/md127
>	  Physical volume "/dev/md127" successfully created.

		$ sudo lvm pvcreate /dev/md126
>	  Physical volume "/dev/md126" successfully created.

		$ sudo lvm pvdisplay
>  --- Physical volume ---
>
>  PV Name               /dev/sda5
>
>  VG Name               vgvagrant
>
>  PV Size               <63.50 GiB / not usable 0   
>
>  Allocatable           yes (but full)
>
>  PE Size               4.00 MiB
>
>  Total PE              16255
>
>  Free PE               0
>
>  Allocated PE          16255
>
>  PV UUID               Mx3LcA-uMnN-h9yB-gC2w-qm7w-skx0-OsTz9z
>   
>
>  "/dev/md126" is a new physical volume of "1018.00 MiB"
>
>  --- NEW Physical volume ---
>
>  PV Name               /dev/md126
>
>  VG Name               
>
>  PV Size               1018.00 MiB
>
>  Allocatable           NO
>
>  PE Size               0   
>
>  Total PE              0
>
>  Free PE               0
>
>  Allocated PE          0
>
>  PV UUID               l1YeJs-GG00-kf2W-qemf-DFqf-z2cW-l1MXuF
>
>   
>  "/dev/md127" is a new physical volume of "<2.00 GiB"
>
>  --- NEW Physical volume ---
>
>  PV Name               /dev/md127
>
>  VG Name               
>
>  PV Size               <2.00 GiB
>
>  Allocatable           NO
>
>  PE Size               0   
>
>  Total PE              0
>
>  Free PE               0
>
>  Allocated PE          0
>
>  PV UUID               V8ZIvu-w3sB-J0fR-jeaX-XMzh-cTQJ-KKeN0W
   
9. Создайте общую volume-group на этих двух PV.
---

		$ sudo vgcreate vg /dev/md127 /dev/md126 
>  Volume group "vg" successfully created

		$ sudo lvm vgs
>  VG        #PV #LV #SN Attr   VSize   VFree 
>  vg          2   0   0 wz--n-  <2.99g <2.99g

10. Создайте LV размером 100 Мб, указав его расположение на PV с RAID0.
---

		$ sudo lvcreate --size 100M vg /dev/md126
>	  Logical volume "lvol0" created.

		$ sudo lvdisplay 
>	  --- Logical volume ---
>  LV Path                /dev/vg/lvol0
>
>  LV Name                lvol0
>
>  VG Name                vg
>
>  LV UUID                RTIcx2-WB0t-GrWq-nesj-sayF-yA9m-gOHLE6
>
>  LV Write Access        read/write
>
>  LV Creation host, time vagrant, 2021-11-24 20:12:13 +0000
>
>  LV Status              available
>
>  # open                 0
>
>  LV Size                100.00 MiB
>
>  Current LE             25
>
>  Segments               1
>
>  Allocation             inherit
>
>  Read ahead sectors     auto
>
>  - currently set to     4096
>
>  Block device           253:2

11. Создайте mkfs.ext4 ФС на получившемся LV.
---

		$ sudo mkfs.ext4 /dev/vg/lvol0
>	mke2fs 1.45.5 (07-Jan-2020)
>	Creating filesystem with 25600 4k blocks and 25600 inodes
>
>	Allocating group tables: done                            
>	Writing inode tables: done                            
>	Creating journal (1024 blocks): done
>	Writing superblocks and filesystem accounting information: done

12. Смонтируйте этот раздел в любую директорию, например, /tmp/new.
---

		$ mkdir /tmp/new
		$ sudo mount /dev/vg/lvol0 /tmp/new/

13. Поместите туда тестовый файл, например wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
---

		$ sudo wget https://mirror.yandex.ru/ubuntu/ls-lR.gz -O /tmp/new/test.gz
>	--2021-11-24 20:25:12--  https://mirror.yandex.ru/ubuntu/ls-lR.gz
>
>	Resolving mirror.yandex.ru (mirror.yandex.ru)... 213.180.204.183, 2a02:6b8::183
>
>	Connecting to mirror.yandex.ru (mirror.yandex.ru)|213.180.204.183|:443... connected.
>
>	HTTP request sent, awaiting response... 200 OK
>
>	Length: 22565143 (22M) [application/octet-stream]
>
>	Saving to: ‘/tmp/new/test.gz’
>
>
>
>	/tmp/new/test.gz    100%[==================>]  21.52M  3.37MB/s    in 7.6s    
>
>
>	2021-11-24 20:25:21 (2.85 MB/s) - ‘/tmp/new/test.gz’ saved [22565143/22565143]

14. Прикрепите вывод **lsblk**.
---

		$ lsblk
>	NAME                 MAJ:MIN RM  SIZE RO TYPE  MOUNTPOINT
>
>	sda                    8:0    0   64G  0 disk  
>	├─sda1                 8:1    0  512M  0 part  /boot/efi
>
>	├─sda2                 8:2    0    1K  0 part  
>
>	└─sda5                 8:5    0 63.5G  0 part  
>
>	  ├─vgvagrant-root   253:0    0 62.6G  0 lvm   /
>
>	  └─vgvagrant-swap_1 253:1    0  980M  0 lvm   [SWAP]
>
>	sdb                    8:16   0  2.5G  0 disk  
>
>	├─sdb1                 8:17   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdb2                 8:18   0  511M  0 part  
>
>	  └─md126              9:126  0 1018M  0 raid0 
>
>	    └─vg-lvol0       253:2    0  100M  0 lvm   /tmp/new
>
>	sdc                    8:32   0  2.5G  0 disk  
>
>	├─sdc1                 8:33   0    2G  0 part  
>
>	│ └─md127              9:127  0    2G  0 raid1 
>
>	└─sdc2                 8:34   0  511M  0 part  
>
>	  └─md126              9:126  0 1018M  0 raid0 
>
>	    └─vg-lvol0       253:2    0  100M  0 lvm   /tmp/new
>

15. Протестируйте целостность файла:
---

		$ gzip -t /tmp/new/test.gz
		$ echo $?
		0

16. Используя **pvmove**, переместите содержимое PV с RAID0 на RAID1.
---

		$ sudo pvmove --name lvol0 /dev/md126 /dev/md127  
		  /dev/md126: Moved: 72.00%

17. Сделайте --fail на устройство в вашем RAID1 md.
---

		$ sudo mdadm /dev/md127 --fail /dev/sdb1
		mdadm: set /dev/sdb1 faulty in /dev/md127

18. Подтвердите выводом **dmesg**, что RAID1 работает в деградированном состоянии.
---

		$ dmesg
		md/raid1:md127: Disk failure on sdb1, disabling device.
		md/raid1:md127: Operation continuing on 1 devices

19. Протестируйте целостность файла, несмотря на "сбойный" диск он должен продолжать быть доступен:
---

		$ gzip -t /tmp/new/test.gz
		$ echo $?
		0
