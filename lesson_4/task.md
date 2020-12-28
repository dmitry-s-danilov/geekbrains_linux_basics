# Урок 4. Права в Linux. Установка программ. Создание и запуск скриптов Python в Linux

## Практическое задание

### Задачи

1. Создать пользователя `user_new`
и предоставить ему права на редактирование файла с программой,
выводящей на экран 'Hello, world!'.

2. Зайти под юзером `user_new`
и с помощью редактора Vim поменять фразу в скрипте из пункта 1
на любую другую.

3. Под юзером `user_new` зайти в его домашнюю директорию
и создать программу на Python,
выводящую в консоль цифры от 1 до 10 включительно
с интервалом в 1 секунду.

### Решение

1. Creates `user_new` user under `ubuntu` user:

   ```
   ubuntu@ip-172-31-42-182:~$ PS1='\u:\w$'

   ubuntu:~$useradd -D
   GROUP=100
   HOME=/home
   INACTIVE=-1
   EXPIRE=
   SHELL=/bin/sh
   SKEL=/etc/skel
   CREATE_MAIL_SPOOL=no

   ubuntu:~$sudo useradd --create-home --home-dir /home/user_new --shell /bin/bash user_new

   ubuntu:~$cat /etc/passwd | grep ^user
   user_new:x:1001:1002::/home/user_new:/bin/sh

   ubuntu:~$ls -l /home
   total 8
   drwxr-xr-x 6 ubuntu   ubuntu   4096 Jul 19 19:07 ubuntu
   drwxr-xr-x 2 user_new user_new 4096 Jul 20 10:50 user_new

   ubuntu:~$sudo passwd user_new
   New password:
   Retype new password:
   passwd: password updated successfully

   ubuntu:~$su user_new
   Password:

   user_new@ip-172-31-42-182:/home/ubuntu$ PS1='\u:\w$'

   user_new:/home/ubuntu$cd ~

   user_new:~$pwd
   /home/user_new

   user_new:~$whoami
   user_new

   user_new:~$groups
   user_new
   ```

   Creates `hello` python script under `ubuntu` user:
   ```
   ubuntu:~$vim hello

   ubuntu:~$chmod u+x hello

   ubuntu:~$./hello
   Hello, World!
   ```

   Created `hello` script:

   ```python
   #!/usr/bin/python3

   print('Hello, World!')

   ```

   Either gives other users the rights to edit `hello` file:

   ```
   ubuntu:~$ls -l hello
   -rwxrw-r-- 1 ubuntu ubuntu 51 Jul 20 12:17 hello

   ubuntu:~$chmod o+w hello
   ```

   Or add `user_new` user to `ubuntu` group:

   ```
   ubuntu:~$sudo usermod --groups ubuntu user_new

   ubuntu:~$groups user_new
   user_new : user_new ubuntu
   ```

2. Changes `hello` file under `user_new` user:

   ```
   user_new:~$vim /home/ubuntu/hello

   user_new:~$python3 /home/ubuntu/hello
   Hello From New User!
   ```

   Modified `hello` script:

   ```python
   #!/usr/bin/python3

   print('Hello From New User!')

   ```

3. Creates a python script `sleep` under `user_new` user:

   ```
   user_new:~$whoami
   user_new

   user_new:~$pwd
   /home/user_new

   user_new:~$vim sleep.py

   user_new:~$ls -l sleep.py
   -rw-rw-r-- 1 user_new user_new 258 Jul 20 12:55 sleep.py

   user_new:~$python3 sleep.py # one line printing
   time left: 00 sec
   ```

   Created `sleep.py` script:

   ```python
   from time import sleep

   n = 10  # a number of times
   dt = 1  # time delta [sec]
   t = n * dt  # current time [sec]

   while True:
       print(f'\rtime left: {t:02d} sec', end='')
       if t > 0:
           sleep(dt)
       else:
           print()
           break
       t -= dt

   ```

4. Delete `user_new` user:

   ```
   ubuntu:~$sudo userdel --remove user_new
   userdel: user_new mail spool (/var/mail/user_new) not found
   ```
