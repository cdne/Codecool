import sys


if len(sys.argv) == 1:
    name = "Hello World!"
    sys.exit(name)
name = "Hello " + sys.argv[1] + "!"
print(name)
