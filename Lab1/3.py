python=set() #set that contains students names who are in python class
webapp=set() #set that contains students names who are in Web Application class
while True:
    student=input("enter student name who is in python class")
    python.add(student)                        # adding all the students
    choise= input("do you wish to add more students(y/n)")
    if choise.lower().__eq__('y'):
        continue
    else:
        break
while True:
    student1=input("enter student name who is in web application class")
    webapp.add(student1)
    choise1= input("do you wish to add more students(y/n)")
    if choise1.lower().__eq__('y'):
        continue
    else:
        break
print("students in python class are :", python)
print("students in web application class are :",webapp)
print("students attending both the classes are :",python&webapp)   # printing the students common in both classes using & operation
print("students not common in both the classes are: ",python ^ webapp) # printing the students common in both classes using ^ operation