Домашнее задание к занятию «2.2. Основы Git»
===
Подготовка  
---
Для подключения к *gitlab.com* и *bitbucket.org* решено использовать ту же пару ключей, что и для подлючения к *github.com* (занятие 2.1)


		$cat ~/.ssh/id_ed25519.pub --> gitlab.com > Edit profile > SSH keys

![Gitlab SSH key](img/gitlab-key.png)

[Gitlab Add an SSH key to your GitLab account](https://docs.gitlab.com/ee/ssh/)


		$cat ~/.ssh/id_ed25519.pub --> bitbucket.org > Personal settings > SSH keys

![Bitbucket SSH key](img/bitbucket-key.png)

[Bitbucket Set up an SSH key](https://support.atlassian.com/bitbucket-cloud/docs/set-up-an-ssh-key/)

Задание 1
---
Исходное состояние: настроен только репозиторий github.com, на репозиторий ссылаемся как на origin:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git remote -v
		origin  git@github.com:vladimir-chernyshev/devops-homework.git (fetch)
		origin  git@github.com:vladimir-chernyshev/devops-homework.git (push)


Добавим gitlab.com под именем gitlab:

		$git remote add gitlab https://gitlab.com/vladimir-chernyshev/devops-netology.git

![Gitlab SSH connection string](img/1.png)
  
Добавим bitbucket.org под именем bitbucket:

                $git remote add bitbucket git@bitbucket.org:vladimir-chernyshev/devops-netology.git

![Bitbucket SSH connection string](img/2.png)  
  
Поглядеть:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git remote -v
		bitbucket       git@bitbucket.org:vladimir-chernyshev/devops-netology.git (fetch)
		bitbucket       git@bitbucket.org:vladimir-chernyshev/devops-netology.git (push)
		gitlab  git@gitlab.com:vladimir-chernyshev/devops-netology.git (fetch)
		gitlab  git@gitlab.com:vladimir-chernyshev/devops-netology.git (push)
		origin  git@github.com:vladimir-chernyshev/devops-homework.git (fetch)
		origin  git@github.com:vladimir-chernyshev/devops-homework.git (push)


Зальем локальный репозиторий на gitlab.com:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git push -u gitlab
		The authenticity of host 'gitlab.com (172.65.251.78)' can't be established.
		ECDSA key fingerprint is SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw.
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added 'gitlab.com,172.65.251.78' (ECDSA) to the list of known hosts.
		Enumerating objects: 82, done.
		Counting objects: 100% (82/82), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (74/74), done.
		Writing objects: 100% (82/82), 320.56 KiB | 6.41 MiB/s, done.
		Total 82 (delta 27), reused 15 (delta 0)
		To gitlab.com:vladimir-chernyshev/devops-netology.git
		 * [new branch]      master -> master
		Branch 'master' set up to track remote branch 'master' from 'gitlab'.


Оказывается, по умолчанию на всех трех репозиториях предсуществует бранч master, причем неудаляемый(?):

-
		v@G713QE:/mnt/c/Games/code/devops-homework$ git push origin :master
		To github.com:vladimir-chernyshev/devops-homework.git
 		! [remote rejected] master (refusing to delete the current branch: refs/heads/master)
		error: failed to push some refs to 'git@github.com:vladimir-chernyshev/devops-homework.git'
-
		v@G713QE:/mnt/c/Games/code/devops-homework$ git push gitlab :master
		remote: GitLab: The default branch of a project cannot be deleted.
		To gitlab.com:vladimir-chernyshev/devops-netology.git
		 ! [remote rejected] master (pre-receive hook declined)
		error: failed to push some refs to 'git@gitlab.com:vladimir-chernyshev/devops-netology.git'
-
		v@G713QE:/mnt/c/Games/code/devops-homework$ git push bitbucket :master
		remote: error: refusing to delete the current branch: refs/heads/master
		To bitbucket.org:vladimir-chernyshev/devops-netology.git
		 ! [remote rejected] master (deletion of the current branch prohibited)
		error: failed to push some refs to 'git@bitbucket.org:vladimir-chernyshev/devops-netology.git'

 По условиям задачи требуется на всех трех репозиториях создать бранч main.  
Из справки [git-push(1)](https://git-scm.com/docs/git-push):
>		*git push*<repository> [<refspec>], where
>		<repository> - parameter can be either a URL or the name of a remote;
>		format of a <refspec> parameter is an optional plus +, followed by the source object <src>, followed by a colon :, followed by the destination ref <dst>..
 The <src> is often the name of the branch you would want to push, such as HEAD (see gitrevisions[7])
Из справки [gitrevision(7)](https://git-scm.com/docs/gitrevisions):
>		HEAD names the commit on which you based the changes in the working tree..
>		@ alone is a shortcut for HEAD

 Названия наших веток \<refspec\> конструируем как \<src\>':'\<dst\> т.е. 'HEAD:main' или '@:main'

- GitHub:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git push origin HEAD:main
		Enumerating objects: 11, done.
		Counting objects: 100% (11/11), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (8/8), done.
		Writing objects: 100% (8/8), 127.52 KiB | 894.00 KiB/s, done.
		Total 8 (delta 1), reused 0 (delta 0)
		remote: Resolving deltas: 100% (1/1), completed with 1 local object.
		remote:
		remote: Create a pull request for 'main' on GitHub by visiting:
		remote:      https://github.com/vladimir-chernyshev/devops-homework/pull/new/main
		remote:
		To github.com:vladimir-chernyshev/devops-homework.git
	 	* [new branch]      HEAD -> main

- GitLab:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git push gitlab HEAD:main
		Enumerating objects: 11, done.
		Counting objects: 100% (11/11), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (8/8), done.
		Writing objects: 100% (8/8), 127.52 KiB | 7.97 MiB/s, done.
		Total 8 (delta 1), reused 0 (delta 0)
		remote:
		remote: To create a merge request for main, visit:
		remote:   https://gitlab.com/vladimir-chernyshev/devops-netology/-/merge_requests/new?merge_request%5Bsource_branch%5D=main
		remote:
		To gitlab.com:vladimir-chernyshev/devops-netology.git
		 * [new branch]      HEAD -> main

- Bitbucket:

		v@G713QE:/mnt/c/Games/code/devops-homework$ git push bitbucket HEAD:main
		The authenticity of host 'bitbucket.org (18.234.32.156)' can't be established.
		RSA key fingerprint is SHA256:zzXQOXSRBEiUtuE8AikJYKwbHaxvSc0ojez9YXaGp1A.
		Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
		Warning: Permanently added 'bitbucket.org,18.234.32.156' (RSA) to the list of known hosts.
		Enumerating objects: 90, done.
		Counting objects: 100% (90/90), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (82/82), done.
		Writing objects: 100% (90/90), 448.03 KiB | 7.72 MiB/s, done.
		Total 90 (delta 28), reused 15 (delta 0)
		remote:
		remote: Create pull request for main:
		remote:   https://bitbucket.org/vladimir-chernyshev/devops-netology/pull-requests/new?source=main&t=1
		remote:
		To bitbucket.org:vladimir-chernyshev/devops-netology.git
		 * [new branch]      HEAD -> main
Задание 2
---
  Посмотрим историю коммитов:  

		$ git log --oneline -5
		c3ea80f (HEAD -> master, origin/main, gitlab/main, bitbucket/main) one more
		2e23ac0 Добавил описание refspec
		3eb4849 (origin/master, origin/HEAD, gitlab/master, bitbucket/master) update readme.md
		97a7a0f update readme.md
		8dec4b9 update readme.md  

Добавим лекговесный тэг к HEAD:  

		$ git tag v0.0 c3ea80f

Посмотрим результат:

		$ git log --oneline -5
		c3ea80f (HEAD -> master, tag: v0.0, origin/main, gitlab/main, bitbucket/main) one more
		2e23ac0 Добавил описание refspec
		3eb4849 (origin/master, origin/HEAD, gitlab/master, bitbucket/master) update readme.md
		97a7a0f update readme.md
		8dec4b9 update readme.md

Добавим аннотированный тэг к HEAD:

		$ git tag -a v0.1 -m 'Annotated tag' c3ea80f

Посмотрим результат:

                $ git log
		v@G713QE:/mnt/c/Games/code/devops-homework$ git log  -5
		commit c3ea80f1b2cd481a9d458a7469165e811b39cad3 (HEAD -> master, tag: v0.1, tag: v0.0, origin/main, gitlab/main, bitbucket/main)
		Author: Vladimir Chernyshev <v.chernyshev@ro.ru>
		Date:   Fri Oct 29 22:37:05 2021 +0500
		
		    one more
		
		commit 2e23ac0a5ed4feb551617fb5d34ad8fc63315b03
		Author: Vladimir Chernyshev <v.chernyshev@ro.ru>
		Date:   Fri Oct 29 22:30:16 2021 +0500
		
		    Добавил описание refspec
		
		commit 3eb48495a0a30074f8af03960098ebd60f205a01 (origin/master, origin/HEAD, gitlab/master, bitbucket/master)
		Author: Vladimir Chernyshev <v.chernyshev@ro.ru>
		Date:   Fri Oct 29 03:05:33 2021 +0500
		
		    update readme.md

Заапишем изменения в ветки main c тэгами, в ветки master без тэгов всех трех репозиториев:

		$git add .
		$git commit -m 'add two tags'
  - GitHub:
		$git push origin HEAD:main
		$git push origin --tags HEAD:main
		$git push origin HEAD
  - GitLab:
		$git push gitlab HEAD:main
		$git push gitlab --tags HEAD:main
		$git push gitlab HEAD
  - Bitbucket
		$git push bitbucket HEAD:main
		$git push bitbucket --tags HEAD:main
		$git push bitbucket HEAD
  

