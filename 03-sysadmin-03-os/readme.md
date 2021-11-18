Домашнее задание к занятию "3.3. Операционные системы, лекция 1
===
1. Какой системный вызов делает команда **cd**?
---

		$ strace  /bin/bash -c 'cd /tmp'
		[..]
		chdir("/tmp")
		[..]

2. Используя **strace** выясните, где находится база данных **file** на основании которой она делает свои догадки.
---

		$ strace file .bashrc 
		[..]
		stat("/home/vagrant/.magic.mgc", 0x7ffca6751170) = -1 ENOENT (No such file or directory)
i		stat("/home/vagrant/.magic", 0x7ffca6751170) = -1 ENOENT (No such file or directory)
		openat(AT_FDCWD, "/etc/magic.mgc", O_RDONLY) = -1 ENOENT (No such file or directory)
		stat("/etc/magic", {st_mode=S_IFREG|0644, st_size=111, ...}) = 0
		openat(AT_FDCWD, "/etc/magic", O_RDONLY) = 3
		openat(AT_FDCWD, "/usr/share/misc/magic.mgc", O_RDONLY) = 3

**file** попробовал открыть файлы *~/.magic.mgc*, *~/.magic*, */etc/magic.mgc*, открыл и прочитал файлы */etc/magic*, */usr/share/misc/magic.mgc*

