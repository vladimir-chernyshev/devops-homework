Домашнее задание к занятию "3.2. Работа в терминале, лекция 2"
===
1.Какого типа команда cd? Попробуйте объяснить, почему она именно такого типа; опишите ход своих мыслей, если считаете что она могла бы быть другого типа.
---

    $ type cd
    cd is a shell builtin
    
Команда **cd** это встроенная в **bash** команда, вероятно, чтобы экономить на создании отдельного процесса для выполнения этой команды.

2.Какая альтернатива без pipe команде **grep** *<some_string> <some_file>* **| wc -l**?
**grep(1)**:
> -c, --count
>              Suppress  normal output; instead print a count of matching lines
>              for each input file.  With the -v,  --invert-match  option  (see
>              below), count non-matching lines.

3.Какой процесс с PID 1 является родителем для всех процессов в вашей виртуальной машине Ubuntu 20.04?

    $ ps 1
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:06 /sbin/init
      
**systemd(1)** это.

4. Как будет выглядеть команда, которая перенаправит вывод stderr ls на другую сессию терминала?
