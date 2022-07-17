Домашнее задание к занятию "08.01 Введение в Ansible"
===

1. Попробуйте запустить playbook на окружении из *test.yml*, зафиксируйте какое значение имеет факт *some_fact* для указанного хоста при выполнении playbook'a.
---
		[v@nb-chernyshev playbook]$ ansible-playbook -i inventory/test.yml site.yml 

		PLAY [Print os facts] **********************************************************

		TASK [Gathering Facts] *********************************************************
		ok: [localhost]

		TASK [Print OS] ****************************************************************
		ok: [localhost] => {
		    "msg": "Fedora"
		}

		TASK [Print fact] **************************************************************
		ok: [localhost] => {
		    "msg": 12
		}

		PLAY RECAP *********************************************************************
		localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

*some_fact* имеет значение 12

2. Найдите файл с переменными (group_vars) в котором задаётся найденное в первом пункте значение и поменяйте его на 'all default fact'.
---

		[v@nb-chernyshev playbook]$ egrep -R 12 group_vars/
		group_vars/all/examp.yml:  some_fact: 12

3. Воспользуйтесь подготовленным (используется docker) или создайте собственное окружение для проведения дальнейших испытаний.
4. Проведите запуск playbook на окружении из prod.yml. Зафиксируйте полученные значения some_fact для каждого из managed host.

	[v@nb-chernyshev playbook]$ ansible-playbook -i inventory/prod.yml site.yml

	PLAY [Print os facts] **********************************************************************************************************************

	TASK [Gathering Facts] *********************************************************************************************************************
	ok: [ubuntu]
	ok: [centos7]

	TASK [Print OS] ****************************************************************************************************************************
	ok: [centos7] => {
	    "msg": "CentOS"
	}
	ok: [ubuntu] => {
	    "msg": "Ubuntu"
	}

	TASK [Print fact] **************************************************************************************************************************
	ok: [centos7] => {
	    "msg": "el"
	}
	ok: [ubuntu] => {
	    "msg": "deb"
	}

PLAY RECAP *********************************************************************************************************************************
centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0  

*some_fact* для Centos имеет значение *el*
*some_fact* для Ubuntu имеет значение *deb*

5. Добавьте факты в *group_vars* каждой из групп хостов так, чтобы для *some_fact* получились следующие значения: для deb - 'deb default fact', для el - 'el default fact'.
---

	group_vars/deb/examp.yml:  some_fact: 'deb default fact'
	group_vars/el/examp.yml:  some_fact: 'el default fact'

6. Повторите запуск playbook на окружении *prod.yml*. Убедитесь, что выдаются корректные значения для всех хостов.
---

       [v@nb-chernyshev playbook]$ ansible-playbook -i inventory/prod.yml site.yml

	PLAY [Print os facts] **********************************************************************************************************************

	TASK [Gathering Facts] *********************************************************************************************************************
	ok: [ubuntu]
	ok: [centos7]

	TASK [Print OS] ****************************************************************************************************************************
	ok: [centos7] => {
	    "msg": "CentOS"
	}
	ok: [ubuntu] => {
	    "msg": "Ubuntu"
	}

	TASK [Print fact] **************************************************************************************************************************
	ok: [centos7] => {
	    "msg": "el default fact"
	}
	ok: [ubuntu] => {
	    "msg": "deb default fact"
	}
	
	PLAY RECAP *********************************************************************************************************************************
	centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
	ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

