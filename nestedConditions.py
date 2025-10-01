# nested conditions = a conditional staemnet that has other conditional
# staements within it. conditions inside of conditions.

def sandwichStore():
    print("welcome to Ian foods. what would you like")
    selection = input(" please select your main food item? ")
    print("1.meatball sandwich")
    print("2 turkey sandwich ")
    print("3. honey turkey sandwich ")
    print("4. buffallo chicken")
    print("5. surprise me (mystery sandwich)")
    selection = input("please select your main food item")
if selection ==1:
    print("youve selected the meatball sandwich.")
    print("what sides do you want? ")
    print("1. fries")
    print("2. salad")
    print("3 chips ")
    side = int(input())
    if side == 1:
        print("great meatball and fries")
    elif side == 2:
        print("healthy! meatball and salad")
    elif side == 3:
        print("nice, meatball and chips")
    else:
        print("sorry, dont understant")










def atm():
    balance = 2000
    pin = 1234

    userPin = input("please type in your bank pin number")
    if userPin == pin:
        print("welcome. what would you like to do? ")
        print(" withdrawl money")
        print("deposit money")
        print(" check your balence")
        selection = int(input())
        if selection ==1:
            amount = int(input("how much do you want to take out"))
            if amount > balence:
                print("sorry, you dont have that much in your account")
            else: