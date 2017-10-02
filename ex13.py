# We have to provide arguments in the python3 compile command
#Eg: python3 ex13.py first, 2nd, third
from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("The first variable is called:", first)
print("The second variable is called:", second)
print("The third variable is called:", third)