7. При помощи ansible-vault зашифруйте факты в group_vars/deb и group_vars/el с паролем netology.
---

	[v@nb-chernyshev playbook]$ ansible-vault encrypt group_vars/deb/examp.yml group_vars/el/examp.yml
	New Vault password: 
	Confirm New Vault password: 
	Encryption successful

	[v@nb-chernyshev playbook]$ cat group_vars/deb/examp.yml 
	$ANSIBLE_VAULT;1.1;AES256
	33306432643838623732336363393664376264386136626462663964366533363739626334366438
	3465323439363637643564383062613334336230366432390a363837336566613663636633343035
	65353539373064646632353030316337393166613361383764633066393966326562636138616432
	3761663530306131380a666262623666333635616264613935343931613465313835313164616334
	36383332336633636433633432326531313235343636326230353361363262613561393037383461
	6165373734633263303565373065383837343139633736653363
	[v@nb-chernyshev playbook]$ cat group_vars/el/examp.yml 
	$ANSIBLE_VAULT;1.1;AES256
	36613566616165356661656436613839646335376134366166643761346333626533373535376235
	6538313038633839323237306334393437363232306364620a666536336632326437616436363332
	31646439336132323739303934383366353834393532343130366364393361376530303731653332
	3733623330646539320a613765313638653435633231653963363937323234363938316437313432
	39346632316335633836396635626635303561353937316137633262313837313432316262633063
	3164623337383034386332653363633561616464343734633733

8. Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь в работоспособности.
---

		[v@nb-chernyshev playbook]$ ansible-playbook -i inventory/prod.yml site.yml --ask-vault-pass
		Vault password: 

		PLAY [Print os facts] **********************************************************************************************************************

		TASK [Gathering Facts] *********************************************************************************************************************
		ok: [ubuntu]
		ok: [centos7]

		TASK [Print OS] ****************************************************************************************************************************
		ok: [centos7] => {
		    "msg": "CentOS"
		}
		ok: [ubuntu] => {
		    "msg": "Ubuntu"
		}

		TASK [Print fact] **************************************************************************************************************************
		ok: [centos7] => {
		    "msg": "el default fact"
		}
		ok: [ubuntu] => {
		    "msg": "deb default fact"
		}

		PLAY RECAP *********************************************************************************************************************************
		centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
		ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

9. Посмотрите при помощи *ansible-doc* список плагинов для подключения. Выберите подходящий для работы на *control node*
---

	[v@nb-chernyshev playbook]$ ansible-doc --type=connection -l | egrep "execute on controller"
	[WARNING]: Collection ibm.qradar does not support Ansible version 2.12.7
	[WARNING]: Collection splunk.es does not support Ansible version 2.12.7
	[DEPRECATION WARNING]: ansible.netcommon.napalm has been deprecated. See the 
	plugin documentation for more details. This feature will be removed from 
	ansible.netcommon in a release after 2022-06-01. Deprecation warnings can be 
	disabled by setting deprecation_warnings=False in ansible.cfg.
	local                          execute on controller         

10. В prod.yml добавьте новую группу хостов с именем local, в ней разместите localhost с необходимым типом подключения.
---

	file: inventory/prod.yml
	---
	  el:
	    hosts:
	      centos7:
	        ansible_connection: docker
	  deb:
	    hosts:
	      ubuntu:
	        ansible_connection: docker
	  local:
	    hosts:
	      localhost:
	        ansible_connection: local         

11. Запустите playbook на окружении prod.yml. При запуске ansible должен запросить у вас пароль. Убедитесь что факты some_fact для каждого из хостов определены из верных group_vars.
---

	[v@nb-chernyshev playbook]$ ansible-playbook site.yml -i inventory/prod.yml --ask-vault-pass
	Vault password: 

	PLAY [Print os facts] *********************************************************************************************************

	TASK [Gathering Facts] ********************************************************************************************************
	ok: [localhost]
	ok: [ubuntu]
	ok: [centos7]

	TASK [Print OS] ***************************************************************************************************************
	ok: [centos7] => {
	    "msg": "CentOS"
	}
	ok: [ubuntu] => {
	    "msg": "Ubuntu"
	}
	ok: [localhost] => {
	    "msg": "Ubuntu"
	}

	TASK [Print fact] *************************************************************************************************************
	ok: [centos7] => {
	    "msg": "el default fact"
	}
	ok: [ubuntu] => {
	    "msg": "deb default fact"
	}
	ok: [localhost] => {
	    "msg": "all default fact"
	}

	PLAY RECAP ********************************************************************************************************************
	centos7                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
	localhost                  : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
	ubuntu                     : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0        

12. Заполните README.md ответами на вопросы. Сделайте git push в ветку master. В ответе отправьте ссылку на ваш открытый репозиторий с изменённым playbook и заполненным README.md.
---

[README.md](playbook/README.md)
