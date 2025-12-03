#def quiz():
    #print("Please type your name to begin")
#Name = input()
#if Name == "Donnell mcgriff":
 

 






#quiz = ["2x2", "1+2", "3x3", "4+4", "4x5"]
#print (quiz)
#for x in quiz:
    #print(x)
    #print("please type your answer")
    #"selection" == input
    #if input == 4:
        #print ("correct")





def quizanswers():
    print("welcome to your quiz")
    quiz = [ 1+1 , 2+2 , 3+3 , 4+4, 5+5]
    answer = []
    answer = input("type your answer please")
    while answer != "quit":
        question = int(answer)
        quiz.append(question)
        print(quiz)
        answer = input("type in a answer")
        if input == 2:
            print("correct")
    else:
        x = sum(quiz)
        print(x)


