from sys import argv

#Here we are getting inputs from the CLI
script,input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count,f.readline(),end = "")

current_file = open(input_file)

print("First let's print the whole file:")
print_all(current_file)

print("Now let's rewing , kind of like a tape")
rewind(current_file)

print("Let's print three lines:")

for current_line in range(3):
    print_a_line(current_line+1,current_file)