3. Основываясь на знаниях о перенаправлении потоков предложите способ обнуления открытого удаленного файла (чтобы освободить место на файловой системе).
---
[Google-fu](https://stackoverflow.com/questions/980283/truncating-a-file-while-its-being-used-linux):

		$  cat > tmp
		1234567890

Не завершая процесс **cat**, в другой консоли найдем его PID и посмотрим вывод **lsof**:

		$ ps u|egrep cat
		v          15196  0.0  0.0 221088   996 pts/2    S+   20:08   0:00 cat
		$lsof -p 15196
		COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
		[..]
		cat     15196    v    1w   REG   0,34       11 332796 /home/v/tmp

Размер открытого на запись файла 11 байт (символы 0-9 и перевод строки), номер дескриптора 1.

		$cp /dev/null /proc/15196/fd/1
		$lsof -p 15196
                COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
                [..]
		cat     15196    v    1w   REG   0,34        0 332796 /home/v/tmp

Размер файла стал 0 байт.

4. Занимают ли зомби-процессы какие-то ресурсы в ОС (CPU, RAM, IO)?
---
 Исходя из написанного в [Wikipedia](https://en.wikipedia.org/wiki/Zombie_process), процессы-зомби потребляют только один ресурс - запиcь в таблице процессов и в неблагоприятном случае могут привести к исчерпанию PID.

5. В iovisor BCC есть утилита **opensnoop**.  На какие файлы вы увидели вызовы группы open за первую секунду работы утилиты? 
---

		# /usr/sbin/opensnoop-bpfcc -d 1
		PID    COMM               FD ERR PATH
		778    vminfo              6   0 /var/run/utmp
		589    dbus-daemon        -1   2 /usr/local/share/dbus-1/system-services
		589    dbus-daemon        18   0 /usr/share/dbus-1/system-services
		589    dbus-daemon        -1   2 /lib/dbus-1/system-services
		589    dbus-daemon        18   0 /var/lib/snapd/dbus-1/system-services/

6. Какой системный вызов использует **uname -a**? Приведите цитату из **man** по этому системному вызову, где описывается альтернативное местоположение в /proc, где можно узнать версию ядра и релиз ОС.
---

		$ strace uname -a
		[..]
		uname({sysname="Linux", nodename="vagrant", ...}) = 0

*uname(2)*:

>Part of the [struct] *utsname* information is also accessible  via  */proc/sys/kernel/{ostype, hostname, osrelease, version, domainname}*.

7. Чем отличается последовательность команд через *;* и через *&&* в **bash**?
---
**bash(1)**:

>Commands separated by a *;* are executed sequentially; the shell waits for each command to terminate in turn.  The return status is the exit status of the last command executed.
>AND and OR lists are sequences of one or more pipelines separated by the *&&* and *||* control operators, respectively.  AND and OR lists are executed with left  associativity.
>      An AND list has the form
>
>              command1 && command2
>
>       command2 is executed if, and only if, command1 returns an exit status of zero (success).
>
>       An OR list has the form
>
>              command1 || command2
>
>       command2 is executed if, and only if, command1 returns a non-zero exit status.  The return status of AND and OR lists is the exit status of the last command executed in the list.

 Команды, разделенные символом *;*, выполняются последовательно и независимо от значения кода выполнения предыдущей.
 Вторая команда из последовательности, разделенной *&&*, будет выполняться только в случае, если код выполнения первой "0" (успешное выполнение).
 Вторая команда из последовательности, разделенной *||*, будет выполняться только в случае, если код выполнения первой не "0".

Есть ли смысл использовать в **bash** *&&*, если применить **set -e**?
---
**bash(1)**:

>set -e
>			Exit immediately if a list exits with a non-zero  sta‐
>                      tus.   The  shell  does  not  exit if the command that
>                      fails is part of any command executed in a && or || list
>			except the command following the final && or ||

При включении **set -e** командная оболочка завершит свою работу если список команд завершится с ненулевым кодом выполнения, за исключением случая, когда с ненулевым кодом выполнения завершится предпоследняя команда в списке:


		$ vagrant ssh
		vagrant@vagrant:~$ false && true
		vagrant@vagrant:~$ echo $?
		1
		vagrant@vagrant:~$ set -e
		vagrant@vagrant:~$ false && true
		vagrant@vagrant:~$ echo $?
		1

		$ vagrant ssh
		vagrant@vagrant:~$ true && false
		vagrant@vagrant:~$ echo $?
		1
		vagrant@vagrant:~$ set -e
		vagrant@vagrant:~$ true && false
		Connection to 127.0.0.1 closed.


Из вывода команд видно, что, хотя во втором случае оболочка завершила свое выполнение, условие выполнения второй команды списка в зависимости от кода выполнения первой не изменилось - следовательно, *&&*-список можно использовать и при включенной опции **set -e**.

8. Из каких опций состоит режим bash set -euxo pipefail и почему его хорошо было бы использовать в сценариях?
---
**bash(1)** [cм.](https://explainshell.com/explain?cmd=set+-euxo+pipefail):

>SHELL BUILTIN COMMANDS
>set
>	-e:	 завершить выполнение командной оболочки, если последняя команда в *pipeline* завершится с ненулевым кодом выполнения;
>	-o pipefail: код выполнения всего pipe принимается равным коду выполнения последней в pipe команды, если ненулевой, причем в этом случае оболочка завершает свою работу, или принимается равным "0", если все команды в pipe выполнились успешно
>	-x:	включение отладки, вывод скрипта построчно со всемы выполненными подстановками и расширениями переменных
>	-u:	выводить сообщение об ошибке каждый раз, когда используется не объявленная ранее переменная

По всей видимости, данный режим полезен при отладке сценариев.

9. Используя *-o stat* для **ps**, определите, какой наиболее часто встречающийся статус у процессов в системе. Его можно не учитывать при расчете (считать S, Ss или Ssl равнозначными).
---

		$ ps -eo stat= | cut -b 1 | sort | uniq -c
		     48 I
		      1 R
		     51 S

или

		$ ps -eo state= | sort | uniq -c
		     48 I
		      2 R
		     51 S

Больше всего в системе процессов в состоянии прерываемого сна:

**ps(1)**:
>               D    uninterruptible sleep (usually IO)
>               I    Idle kernel thread
>               R    running or runnable (on run queue)
>               S    interruptible sleep (waiting for an event to complete)
>               T    stopped by job control signal
>               t    stopped by debugger during the tracing
>               W    paging (not valid since the 2.6.xx kernel)
>               X    dead (should never be seen)
>               Z    defunct ("zombie") process, terminated but not reaped by
                    its parent

