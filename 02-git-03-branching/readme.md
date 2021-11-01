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

- Сделаем коммит и отправим изменения в репозиторий:

		$ git add .
		$ git commit -m 'merge: @ instead *'
		$ git push
