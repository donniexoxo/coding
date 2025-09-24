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





down = input("what down is it?")
yards = input("how man yards do you need to get another first down?")

if down ==3 and yards < 10:
    print("bomb the ball- pass")
elif down == 2 and yards < 8:
    print('short pass')
elif down == 3 and yards > 10:
    print('run it')
else:#this is the exit; assumes it is 4th dowm
    print("punt")


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


age=17

if age == 17 and age > 17:
    print("allowed to get permint")
elif age == 14 and age > 14:
    print('is not allowed to get there permint')



def permitcheck(age):
    if age >= 16:
        print("congrats, you can begin learning to drive.")