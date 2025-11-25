#def gradecheck(grade):
   #if grade >=90:
      #print("your grade is an A")
   #elif grade >=80:
      #print("you have a B")
   #elif grade >=70:
      #print("your grade is a C")
   #else:
      #print("you have an F")

#gradecheck(69)

#Kg = 0
#while Kg < 100:
   #Kg += 2.2
   #print(Kg)

def removeitemfromlist():
    Jadens_backpack = ["snacks", "soda", "binder", "pens", "notebook"]
    item = input("please type what item you want to remove")
    Jadens_backpack.remove(item)
    item = input("please tpye items you want to add")
    Jadens_backpack.append(item)
    ptint (Jadens_backpack)