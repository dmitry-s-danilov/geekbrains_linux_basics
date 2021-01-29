# Geekbrains. Введение в Linux и облачные вычисления

## Урок 7. Способы выбора данных из файла

- Команды *awk*, *sed*, *grep*
- Регулярные выражения

## Практическое задание

1. Выбрать из домашней директории текущего пользователя
файлы с расширением *.py*, название которых начинается на букву *t*.
2. Из всех файлов с расширением *.py*,
расположенных в домашней директории пользователя,
выбрать строки, содержащие команду *print*,
и вывести их на экран.
3. Из результатов работы команды *uptime* выведите число дней
(часов или минут – в зависимости от времени работы ОС),
которое система работает без перезагрузки.


## Решение задания

### 0. Create files

Generates python files *.py*
using a self-replicated system of two file:

- a program *test.py*
that rearranges characters in self name,
- a script *test.sh*
that copies a program
until name symbols permutations are exhausted.

```
$ ls
test.py  test.sh

$ sh test.sh 
initial: test.py
copied: estt.py
copied: stte.py
copied: ttes.py

$ ls
estt.py  stte.py  test.py  test.sh  ttes.py
```

A program *test.py*:
    
```python
from sys import argv

name_ext = argv[0]
name = name_ext[:-3]
ext = name_ext[-3:]

name = name[1:] + name[0]
name_ext = name + ext

print(name_ext)
```

A script *test.sh*:
    
```bash
ZERO=test.py
echo initial: $ZERO

FIRST=$ZERO
SECOND=`python3 $FIRST`

while [ "$SECOND" != "$ZERO" ]
do
    cp $FIRST $SECOND
    echo copied: $SECOND
    
    FIRST=$SECOND
    SECOND=`python3 $FIRST`
done
```

### 1. Select files

Selects files,
the name of which begins with the symbol *t*,
and with the *.py* extension.

Lists using *ls*:

```
$ ls -a
.  ..  .bash_logout  .bashrc  .cache  .profile  .ssh  estt.py  stte.py  test.py  test.sh  ttes.py
```

Selects with *ls* and *grep*:

```
$ ls -a | grep '^t.*' # begins with 't'
test.py
test.sh
ttes.py

$ ls -a | grep '\.py$' # ends with '.py'
estt.py
stte.py
test.py
ttes.py

$ ls -a | grep '^t.*\.py$' # both
test.py
ttes.py
```

Selects with *ls* and *sed*:

```
$ ls -a | sed -n '/^t.*/p' # begins with 't'
test.py
test.sh
ttes.py

$ ls -a | sed -n '/\.py$/p' # ens with '.py'
estt.py
stte.py
test.py
ttes.py

$ ls -a | sed -n '/^t.*\.py$/p' # both
test.py
ttes.py
```

### 2. Select lines

From all files with the *.py* extension
selects the lines containing the *print* command.

Select with *cat* and *grep*:

```
$ cat *\.py | grep '^.*print(\w\+).*$'
print(name_ext)
print(name_ext)
print(name_ext)
print(name_ext)
```

Select with *cat* and *sed*:

```
$ cat *\.py | sed -n '/^.*print(\w\+).*$/p'
print(name_ext)
print(name_ext)
print(name_ext)
print(name_ext)
```

### 3. Select from uptime output

Samples of *uptime* output from file *uptime.txt*:

```txt
 08:41:43  up 123 days, 12:14,  5 user,  load average: 1.24, 5.20, 4.31
 07:54:38  up   7:03,  1 user,  load average: 1.70, 1.67, 1.63
```

Selects users with *uptime* and *sed*:

```
$ sed -f users.sed uptimes.txt 
users: 5
users: 1

$ uptime
 09:10:24  up   8:19,  1 user,  load average: 0.24, 0.26, 0.21

$ uptime | sed -f users.sed
users: 1
```

Substitution instructions from file *users.sed*:

```sed
s!^.*\s\+\([0-9]\)\+\s\+user[s]\?.*$!users: \1!
```

Selects days with *uptime* and *sed*:

```
$ sed -f days.sed uptimes.txt 
days: 3
 07:54:38  up   7:03,  1 user,  load average: 1.70, 1.67, 1.63

$ uptime 
 09:14:16  up   8:23,  1 user,  load average: 0.05, 0.17, 0.18

$ uptime | sed -f days.sed 
 09:14:37  up   8:23,  1 user,  load average: 0.04, 0.16, 0.17
```

Substitution instructions from file *days.sed*:

```sed
s!^.*up\s\+\([0-9]\)\+\s\+day[s]\?.*$!days: \1!
```

Selects hours with *uptime* and *sed*:

```
$ sed -f hours.sed uptimes.txt 
hours: 12
hours: 7

$ uptime
 09:16:37  up   8:25,  1 user,  load average: 0.06, 0.14, 0.17

$ uptime | sed -f hours.sed
hours: 8
```

Substitution instructions from file *hours.sed*:

```sed
s!^.*up.*\s\([1-2]\?[0-9]\):[0-5][0-9].*$!hours: \1!
```

Selects minutes with *uptime* and *sed*:

```
$ sed -f minutes.sed uptimes.txt 
minutes: 14
minutes: 03

$ uptime 
 09:24:06  up   8:33,  1 user,  load average: 0.23, 0.39, 0.29

$ uptime | sed -f minutes.sed
minutes: 33
```

Substitution instructions from file *minutes.sed*:

```sed
s!^.*up.*\s[1-2]\?[0-9]:\([0-5][0-9]\).*$!minutes: \1!
```

