Домашнее задание к занятию "6.4. PostgreSQL"
===
1.
---
Используя docker поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume. Подключитесь к БД PostgreSQL используя psql.

Dockerfile:

		FROM postgres:13
		ENV POSTGRES_PASSWORD=password
		USER postgres
		VOLUME /var/lib/postgresql/data

		$ docker build .
		--> d2681261d62
		d2681261d62907ac551ee7f2d2622d3ac6166cba4ed377ef5232ddd9674220ad

		$ docker run -d -v "data:/var/lib/postgresql/data" d2681261d62
		a96eeaabb177cb9377b8d9d217915f9a210157b01ad79cd3883d0898531d92bb

		$ docker exec -it ccbccda3869b6  psql
		psql (13.6 (Debian 13.6-1.pgdg110+1))
		Type "help" for help.

		postgres=# 

Найдите и приведите управляющие команды для:
- вывода списка БД  
	\l  
- подключения к БД  
	\c <имя_базы>  

		postgres=# \conninfo
		You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".

- вывода списка таблиц
	\dt
- вывода описания содержимого таблиц
	\d <имя_базы>
- выхода из psql
	\q

2.
---
Используя psql создайте БД test_database.

		postgres=# CREATE DATABASE test_database;
		CREATE DATABASE

Восстановите бэкап БД в test_database.

		$ docker cp ./test_dump.sql ccbccda3869b:/tmp
		$ docker exec -it ccbccda3869b6  psql -d test_database -f /tmp/test_dump.sql

Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.

		test_database-# \dt
		         List of relations
		 Schema |  Name  | Type  |  Owner   
		--------+--------+-------+----------
		 public | orders | table | postgres
		(1 row)

		test_database=# ANALYZE VERBOSE;
		INFO:  analyzing "public.orders"
		INFO:  "orders": scanned 0 of 0 pages, containing 0 live rows and 0 dead rows; 0 rows in sample, 0 estimated total rows
		[..]

Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.

		test_database=# SELECT tablename, attname, avg_width FROM pg_stats WHERE tablename = 'orders' ORDER BY avg_width DESC;
		 tablename | attname | avg_width
		-----------+---------+-----------
		 orders    | title   |        16
		 orders    | id      |         4
		 orders    | price   |         4
		(3 rows)

3.
---
Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и поиск по ней занимает долгое время. Вам, как успешному выпускнику курсов DevOps в нетологии предложили провести разбиение таблицы на 2 (шардировать на orders_1 - price>499 и orders_2 - price<=499).

Предложите SQL-транзакцию для проведения данной операции.

BEGIN;  
CREATE TABLE orders_1 (LIKE orders);  
INSERT INTO orders_1 SELECT * FROM orders WHERE price >499;  
DELETE FROM orders WHERE price >499;  
CREATE TABLE orders_2 (LIKE orders);  
INSERT INTO orders_2 SELECT * FROM orders WHERE price <=499;  
DELETE FROM orders WHERE price <=499;  
COMMIT;  

Можно ли было изначально исключить "ручное" разбиение при проектировании таблицы orders?

 В [документации](https://www.postgresql.org/docs/10/ddl-partitioning.html) описан метод оптимизации таблиц методом разделения по диапазонам выбранного ключа (range partitioning)

4.
---
Используя утилиту pg_dump создайте бекап БД test_database.

		$ docker exec -it ccbccda3869b6  pg_dump -f /tmp/dump test_database

Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?

Согласно [документации](https://www.postgresql.org/docs/9.4/ddl-constraints.html), нужно добавить Unique Constraints на столбец title при создании таблицы

CREATE TABLE public.orders (
    id integer NOT NULL,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0,
    UNIQUE (title)
);
