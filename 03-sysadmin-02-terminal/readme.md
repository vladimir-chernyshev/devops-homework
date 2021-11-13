Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"
===
1.Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.
---

    $ type cd
    cd is a shell builtin
    
Команда **cd** это встроенная в **bash** команда, вероятно, чтобы экономить на создании отдельного процесса для выполнения этой команды.

2.Какая альтернатива без pipe команде **grep** *<some_string> <some_file>* **| wc -l**?
---
**grep(1)**:
> -c, --count  
>              Suppress  normal output; instead print a count of matching lines
>              for each input file.  With the -v,  --invert-match  option  (see
>              below), count non-matching lines.

3.Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?
---

        $ ps 1
        PID TTY      STAT   TIME COMMAND
        1 ?        Ss     0:06 /sbin/init
      
**systemd(1)** это.

4. Как будет выглядеть команда, которая перенаправит вывод stderr ls на другую сессию терминала?
---
[Google-fu](https://unix.stackexchange.com/questions/261531/how-to-send-output-from-one-terminal-to-another-without-making-any-new-pipe-or-f):

        $ who
        vagrant  pts/0        2021-11-13 01:00 (10.0.2.2)
        vagrant  pts/1        2021-11-13 01:21 (10.0.2.2)
        $ who am i
        vagrant  pts/0        2021-11-13 01:00 (10.0.2.2)

Команда будет выглядеть следующим образом:

        $ ls xxx 2>/dev/pts/1
        
5.Получится ли одновременно передать команде файл на stdin и вывести ее stdout в другой файл? Приведите работающий пример.
---

        $ echo test > test
        $ cat <./test >test.out
        $ cat test.out
        test

6. Получится ли вывести находясь в графическом режиме данные из PTY в какой-либо из эмуляторов TTY? Сможете ли вы наблюдать выводимые данные?
---
7.Выполните команду bash 5>&1. К чему она приведет? Что будет, если вы выполните echo netology > /proc/$$/fd/5? Почему так происходит?
---

        $ bash 5>&1
        $ echo netology > /proc/$$/fd/5
        netology
        vagrant@vagrant:~$ echo $$
        12864
        $ ps
            PID TTY          TIME CMD
           3549 pts/0    00:00:00 bash
          12864 pts/0    00:00:00 bash
          12870 pts/0    00:00:00 ps

Команда **bash 5>&1** запустит оболочку с перенаправлением потока ввода-вывода с файловым дескриптором 5 в стандартный поток вывода. В переменной $$ хранится PID текущей оболочки, поэтому вторая команда выводит строку "netology" в поток с дескриптором 5 текущей оболочки, который, в свою очередь, перенаправлен в поток стандартного вывода, который связан с текущим терминалом.

8. Получится ли в качестве входного потока для pipe использовать только stderr команды, не потеряв при этом отображение stdout на pty? 
---
[Google-fu](https://stackoverflow.com/questions/2342826/how-can-i-pipe-stderr-and-not-stdout): 

        $ who am i
        vagrant  pts/1        2021-11-13 01:21 (10.0.2.2)
        $ find / -name ls 2>&1 1>/dev/pts/1 | cat > err
        /usr/lib/klibc/bin/ls
        /usr/bin/ls
        $ head err
        find: ‘/proc/tty/driver’: Permission denied
        find: ‘/proc/1/task/1/fd’: Permission denied
        find: ‘/proc/1/task/1/fdinfo’: Permission denied
        [..]

9.Что выведет команда cat /proc/$$/environ? Как еще можно получить аналогичный по содержанию вывод?
---
Команда выведет переменные окружения текущей оболочки. Аналогичный по содержанию вывод выдаст встроенная команда оболочки **set** без параметров.

10. Используя man, опишите что доступно по адресам /proc/<PID>/cmdline, /proc/<PID>/exe.
---
**proc(5)**:
> /proc/[pid]/cmdline
>              This  read-only  file  holds  the  complete command line for the
>              process..     
    
> /proc/[pid]/exe
>              Under Linux 2.2 and later, this file is a symbolic link contain‐
>              ing the actual pathname of the executed command. 
    
11. Узнайте, какую наиболее старшую версию набора инструкций SSE поддерживает ваш процессор с помощью /proc/cpuinfo.
---
        $cat /proc/cpuinfo | egrep sse
        flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl          xtopology nonstop_tsc cpuid tsc_known_freq pni pclmulqdq ssse3 cx16 sse4_1 sse4_2 x2apic movbe popcnt aes rdrand hypervisor lahf_lm 3dnowprefetch pti
    
Самая старшая версия SSE 4.2
