Домашнее задание к занятию "08.02 Работа с Playbook"
===

1. Приготовьте свой собственный inventory файл `prod.yml`.
---

		---
		clickhouse:
		  hosts:
		    clickhouse-01:
		      ansible_host: 192.168.0.2
		      ansible_connection: ssh
		      ansible_ssh_user: root


2. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает [vector](https://vector.dev).
3. При создании tasks рекомендую использовать модули: `get_url`, `template`, `unarchive`, `file`.
4. Tasks должны: скачать нужной версии дистрибутив, выполнить распаковку в выбранную директорию, установить vector.
---

		---
		- name: install clickhouse
		  hosts: clickhouse
		  handlers:
		    - name: start clickhouse service
		      become: true
		      ansible.builtin.service:
		        name: clickhouse-server
		        state: restarted
		  tasks:
		    - block:
		        - name: get clickhouse distrib
		          ansible.builtin.get_url:
		            url: "https://packages.clickhouse.com/rpm/stable/{{ item }}-{{ clickhouse_version }}.noarch.rpm"
		            dest: "./{{ item }}-{{ clickhouse_version }}.rpm"
		          with_items: "{{ clickhouse_packages }}"
		      rescue:
		        - name: get clickhouse distrib
		          ansible.builtin.get_url:
		            url: "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-{{ clickhouse_version }}.x86_64.rpm"
		            dest: "./clickhouse-common-static-{{ clickhouse_version }}.rpm"
		    - name: Install clickhouse packages
		      become: true
		      ansible.builtin.yum:
		        name:
		          - clickhouse-common-static-{{ clickhouse_version }}.rpm
		          - clickhouse-client-{{ clickhouse_version }}.rpm
		          - clickhouse-server-{{ clickhouse_version }}.rpm
		      notify: start clickhouse service

		    - name: Force restart clickhouse service
		      ansible.builtin.meta: flush_handlers

		    - name: create database
		      ansible.builtin.command: "clickhouse-client -q 'create database logs;'"
		      register: create_db
		      failed_when: create_db.rc != 0 and create_db.rc !=82
		      changed_when: create_db.rc == 0

		- name: install vector
		  hosts: clickhouse
		  handlers:
		    - name: start vector service
		      become: true
		      ansible.builtin.service:
		        name: vector
		        state: restarted
		  tasks:
		    - name: get vector distrib
		      ansible.builtin.get_url:
		        url: "https://packages.timber.io/vector/0.22.0/vector-0.22.0-1.x86_64.rpm"
		        dest: ./vector.rpm
		    - name: install vector packages
		      become: true
		      ansible.builtin.yum:
		        name:
		          - vector.rpm
		      notify: start vector service


5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
---

		$ ansible-playbook -i inventory/prod.yml site.yml --check

		PLAY [install clickhouse] *************************************************************************************************************************************

		TASK [Gathering Facts] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [get clickhouse distrib] *********************************************************************************************************************************
		changed: [clickhouse-01] => (item=clickhouse-client)
		changed: [clickhouse-01] => (item=clickhouse-server)
		failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-22.3.3.44.rpm", "elapsed": 0, "item": "clickhouse-common-static", "msg": "Request failed", "response": "HTTP Error 404: Not Found", "status_code": 404, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-22.3.3.44.noarch.rpm"}

		TASK [Get clickhouse distrib] *********************************************************************************************************************************
		changed: [clickhouse-01]

		TASK [Install clickhouse packages] ****************************************************************************************************************************
		fatal: [clickhouse-01]: FAILED! => {"changed": false, "msg": "No RPM file matching 'clickhouse-common-static-22.3.3.44.rpm' found on system", "rc": 127, "results": ["No RPM file matching 'clickhouse-common-static-22.3.3.44.rpm' found on system"]}

		PLAY RECAP ****************************************************************************************************************************************************
		clickhouse-01              : ok=2    changed=1    unreachable=0    failed=1    skipped=0    rescued=1    ignored=0 

7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
---

		$ ansible-playbook -i inventory/prod.yml site.yml --diff

		PLAY [Install Clickhouse] *************************************************************************************************************************************

		TASK [Gathering Facts] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Get clickhouse distrib] *********************************************************************************************************************************
		changed: [clickhouse-01] => (item=clickhouse-client)
		changed: [clickhouse-01] => (item=clickhouse-server)
		failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-22.6.3.35.rpm", "elapsed": 0, "item": "clickhouse-common-static", "msg": "Request failed", "response": "HTTP Error 404: Not Found", "status_code": 404, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-22.6.3.35.noarch.rpm"}

		TASK [Get clickhouse distrib] *********************************************************************************************************************************
		changed: [clickhouse-01]

		TASK [Install clickhouse packages] ****************************************************************************************************************************
		changed: [clickhouse-01]

		TASK [Force restart clickhouse service] ***********************************************************************************************************************

		RUNNING HANDLER [Start clickhouse service] ********************************************************************************************************************
		changed: [clickhouse-01]

		TASK [Create database] ****************************************************************************************************************************************
		changed: [clickhouse-01]

		PLAY [Install Vector] *****************************************************************************************************************************************

		TASK [Gathering Facts] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Get vector distrib] *************************************************************************************************************************************
		changed: [clickhouse-01]

		TASK [Install vector packages] ********************************************************************************************************************************
		changed: [clickhouse-01]

		RUNNING HANDLER [Start vector service] ************************************************************************************************************************
		changed: [clickhouse-01]

		PLAY RECAP ****************************************************************************************************************************************************
		clickhouse-01              : ok=9    changed=7    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0

8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
---

		$ ansible-playbook -i inventory/prod.yml site.yml --diff

		PLAY [Install Clickhouse] *************************************************************************************************************************************

		TASK [Gathering Facts] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Get clickhouse distrib] *********************************************************************************************************************************
		ok: [clickhouse-01] => (item=clickhouse-client)
		ok: [clickhouse-01] => (item=clickhouse-server)
		failed: [clickhouse-01] (item=clickhouse-common-static) => {"ansible_loop_var": "item", "changed": false, "dest": "./clickhouse-common-static-22.6.3.35.rpm", "elapsed": 0, "gid": 0, "group": "root", "item": "clickhouse-common-static", "mode": "0644", "msg": "Request failed", "owner": "root", "response": "HTTP Error 404: Not Found", "size": 246310036, "state": "file", "status_code": 404, "uid": 0, "url": "https://packages.clickhouse.com/rpm/stable/clickhouse-common-static-22.6.3.35.noarch.rpm"}

		TASK [Get clickhouse distrib] *********************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Install clickhouse packages] ****************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Force restart clickhouse service] ***********************************************************************************************************************

		TASK [Create database] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		PLAY [Install Vector] *****************************************************************************************************************************************

		TASK [Gathering Facts] ****************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Get vector distrib] *************************************************************************************************************************************
		ok: [clickhouse-01]

		TASK [Install vector packages] ********************************************************************************************************************************
		ok: [clickhouse-01]

		PLAY RECAP ****************************************************************************************************************************************************
		clickhouse-01              : ok=7    changed=0    unreachable=0    failed=0    skipped=0    rescued=1    ignored=0

9. Подготовьте README.md файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
---

[README.md](playbook/README.md)

10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-02-playbook` на фиксирующий коммит, в ответ предоставьте ссылку на него.
---

Ссылка на соответствующий [тег](https://github.com/vladimir-chernyshev/devops-homework/tree/08-ansible-02-playbook/08-ansible-02-playbook)

