from sys import argv

script, file_name = argv
#We are opening a file here and if it doesn't exist it'll be created
#When we use 'w' it'll wipe the entire file and we have to start fresh
f = open(file_name,'w+')

for i in range(10):
    f.write(f"This is line {i+1}\n")
f.close()



