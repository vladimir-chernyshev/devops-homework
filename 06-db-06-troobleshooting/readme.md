Домашнее задание к занятию "6.6. Troubleshooting"
===

1.
---
Пользователь (разработчик) написал в канал поддержки, что у него уже 3 минуты происходит CRUD операция в MongoDB и её нужно прервать.

Вы как инженер поддержки решили произвести данную операцию:

- напишите список операций, которые вы будете производить для остановки запроса пользователя

Поиск операций, время выполнения которых превысило 3 минуты (180 сек):

		db.currentOp().inprog.forEach(
		  function(op) {
		    if(op.secs_running > 180) printjson(op);
		  }
		)

Принудительное завершение транзакции:

		db.killOp(<opid>)

- предложите вариант решения проблемы с долгими (зависающими) запросами в MongoDB
 Согласно [документации](https://docs.mongodb.com/manual/tutorial/terminate-running-operations/), MongoDB предлагает метод maxTimeMS() для задания лимита выполнения операции.

2.
---
Вы запустили инстанс Redis для использования совместно с сервисом, который использует механизм TTL. Причем отношение количества записанных key-value значений к количеству истёкших значений есть величина постоянная и увеличивается пропорционально количеству реплик сервиса.
При масштабировании сервиса до N реплик вы увидели, что:
- сначала рост отношения записанных значений к истекшим
- Redis блокирует операции записи
Как вы думаете, в чем может быть проблема?

Согласно [документации](https://redis.io/topics/latency), блокировка записи может быть вызвана процессом сброса буфера записи на диск:

Latency due to AOF and disk I/O

"Another source of latency is due to the Append Only File support on Redis. The AOF basically uses two system calls to accomplish its work. One is write(2) that is used in order to write data to the append only file, and the other one is fdatasync(2) that is used in order to flush the kernel file buffer on disk in order to ensure the durability level specified by the user."

3.
---
Вы подняли базу данных MySQL для использования в гис-системе. При росте количества записей, в таблицах базы, пользователи начали жаловаться на ошибки вида:

InterfaceError: (InterfaceError) 2013: Lost connection to MySQL server during query u'SELECT..... '

Как вы думаете, почему это начало происходить и как локализовать проблему?

Какие пути решения данной проблемы вы можете предложить?

Согласно [документации](https://dev.mysql.com/doc/refman/8.0/en/error-lost-connection.html), подобное сообщение может появиться при выборке таблицы с очень большим количеством строк. Предложенное решение - увеличение значения параметра net_read_timeout

"Sometimes the “during query” form happens when millions of rows are being sent as part of one or more queries. If you know that this is happening, you should try increasing net_read_timeout from its default of 30 seconds to 60 seconds or longer, sufficient for the data transfer to complete. "

4.
---
После запуска пользователи начали жаловаться, что СУБД время от времени становится недоступной. В dmesg вы видите, что:

postmaster invoked oom-killer

Как вы думаете, что происходит?
Как бы вы решили данную проблему?

Согласно [блога Percona](https://www.percona.com/blog/2020/06/05/10-common-postgresql-errors/), процесс СУБД был прекращен из-за превышения имеющегося количества памяти процессом ядра OOM-killer. В этом сообщении [блога Percona](https://www.percona.com/blog/2019/08/02/out-of-memory-killer-or-savior/) приводится развернутое объяснение проблемы и предложены методы решения, например, модифицировать параметр процесса СУБД oom_score_adj

"If you really want your process not to be killed by OOM-Killer, then there is another kernel parameter oom_score_adj. You can add a big negative value to that to reduce the chance your process gets killed."
