#build gpa calculator 
# take in numbers and average them out based on numbers given.

# 2. take in subject area as string.





#def gpacalculator():
    #print("which subject is the gpa for")
    #subject = input()
    #print('the subject is ' + subject)
    #gradelist = []
    #week = 1
    


def gpacalculator():
    grade = 0
    print("which subject is the gpa for")
    subject = input()
    print('the subject is ' + subject)
    print('please enter a grade for week 1')
    week1grade= input()
    print(week1grade)
if gpacalculator():
    grade = +1
    print('what subject id this grade for')
    subject = input()
    print('the subject is' + subject)
    print('please enter a grade for week 2')
    week2grade= input()
    print(week2grade)


def gpaCalculator():
    print(' What subject is this GPA for? ')
    subject = input()
    print("the user entered: "+ subject)
    week = 1
    sum = 0
    for x in range (18):
        print('Please enter the grade for week : '+ str(week))
        grade = int(input())
        sum += grade
        week += 1
        gpa = sum / 10
    if gpa > 70 and gpa < 80:
        print('C')
    elif gpa > 80  and gpa < 90:
        print('B')
    elif gpa > 90  and gpa <100:
        print('A')
    else:
        print('F')
    print('your gpa for '+ subject + ' is ' + str(gpa))












gpacalculator()