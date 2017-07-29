#Checking to see how we can use direct values and variables 
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have %d cheeses" %cheese_count)
	print("You have %d boxes of crackers" %boxes_of_crackers)

#Direct Values here
print("We can give the function argument values directly:")
cheese_and_crackers(20,40)

print("Or we can even use variables")

#Variables here
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#We can also add values and variables too
print("We can combine the variables and do math too")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)