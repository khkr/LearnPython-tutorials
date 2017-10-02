#We are going to see local and global variables 

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes_of_crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")
	

print("We can just give the function numbers directly:")
#Here we are passing just numbers
cheese_and_crackers(20,30)

print("Or we can use variables from our script:")

#These are local variables
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print("we can even do math inside too:")
#Turns out even math can be added
cheese_and_crackers(10+20, 5+6)
print("And we can even combine the two , variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)