Домашнее задание к занятию "6.3. MySQL"
===

1.
---

 Используя docker поднимите инстанс MySQL (версию 8). Данные БД сохраните в volume.

Файл docker-compose.yml:
		volumes:
		  db:

		services:
		  mysql:
		    image: mysql:8
		    restart: always
		    environment:
		      MYSQL_ROOT_PASSWORD: password
		    volumes:
		      - db:/var/lib/mysql

		  adminer:
		    image: adminer
		    restart: always
		    ports:
		      - 8080:8080

Изучите бэкап БД и восстановитесь из него.

Копируем дамп в контейнер:

		docker cp test_dump.sql ae6e135a7fae:/var/tmp/test_dump.sql
		docker exec -it ae6e135a7fae sh
		mysql -uroot -p"password"

Создаем базу-приемник бэкапа

		CREATE DATABASE test_db;

Восстановление бэкапа

		$mysql -uroot -p"password" test_db < /var/tmp/test_dump.sql

 Найдите команду для выдачи статуса БД и приведите в ответе из ее вывода версию сервера БД.

		mysql> \s
		--------------
		mysql  Ver 8.0.28 for Linux on x86_64 (MySQL Community Server - GPL)
		
		Connection id:		31
		Current database:
		Current user:		root@localhost
		SSL:			Not in use
		Current pager:		stdout
		Using outfile:		''
		Using delimiter:	;
		Server version:		8.0.28 MySQL Community Server - GPL
		Protocol version:	10
		Connection:		Localhost via UNIX socket
		Server characterset:	utf8mb4
		Db     characterset:	utf8mb4
		Client characterset:	latin1
		Conn.  characterset:	latin1
		UNIX socket:		/var/run/mysqld/mysqld.sock
		Binary data as:		Hexadecimal
		Uptime:			32 min 50 sec

Подключитесь к восстановленной БД и получите список таблиц из этой БД.

		mysql> USE test_db;
		mysql> SHOW TABLES;
		+------------------+
		| Tables_in_test_db |
		+-------------------+
		| orders            |
		+-------------------+
		1 row in set (0.01 sec)

Приведите в ответе количество записей с price > 300.

		mysql> SELECT * FROM orders WHERE price > 300;
		+----+----------------+-------+
		| id | title          | price |
		+----+----------------+-------+
		|  2 | My little pony |   500 |
		+----+----------------+-------+
		1 row in set (0.01 sec)

2.
---

Создайте пользователя test в БД c паролем test-pass, используя:
 - плагин авторизации mysql_native_password
 - срок истечения пароля - 180 дней
 - количество попыток авторизации - 3
 - максимальное количество запросов в час - 100
 - аттрибуты пользователя:
   - Фамилия "Pretty"
   - Имя "James"

		mysql> CREATE USER
		    ->   'test'@'localhost' IDENTIFIED WITH mysql_native_password BY 'test-pass'
		    ->   REQUIRE NONE WITH MAX_QUERIES_PER_HOUR 100
		    ->   PASSWORD EXPIRE INTERVAL 180 DAY
		    ->   FAILED_LOGIN_ATTEMPTS 3
		    ->   ACCOUNT LOCK;
		Query OK, 0 rows affected (0.01 sec)

Предоставьте привелегии пользователю test на операции SELECT базы test_db.

		mysql> GRANT SELECT ON test_db.* TO 'test'@'localhost';
		Query OK, 0 rows affected, 1 warning (0.01 sec)

Используя таблицу INFORMATION_SCHEMA.USER_ATTRIBUTES получите данные по пользователю test и приведите в ответе к задаче.

		mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES WHERE user='test';
		+------+-----------+---------------------------------------+
		| USER | HOST      | ATTRIBUTE                             |
		+------+-----------+---------------------------------------+
		| test | localhost | {"fname": "James", "lname": "Pretty"} |
		+------+-----------+---------------------------------------+
		1 row in set (0.00 sec)

3.
---

Установите профилирование SET profiling = 1.

		mysql> SET profiling = 1;
		Query OK, 0 rows affected, 1 warning (0.00 sec)

Изучите вывод профилирования команд SHOW PROFILES;.

		mysql> SHOW PROFILES;
		+----------+------------+---------------------------------------------------------+
		| Query_ID | Duration   | Query                                                   |
		+----------+------------+---------------------------------------------------------+
		|        1 | 0.00037625 | mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES |
		|        2 | 0.00878975 | SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES        |
		|        3 | 0.00180375 | SELECT * FROM orders WHERE price > 300                  |
		+----------+------------+---------------------------------------------------------+
		3 rows in set, 1 warning (0.00 sec)

Исследуйте, какой engine используется в таблице БД test_db и приведите в ответе.

		mysql> SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'test_db';
		+------------+--------+
		| TABLE_NAME | ENGINE |
		+------------+--------+
		| orders     | InnoDB |
		+------------+--------+
		1 row in set (0.01 sec)

Измените engine и приведите время выполнения и запрос на изменения из профайлера в ответе:
 - на MyISAM
 - на InnoDB

		mysql> ALTER TABLE orders ENGINE=MyISAM;
		Query OK, 5 rows affected (0.35 sec)
		Records: 5  Duplicates: 0  Warnings: 0

		mysql> ALTER TABLE orders ENGINE=InnoDB;
		Query OK, 5 rows affected (0.30 sec)
		Records: 5  Duplicates: 0  Warnings: 0

		mysql> SHOW PROFILES;
		+----------+------------+-----------------------------------------------------------------------------------------+
		| Query_ID | Duration   | Query                                                                                   |
		+----------+------------+-----------------------------------------------------------------------------------------+
		|        1 | 0.00037625 | mysql> SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES                                 |
		|        2 | 0.00878975 | SELECT * FROM INFORMATION_SCHEMA.USER_ATTRIBUTES                                        |
		|        3 | 0.00180375 | SELECT * FROM orders WHERE price > 300                                                  |
		|        4 | 0.01050600 | SELECT TABLE_NAME, ENGINE FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'test_db' |
		|        5 | 0.28242400 | ALTER TABLE orders ENGINE=MyISAM                                                        |
		|        6 | 0.36804400 | ALTER TABLE orders ENGINE=InnoDB                                                        |
		+----------+------------+-----------------------------------------------------------------------------------------+
		6 rows in set, 1 warning (0.00 sec)

4.
---

Изучите файл my.cnf в директории /etc/mysql. Измените его согласно ТЗ (движок InnoDB):

    Скорость IO важнее сохранности данных
    Нужна компрессия таблиц для экономии места на диске
    Размер буффера с незакомиченными транзакциями 1 Мб
    Буффер кеширования 30% от ОЗУ
    Размер файла логов операций 100 Мб

Приведите в ответе измененный файл my.cnf.

		[mysqld]
		pid-file        = /var/run/mysqld/mysqld.pid
		socket          = /var/run/mysqld/mysqld.sock
		datadir         = /var/lib/mysql
		secure-file-priv= NULL

		innodb_buffer_pool_size     = 3068M
		innodb_log_file_size        = 100M
		innodb_log_buffer_size      = 1M
		innodb_file_per_table       = 1
		innodb_flush_log_at_trx_commit  = 2
