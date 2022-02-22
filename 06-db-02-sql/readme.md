Домашнее задание к занятию "6.2. SQL"
===
1. Используя docker поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы.
---

		$ docker  run -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_PASSWORD=password --mount=type=volume,src=vol1,dst=/home/vol1 --mount=type=volume,src=vol2,dst=/home/vol2 -d docker.io/library/postgres:12-alpine
8a37f863a8f720342c32f4ba402924b98767a213017ddc37ecf971af8b4d4d42
		$ docker exec -itu postgres 8a37f863a8f720342c32f4ba402924b98767a213017ddc37ecf971af8b4d4d42  psql
		psql (12.10)
		Type "help" for help.
		
		postgres=# 

2. В БД из задачи 1:
---

 - создайте пользователя test-admin-user и БД test_db  
		postgres=# create database test_db;
		CREATE DATABASE
		postgres=# create user test_admin_user;
		CREATE ROLE
 - в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже)

		postgres=# CREATE TABLE orders ( id SERIAL PRIMARY KEY, наименование TEXT,  цена INT );
		CREATE TABLE
		postgres=# 
		postgres=# CREATE TABLE clients(
		postgres(#   id SERIAL PRIMARY KEY,
		postgres(#   фамилия TEXT,
		postgres(#   страна_проживания TEXT,
		postgres(#   заказ INT,
		postgres(#   CONSTRAINT fk_orders
		postgres(#     FOREIGN KEY (заказ)
		postgres(#     REFERENCES orders (id)
		postgres(# );
		CREATE TABLE
		postgres=# CREATE INDEX страна_проживания_idx ON clients(страна_проживания);
		CREATE INDEX

 - предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db
		postgres=# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO test_admin_user;
		GRANT
 - создайте пользователя test-simple-user
		postgres=# CREATE USER test_simple_user ;
		CREATE ROLE
 - предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE данных таблиц БД test_db
		postgres=# GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO test_simple_user;
		GRANT

Приведите:

 - итоговый список БД после выполнения пунктов выше
		postgres=# SELECT datname FROM pg_database;
		  datname  
		-----------
		 postgres
		 test_db
		 template1
		 template0
		(4 rows)

 - описание таблиц 
		postgres=# \d orders
		                               Table "public.orders"
		    Column    |  Type   | Collation | Nullable |              Default               
		--------------+---------+-----------+----------+------------------------------------
		 id           | integer |           | not null | nextval('orders_id_seq'::regclass)
		 наименование | text    |           |          | 
		 цена         | integer |           |          | 
		Indexes:
		    "orders_pkey" PRIMARY KEY, btree (id)
		Referenced by:
		    TABLE "clients" CONSTRAINT "fk_orders" FOREIGN KEY ("заказ") REFERENCES orders(id)

		postgres=# \d clients
		                                  Table "public.clients"
		      Column       |  Type   | Collation | Nullable |               Default               
		-------------------+---------+-----------+----------+-------------------------------------
		 id                | integer |           | not null | nextval('clients_id_seq'::regclass)
		 фамилия           | text    |           |          | 
		 страна_проживания | text    |           |          | 
		 заказ             | integer |           |          | 
		Indexes:
		    "clients_pkey" PRIMARY KEY, btree (id)
		    "страна_проживания_idx" btree ("страна_проживания")
		Foreign-key constraints:
		    "fk_orders" FOREIGN KEY ("заказ") REFERENCES orders(id)

 - 

    SQL-запрос для выдачи списка пользователей с правами над таблицами test_db

		SELECT * from information_schema.table_privileges WHERE grantee LIKE 'test%';

 - список пользователей с правами над таблицами test_db

		postgres=# SELECT * from information_schema.table_privileges WHERE grantee LIKE 'test%';
		 grantor  |     grantee      | table_catalog | table_schema | table_name | privilege_type | is_grantable | with_hierarchy 
		----------+------------------+---------------+--------------+------------+----------------+--------------+----------------
		 postgres | test_admin_user  | postgres      | public       | orders     | INSERT         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | orders     | SELECT         | NO           | YES
		 postgres | test_admin_user  | postgres      | public       | orders     | UPDATE         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | orders     | DELETE         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | orders     | TRUNCATE       | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | orders     | REFERENCES     | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | orders     | TRIGGER        | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | INSERT         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | SELECT         | NO           | YES
		 postgres | test_admin_user  | postgres      | public       | clients    | UPDATE         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | DELETE         | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | TRUNCATE       | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | REFERENCES     | NO           | NO
		 postgres | test_admin_user  | postgres      | public       | clients    | TRIGGER        | NO           | NO
		 postgres | test_simple_user | postgres      | public       | orders     | INSERT         | NO           | NO
		 postgres | test_simple_user | postgres      | public       | orders     | SELECT         | NO           | YES
		 postgres | test_simple_user | postgres      | public       | orders     | UPDATE         | NO           | NO
		 postgres | test_simple_user | postgres      | public       | orders     | DELETE         | NO           | NO
		 postgres | test_simple_user | postgres      | public       | clients    | INSERT         | NO           | NO
		 postgres | test_simple_user | postgres      | public       | clients    | SELECT         | NO           | YES
		 postgres | test_simple_user | postgres      | public       | clients    | UPDATE         | NO           | NO
		 postgres | test_simple_user | postgres      | public       | clients    | DELETE         | NO           | NO
		(22 rows)

3. Используя SQL синтаксис - наполните таблицы следующими тестовыми данными:
---

		postgres=# INSERT INTO orders (наименование, цена)
		postgres-#   VALUES
		postgres-#   ('Шоколад', 10),
		postgres-#   ('Принтер', 3000),
		postgres-#   ('Книга',   500),
		postgres-#   ('Монитор', 7000),
		postgres-#   ('Гитара',  4000);
		INSERT 0 5

		postgres=# INSERT INTO clients (фамилия, страна_проживания)
		postgres-#   VALUES
		postgres-#   ('Иванов Иван Иванович', 'USA'),
		postgres-#   ('Петров Петр Петрович', 'Canada'),
		postgres-#   ('Иоганн Себастьян Бах', 'Japan'),
		postgres-#   ('Ронни Джеймс Дио', 'Russia'),
		postgres-#   ('Ritchie Blackmore', 'Russia');
		INSERT 0 5

вычислите количество записей для каждой таблицы:

		postgres=#  SELECT COUNT(id) FROM orders;
		 count 
		-------
		     5
		(1 row)

		postgres=# SELECT COUNT(id) FROM clients;
		 count 
		-------
		     5
		(1 row)

4. Часть пользователей из таблицы clients решили оформить заказы из таблицы orders. Используя foreign keys свяжите записи из таблиц
---

		postgres=# \c test_db
		You are now connected to database "test_db" as user "postgres".

		test_db=# UPDATE clients SET заказ=3 WHERE id=1;
		UPDATE 1

		test_db=# UPDATE clients SET заказ=4 WHERE id=2;
		UPDATE 1

		test_db=# UPDATE clients SET заказ=5 WHERE id=3;
		UPDATE 1

Приведите SQL-запрос для выдачи всех пользователей, которые совершили заказ, а также вывод данного запроса.

		test_db=# SELECT * FROM clients WHERE заказ IS NOT NULL;
		 id |       фамилия        | страна_проживания | заказ 
		----+----------------------+-------------------+-------
		  1 | Иванов Иван Иванович | USA               |     3
		  2 | Петров Петр Петрович | Canada            |     4
		  3 | Иоганн Себастьян Бах | Japan             |     5
		(3 rows)

5. Получите полную информацию по выполнению запроса выдачи всех пользователей из задачи 4 (используя директиву EXPLAIN). Приведите получившийся результат и объясните что значат полученные значения.
---

		test_db=# EXPLAIN SELECT * FROM clients WHERE заказ IS NOT NULL;
		                        QUERY PLAN                         
		-----------------------------------------------------------
		 Seq Scan on clients  (cost=0.00..18.10 rows=806 width=72)
		   Filter: ("заказ" IS NOT NULL)
		(2 rows)

 - Выбран план простого последовательного сканирования. 
 - 0.00: приблизительная стоимость запуска. Это время, которое проходит, прежде чем начнётся этап вывода данных, например для сортирующего узла это время сортировки.
 - 18.10: приблизительная общая стоимость. Она вычисляется в предположении, что узел плана выполняется до конца, то есть возвращает все доступные строки.
 - 806: ожидаемое число строк, которое должен вывести этот узел плана. При этом так же предполагается, что узел выполняется до конца.
 - 72: ожидаемый средний размер строк, выводимых этим узлом плана (в байтах).



