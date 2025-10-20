# while loop definition -  a while loop is a type of construct
# where code instructions will keep on running so
# long as a condition is TRUE (boolean)

# NOTE - In order to stop a loop (or any program) from running
# in you terminal, click crtl + c at the same time

# while loop syntax

agetobuygame = 17
customerage = int(input("how old are you: "))

while agetobuygame >= customerage:
    print("sorry, your not old enough to buy GTA VI")
else:
    print("great enjoy your collectors edition of GTA VI!")



savedpassword = '123Abc'
userpassword = input("please tipe in your password: ")
attempt = 1
while savedpassword != userpassword:
    print("incorrect try agian please. ")
    attempt += 1
    print('attempts:' + str(attempt))
    userpassword = input ("please type in your password agian: ")
    if attempt








number = 0
while number < 10:
    number += 1
    print(number)
else:
    print('done counting ')


# create a while loop that counts down from 30 by 1

number = 30
while number > 0:
    number = 1
    print(number)
else:
    print('done counting')
