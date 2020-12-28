# Урок 3. Редактирование файлов

- Обзор текстовых редакторов (*nano*, *less*, *vim*)
- Работа с текстовыми файлами в командной строке
- Конкатенация файлов (*cat*)
- Объединение команд

## Практическое задание

### Задачи

1. С помощью текстового редактора *Vim* создать файл
с программой на *Python*, выводящей текст *'Hello, world!'*.

2. Запустить команду,
определяющую число строк в файле.

3. Создать еще один файл с командой на *Python*,
выводящей текст *'Linear regression'*.

4. Объединить эти два файла с помощью команды *cat*.

5. Придумать три случая применения команды *cat*
для работы с текстовыми файлами.

### Решение

1. Create *Python* script.

  ```
  $which python3
  /usr/bin/python3

  $vim hello.py

  $ls
  hello.py  hello.py~  task.md

  $chmod 744 hello.py

  $ls -l
  total 12
  -rwxr--r-- 1 dd users   59 Jul 17 15:54 hello.py
  -rw-r--r-- 1 dd users   55 Jul 17 15:32 hello.py~
  -rw-r--r-- 1 dd users 1070 Jul 17 15:49 task.md

  $./hello.py
  Hello, Brave New World!
  ```

  *hello.py*:

  ```python
  #!/usr/bin/python3

  s = 'Hello, Brave New World!'
  print(s)

  ```

2. Count lines in script file using *cat* and *wc* utilities.

  ```
  $cat --number hello.py
       1	#!/usr/bin/python3
       2
       3	s = 'Hello, Brave New World!'
       4	print(s)

  $wc --line < hello.py
  4
  ```

3. Create one more *Python* script.

  ```
  $nano regress.py

  $ls
  hello.py  regress.py  task.md

  $python3 regress.py
  Hello, Linear Regression!
  ```

  *regress.py*:

  ```python
  s = 'Hello, Linear Regression!'
  print(s)

  ```

4. Concatenates script files using *cat* utility.

  ```
  $cat hello.py regress.py > hello_regress.py

  $cat hello_regress.py
  #!/usr/bin/python3

  s = 'Hello, Brave New World!'
  print(s)
  s = 'Hello, Linear Regression!'
  print(s)

  $chmod 744 hello_regress.py

  $ls -l
  total 16
  -rwxr--r-- 1 dd users   59 Jul 17 16:21 hello.py
  -rwxr--r-- 1 dd users  100 Jul 17 16:24 hello_regress.py
  -rw-r--r-- 1 dd users   41 Jul 17 16:16 regress.py
  -rw-r--r-- 1 dd users 2100 Jul 17 16:21 task.md

  $./hello_regress.py
  Hello, Brave New World!
  Hello, Linear Regression!
  ```

5. Some more examples of *cat* utility use.

  - Copy standard input to file output.
  - Concatenate file to standard output.
  - Concatenates files and standard input to file or standard output.

```
$cat > one
first
second

third


fourth
```

```
$cat one
first
second

third


fourth
$cat --number one # number all output lines
     1	first
     2	second
     3
     4	third
     5
     6
     7	fourth
$cat --number-nonblank one # number nonempty output lines
     1	first
     2	second

     3	third


     4	fourth
$cat --squeeze-blank one # suppress repeated empty output lines
first
second

third

fourth
```

```
$cat > three
sixth
$cat one - three > four
fifth
$cat -s four
first
second

third

fourth
fifth
sixth
```
