# function needs to have a list of 4 words
#function needs to take 1 word from list randomly
# selected words needs to be randomized/ shuffled
# allow user to guess the original / correct word
# if it is correct, they else they lose

def scramlewordgame():
    wordpool = ["pennsylvania", "north carolina", "congregate", "function"]
    print("welcome to word scramble!")

    randomwordselect = random.randint(0,3)
    correctword =
    if randomworlselect == 0:
        print(wordpool[0])

    elif randomworlselect == 1:
        print(wordpool[1])

    elif randomworlselect == 2:
        print(wordpool[2])

    elif randomworlselect == 3:
        print(wordpool[3])
    
    convertedselection = list(correctword)
    random.shuffle(convertedselection)
    scrambled = "".join(convertedselection)
    print("guess the correct word" + scrambled)
    userguess = input()
    if userguess == correctword:
        print("this is corrrect")
    else:
        ptint("this is wrong")

    print(convertedselection)





scramblewordgame()