the_count = [1,2,3,4,5]
fruits = ['pears','oranges','apricots','mangoes']
change = [7,'paise',2,'rupees',5,'hundred']

for number in the_count:
    print(f"Let's see : {number} ")

for fruit in fruits:
    print(f"Fruited : {fruit} ")

#We can even print a mixed list that's awesome
for i in change:
    print(f"I have some change: {i} ")

#Now let's try to fill a list

elements = []

for i in range(6):
    print(f"Adding {i+1} to the list")
    elements.append(i+1)

#We are printing the elements too

for i in elements:
    print(f"Here: {i} ")

