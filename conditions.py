# conditional statements=code that has a set of different
# outcome nased on the data that is give

#Condtional syntax= if/ else
#If = the condition we are looking to satisfy

# Else= the default/exit. the thing that happens
#when our condition is NOT satisfied


weather=input('whats the weather like today ?')

if weather== 'sunny':
    print('Its gonna be nice out. wear shades.')
elif weather=="rainy":
    print("remeber to bring an umbrella.")
elif weather== "chilly":
    print('bring a jacket.')
else:
    print("Have a good day.")

#create a conditional block of code that acts as a 
#password checker. the user should be able to input a
#password. if it is correct, they should get a message
#saying "welcome, you are logged in".otherwise, they
#should get a message saying "try again".

password=input('please enter your password.')

if password== "abc123":
    print('welcome! you are logged in.')
else:
    print('incorrsct password.')