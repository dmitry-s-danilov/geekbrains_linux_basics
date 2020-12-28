# Урок 2. Файлы и папки

## Практическое задание

### Задачи

1. Создать каталоги ​*first* и *​second* в домашней директории,
а в них — текстовые файлы ​*first.py* и *second.py*​,
содержащие программы, выводящие на экран числа *1* и *2* соответственно.

2. Переместить файл ​*second.py*​ в папку ​*first*.

3. Удалить папку ​*second*​.

4. Переименовать папку ​*first*​ в *first_second*​.

5. Удалить папку *​first_second*​ вместе с содержимым.

### Решение

0. Change the value of the default prompt.

  ```
  ubuntu@ip-172-31-37-88:~$ PS1='$'
  $whoami
  ubuntu
  $pwd
  /home/ubuntu
  ```

1. Make directories and scripts.

  ```
  $pwd
  /home/ubuntu
  $mkdir first
  $mkdir second
  $ls
  first  second
  $echo 'print(1)' > first/first.py
  $ls first
  first.py
  $python3 first/first.py
  1
  $echo 'print(2)' > second/second.py
  $ls second
  second.py
  $python3 second/second.py
  2
  ```

2. Move a file.

  ```
  $mv second/second.py first
  $ls first
  first.py  second.py
  ```

3. Remove a directory.

  ```
  $rm -r second
  $ls
  first
  ```

4. Rename a directory.

  ```
  $mv first first_second
  $ls
  first_second
  ```

5. Remove a directory.

  ```
  $rm -r first_second
  $ls -l
  total 0
  ```
