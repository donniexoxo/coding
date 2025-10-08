# list = a collection system for storing and organizing multiple
# pieces of data

# list syntax (how it is written)
# when we want to create a list, we first create a variable, and then
# assign it to the square brackets [].

# [] = square brackets means list

shoppinglist = ['apples', 'oranges', 'water',1,2,3,true,["bread", "milk"]]

print(shoppinglist)

# if we want to acccess an item from a list, we use the index system
# we write the list variable




#print(shoppinglist[2])

trunkparty = ['fan','Mini-fridge','laptop','TV','Air fryer']

def additemforcollege(list):
    newitem = input ("please add a new item to the college trunk party list:")
    list.append(newitem)
    print(list)

additemforcollege(trunkparty)

# create a function that will remove an item from the trunk party list
# use w3schools to find a list methond 