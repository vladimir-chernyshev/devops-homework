### Подготовка к выполнению лабораторной работы, аутентификация на github.com посредством ключа SSH

1. Генерируем пару ключей SSH согласно статьи  [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent):

 $ssh-keygen -t ed25519 -C "Ваш email"

2. Редактируем ~/.profile, чтобы закрытый ключ автоматически загружался в SSH-агент при запуске WSL:

 $vi ~/.profile

	eval $(ssh-agent) >/dev/null

	ssh-add -q

 Посмотреть (и убедиться) после выхода\входа в WSL:

 $ssh-add -l

3. Добавляем открытый ключ в аккаунт на github.com согласно статьи  [Adding a new SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account):

 $cat ~/.ssh/id_ed25519.pub --> github.com > "Settings" > "SSH & GPG keys"

4. Меняем протокол синхронизации с github.com c HTTP на SSH согласно статьи  [Switching remote URLs from SSH to HTTPS](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories#switching-remote-urls-from-https-to-ssh):

 - идем в корень локального репозитория (NB!в WSL содержимое диска С: отображается как точка монтирования /mnt/c)

   $cd /mnt/c/[..]/devops-homework
 - смотрим как сейчас:

   $git remote -v

	origin  https://github.com/vladimir-chernyshev/devops-homework.git (fetch)

	origin  https://github.com/vladimir-chernyshev/devops-homework.git (push)

 - меняем

   $git remote set-url origin git@github.com:vladimir-chernyshev/devops-homework.git

 - пробуем:

   /mnt/c/Games/code/devops-homework$ git push

The authenticity of host 'github.com (140.82.121.4)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yessh
Warning: Permanently added 'github.com,140.82.121.4' (RSA) to the list of known hosts.
Everything up-to-date

5. Приступаем к выполнению лабораторной:

 $mkdir 02-git-01-vcs

 $vi 02-git-01-vcs/readme.md

### Выполнение лабораторной работы согласно задания:

git add 02-git-01-vcs/readme.md

git status

git commit -m 'First commit'

touch 02-git-01-vcs/.gitignore

mkdir 02-git-01-vcs/terraform

vi 02-git-01-vcs/terraform/.gitignore

vi 02-git-01-vcs/terraform/readme.md

git add 02-git-01-vcs/terraform/

git commit -m 'Added gitignore'

echo will_be_deleted > 02-git-01-vcs/will_be_deleted.txt

echo will_be_moved > 02-git-01-vcs/will_be_moved.txt

git add 02-git-01-vcs/*

git commit -m 'Prepare to delete and move'

git rm 02-git-01-vcs/will_be_deleted.txt

git mv 02-git-01-vcs/will_be_moved.txt 02-git-01-vcs/has_been_moved.txt

git commit -m 'Prepare to delete and move'

git push
