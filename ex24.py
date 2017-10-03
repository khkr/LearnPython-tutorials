print("Let's practise everything.")

print('You\'d need to know \'bout escapes with \\that do:')

print('\n newlines and \t tabs.')

poem = """ 
\tThe lovely world with logic so firmly planted cannot discern\n the needs of love nor comprehend passion from intuition and requires an explanation\n\t where there is none.
"""
print("-"*15)
print(poem)
print("-"*15)

five = 10 - 2 +3 - 6
print(f"This should be {five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans/1000
    crates = jars/100

    return jelly_beans, jars, crates

start_point = 10000

beans,jars,crates = secret_formula(start_point)

#This is another format to print a string

print("With a starting point of{}".format(start_point))

#This is the way we generally use
print(f"We'll have {beans} beans , {jars} jars and {crates} crates ")

start_point = start_point/10

print("We can also do this anothe way too")

formula = secret_formula(start_point)

#This is amazing way , make note KHKR

print("We'll have {} beans , {} jars and {} crates".format(*formula))