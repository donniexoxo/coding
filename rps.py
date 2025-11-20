"should be able to tell which is which"
"be able to know whos the winner"
"it will be able to loop"



# how will the program work
"welcome the user to the game"
"give them the option to play the game or look at game tutorials"
"is user select rules, show them the rules, else start the game"
"inform the user the game has started and ask them to make a selection;"
"computer makes a random selection"
"determine and the user/player if they won,lose,or tied "
"and keep track of score and round"







def rpsdgame():
    print("welcome to rock paper scissor: the game!")
    print("please select one of the following: ")
    print ("enter, p to start game, ")
    print ("or enter to rules")
    selection = input()
    if selection == 'r':
        print("here are the game rules . . .")
    elif selection == 'p':
        print('the game is starting . . .')
        choice = input("please make a selection, r = rock, p = papaer, s = scissor")
        choicecui = random.choice(rpsoptions_cpu)
        print("user selecten " + choice)
    
    else:
        print('sorry, we didint understand your entry')
        choice = input("")