Домашнее задание к занятию «2.3. Ветвления в Git»
===
Подготовка к выполнению задания
---
- Создаем каталоги и два файла _merge.sh_ и _rebase.sh_ идентичного содержания:

		$mkdir -p 02-git-03-branching/branching

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		 #!/bin/bash
		 # display command line options
		
		 count=1
		 for param in "$*"; do
		     echo "\$* Parameter #$count = $param"
		     count=$(( $count + 1 ))
		 done
		 EOF

		$ cp 02-git-03-branching/branching/merge.sh 02-git-03-branching/branching/rebase.sh

- Сделаем предварительный коммит в ветку *main*:

		$ git status
		On branch main
		
		Untracked files:
		  (use "git add <file>..." to include in what will be committed)
		        02-git-03-branching/
		
		$git add .
		$git commit -m 'prepare for merge and rebase'
		$git status
		On branch main
		nothing to commit, working tree clean

Подготовка файла *merge.sh*
---
- Создадим ветку *git-merge*:

		$ git branch
		* main
		  master
		$ git switch -c git-merge
		Switched to a new branch 'git-merge'

- Заменим содержимое файла _merge.sh_ на

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		#!/bin/bash
		# display command line options
		
		count=1
		for param in "$@"; do
		    echo "\$@ Parameter #$count = $param"
		    count=$(( $count + 1 ))
		done
		EOF

- Сделаем коммит и отправим изменения в репозиторий git-merge:

		$ git add .
		$ git commit -m 'merge: @ instead *'
		$ git push -u origin git-merge
		Enumerating objects: 34, done.
		Counting objects: 100% (34/34), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (20/20), done.
		Writing objects: 100% (24/24), 4.46 KiB | 198.00 KiB/s, done.
		Total 24 (delta 7), reused 0 (delta 0)
		remote: Resolving deltas: 100% (7/7), completed with 4 local objects.
		remote:
		remote: Create a pull request for 'git-merge' on GitHub by visiting:
		remote:      https://github.com/vladimir-chernyshev/devops-homework/pull/new/git-merge
		remote:
		To github.com:vladimir-chernyshev/devops-homework.git
		 * [new branch]      git-merge -> git-merge
		Branch 'git-merge' set up to track remote branch 'git-merge' from 'origin'.

- Внесем еще одно изменение в _merge.sh_:

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		#!/bin/bash
		# display command line options
		
		count=1
		while [[ -n "$1" ]]; do
		    echo "Parameter #$count = $1"
		    count=$(( $count + 1 ))
		    shift
		done
		EOF

- Сделаем коммит и отправим изменения в репозиторий git-merge:

                $ git commit -a -m 'merge: use shift'
                $ git push 

Изменение ветки *main*
---
- Вернемся в ветку *main*:

		$ git switch main
		Switched to branch 'main'

- Изменим файл _rebase.sh_ и отправим изменения в репозиторий *main*:

		cat << EOF > 02-git-03-branching/branching/rebase.sh
		#!/bin/bash
		# display command line options
		
		count=1
		for param in "$@"; do
		    echo "\$@ Parameter #$count = $param"
		    count=$(( $count + 1 ))
		done
		
		echo "====="
		EOF

		$ git add .
		$ git commit -m 'rebase.sh to main'
		$ git push -u origin main
		Enumerating objects: 12, done.
		Counting objects: 100% (12/12), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (6/6), done.
		Writing objects: 100% (7/7), 1.75 KiB | 199.00 KiB/s, done.
		Total 7 (delta 2), reused 0 (delta 0)
		remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
		To github.com:vladimir-chernyshev/devops-homework.git
		   2e19f73..7e83f47  main -> main
		Branch 'main' set up to track remote branch 'main' from 'origin'.

Подготовка файла _rebase.sh_
---
- Найдем хэш коммита 'prepare for merge and rebase' и сделаем checkout на него:

		$ git log --grep 'prepare for merge and rebase'
		commit 61965401eb79e4edc29644d5986059cc1d9fb2a5
		Author: Vladimir Chernyshev <v.chernyshev@ro.ru>
		Date:   Mon Nov 1 20:57:41 2021 +0500
		
		    prepare for merge and rebase
		git checkout 61965401eb79e4edc29644d5986059cc1d9fb2a5
		Note: switching to '61965401eb79e4edc29644d5986059cc1d9fb2a5'.
		
		You are in 'detached HEAD' state. You can look around, make experimental
		changes and commit them, and you can discard any commits you make in this
		state without impacting any branches by switching back to a branch.
		
		If you want to create a new branch to retain commits you create, you may
		do so (now or later) by using -c with the switch command. Example:
		
		  git switch -c <new-branch-name>
		
		Or undo this operation with:
		
		  git switch -
		
		Turn off this advice by setting config variable advice.detachedHead to false
		
		HEAD is now at 6196540 prepare for merge and rebase

- Создадим на этом коммите ветку *git-rebase*:

		$ git switch -c git-rebase
Switched to a new branch 'git-rebase'

- Изменим содержимое файла _rebase.sh_ и отправим коммит в ветку *git-rebase*:

		$cat << EOF > 02-git-03-branching/branching/rebase.sh
		#!/bin/bash
		# display command line options
		
		count=1
		for param in "$@"; do
		    echo "Parameter: $param"
		    count=$(( $count + 1 ))
		done
		
		echo "====="
		EOF
		$git add .
		$git commit -m 'git-rebase 1'
		$git push -u origin git-rebase
		Enumerating objects: 12, done.
		Counting objects: 100% (12/12), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (6/6), done.
		Writing objects: 100% (7/7), 2.41 KiB | 274.00 KiB/s, done.
		Total 7 (delta 1), reused 0 (delta 0)
		remote: Resolving deltas: 100% (1/1), completed with 1 local object.
		remote:
		remote: Create a pull request for 'git-rebase' on GitHub by visiting:
		remote:      https://github.com/vladimir-chernyshev/devops-homework/pull/new/git-rebase
		remote:
		To github.com:vladimir-chernyshev/devops-homework.git
		 * [new branch]      git-rebase -> git-rebase
		Branch 'git-rebase' set up to track remote branch 'git-rebase' from 'origin'.

- Заменим строку _echo "Parameter: $param"_ на _echo "Next parameter: $param"_ и сделаем еще один коммит в *git-rebase*:

		$cat << EOF > 02-git-03-branching/branching/rebase.sh
		#!/bin/bash
		# display command line options
		
		count=1
		for param in "$@"; do
		    echo "Next parameter: $param"
		    count=$(( $count + 1 ))
		done
		
		echo "====="
		EOF
		$ git commit -a -m 'git-rebase 2'
		$ git push
		Enumerating objects: 11, done.
		Counting objects: 100% (11/11), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (6/6), done.
		Writing objects: 100% (6/6), 781 bytes | 130.00 KiB/s, done.
		Total 6 (delta 3), reused 0 (delta 0)
		remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
		To github.com:vladimir-chernyshev/devops-homework.git
		   69504cb..f5494b5  git-rebase -> git-rebase


