from sys import argv

name_ext = argv[0]
name = name_ext[:-3]
ext = name_ext[-3:]

name = name[1:] + name[0]
name_ext = name + ext

print(name_ext)

