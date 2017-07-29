#It uses command something akin to argv
def print_two(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" %(arg1, arg2))

#Same kind of one but from different perspective
def print_two_again(arg1,arg2):
	print("arg1: %r, arg2: %r" %(arg1, arg2))

#take one argument
def print_one(arg1):
	print("arg1: %r" % arg1)

#no arguments
def print_none():
	print("No arguments here")

print_two("KHKR","F Semicolon")
print_two_again("Harish", "Pavan")
print_one("Best")
print_none()