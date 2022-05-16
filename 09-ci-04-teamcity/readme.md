Домашнее задание к занятию "09.04 Teamcity"
===

Подготовка инфраструктуры.
---
docker-compose.yml:

	version: "3"
	services:
	  teamcity:
	    image: jetbrains/teamcity-server
	    volumes:
	      - ~/teamcity/data/:/data/teamcity_server/datadir
	      - ~/teamcity/logs/:/opt/teamcity/logs
	    ports:
	      - 8111:8111
	  teamcity-agent:
	    image: jetbrains/teamcity-agent 
	    depends_on:
	      - teamcity
	    volumes:
	      - ~/teamcity/agent/:/data/teamcity_agent/conf 
	    environment:
	      SERVER_URL: "http://teamcity:8111"

Предварительное удаление контейнеров, образов, томов:

	docker rm -a
	docker image rm -a
	docker volume rm -a

Запуск docker-compose от текущего непрепилегированного пользователя (v):
[Running Docker Compose with Rootless Podman](https://fedoramagazine.org/use-docker-compose-with-podman-to-orchestrate-containers-on-fedora/)

	systemctl --user enable podman.socket
	systemctl --user start podman.socket
	systemctl --user status podman.socket
	export DOCKER_HOST=unix:///run/user/$UID/podman/podman.sock

	 docker-compose up
	Creating network "v_default" with the default driver
	Creating v_teamcity_1 ... done
	Creating v_teamcity-agent_1 ... done
	Attaching to v_teamcity_1, v_teamcity-agent_1
	teamcity_1        | /run-services.sh
	teamcity_1        | /services/check-server-volumes.sh
	teamcity_1        | 
	teamcity_1        | >>> Permission problem: TEAMCITY_DATA_PATH '/data/teamcity_server/datadir' is not a writeable directory
	teamcity_1        | >>> Permission problem: TEAMCITY_LOGS '/opt/teamcity/logs' is not a writeable directory
	teamcity_1        | 
	teamcity_1        |     Looks like some mandatory directories are not writable (see above).
	teamcity_1        |     TeamCity container is running under 'tcuser' (1000/1000) user.
	teamcity_1        | 
	teamcity_1        |     A quick workaround: pass '-u 0' parameter to 'docker run' command to start it under 'root' user.
	teamcity_1        |     The proper fix: run 'chown -R 1000:1000' on the corresponding volume(s), this can take noticeable time.
 	teamcity_1        | 
	teamcity_1        |     If the problem persists after the permission fix, please check that the corresponding volume(s)
	teamcity_1        |     are not used by stale stopped Docker containers ("docker container prune" command may help).
	teamcity_1        | 
	v_teamcity_1 exited with code 1
	teamcity-agent_1  | /run-services.sh
	teamcity-agent_1  | /services/run-docker.sh
	teamcity-agent_1  | /run-agent.sh
	teamcity-agent_1  | Will create new buildAgent.properties using distributive
	teamcity-agent_1  | TeamCity URL is provided: http://teamcity:8111
	teamcity-agent_1  | Will prepare agent config
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/buildAgent.dist.properties': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/buildAgent.properties': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/log4j.dtd': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/teamcity-agent-log4j2.xml': Permission denied
	teamcity-agent_1  | Error! Stopping the script.
	v_teamcity-agent_1 exited with code 1

Пользователь, от имени которого запускаются команды, имеет UID 1000:

	[v@nb-chernyshev ~]$ id
	uid=1000(v) gid=1000(v) groups=1000(v),10(wheel),18(dialout),977(vboxusers) context=unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023
	[v@nb-chernyshev ~]$ ls -n ~/teamcity/
	total 0
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 agent
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 data
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 logs

Тем не менее, запуск рекомендуемой команды:

	[v@nb-chernyshev ~]$ chown -R 1000:1000 ~/teamcity/
	[v@nb-chernyshev ~]$ ls -n ~/teamcity/
	total 0
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 agent
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 data
	drwxr-xr-x. 1 1000 1000 0 May 17 00:23 logs

Повторный запуск docker-compose приводит к той же ошибке:

	[v@nb-chernyshev ~]$ docker-compose up
	Starting v_teamcity_1 ... done
	Starting v_teamcity-agent_1 ... done
	Attaching to v_teamcity_1, v_teamcity-agent_1
	teamcity-agent_1  | /run-services.sh
	teamcity-agent_1  | /services/run-docker.sh
	teamcity_1        | /run-services.sh
	teamcity_1        | /services/check-server-volumes.sh
	teamcity_1        | 
	teamcity_1        | >>> Permission problem: TEAMCITY_DATA_PATH '/data/teamcity_server/datadir' is not a writeable directory
	teamcity_1        | >>> Permission problem: TEAMCITY_LOGS '/opt/teamcity/logs' is not a writeable directory
	teamcity_1        | 
	teamcity_1        |     Looks like some mandatory directories are not writable (see above).
	teamcity_1        |     TeamCity container is running under 'tcuser' (1000/1000) user.
	teamcity_1        | 
	teamcity_1        |     A quick workaround: pass '-u 0' parameter to 'docker run' command to start it under 'root' user.
	teamcity_1        |     The proper fix: run 'chown -R 1000:1000' on the corresponding volume(s), this can take noticeable time.
	teamcity_1        | 
	teamcity_1        |     If the problem persists after the permission fix, please check that the corresponding volume(s)
	teamcity_1        |     are not used by stale stopped Docker containers ("docker container prune" command may help).
	teamcity_1        | 
	teamcity-agent_1  | /run-agent.sh
	teamcity-agent_1  | Will create new buildAgent.properties using distributive
	teamcity-agent_1  | TeamCity URL is provided: http://teamcity:8111
	teamcity-agent_1  | Will prepare agent config
	teamcity-agent_1  | Error! Stopping the script.
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/buildAgent.dist.properties': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/buildAgent.properties': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/log4j.dtd': Permission denied
	teamcity-agent_1  | cp: cannot create regular file '/data/teamcity_agent/conf/teamcity-agent-log4j2.xml': Permission denied
	v_teamcity-agent_1 exited with code 1
	v_teamcity_1 exited with code 1

НЕОБХОДИМА ПОМОЩЬ ЭКСПЕРТОВ.
Михаил Караханов:  
"Попробуйте переделать в compose файле volume с обычного бинда на named volume -  я у себя исправил, все взлетело"  

docker-compose.yml

	version: "3"
	services:
	  teamcity:
	    image: jetbrains/teamcity-server
	    volumes:
	      - type: volume
	        source: data
	        target: /data/teamcity_server/datadir
	      - type: volume
	        source: logs
	        target: /opt/teamcity/logs
	    ports:
	      - 8111:8111
	  teamcity-agent:
	    image: jetbrains/teamcity-agent 
	    depends_on:
	      - teamcity
	    volumes:
	      - type: volume
	        source: logs
	        target: /data/teamcity_agent/conf 
	    environment:
	      SERVER_URL: "http://teamcity:8111"
	
	volumes:
	    data:
	    logs:
	    agent:


