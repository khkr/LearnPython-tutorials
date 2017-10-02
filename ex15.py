#This line gets argv which is used to pass arguments in the command line
from sys import argv

#Files name
script, filename = argv

#Extracts the files
txt = open(filename)

print(f"Here's your file {filename}:")
print("-"*15)
print(txt.read())
print("-"*15)
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print("-"*15)
print(txt_again.read())
print("-"*15)
