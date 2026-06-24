from clear_cls import *
from files import *

sstudents = []

Option = """
What is the student's status?
1. Asset
2. Idle
        """



#'''Function to add a product to the inventory. Asks the user for the product name, price and quantity.
#It validates the inputs and checks if the product already exists.'''
def addStudent ():

    validation=True

    print("Register a new student")
    print("--------------------------------")

    while validation:
        try:
            id=int(input("Please, Enter the new student's ID: "))

            if id:
                for student in sstudents:
                    if student['id'] == id :
                        clearScreen()
                        print(f"The ID ({id}) is already registered \n")
                        print(f"ID Student: {student['id']} \n" \
                            f"Name Student: {student['name'].capitalize()}")
                        validation=False

                break

            else:
                print()
                print("Error! You must enter a ID.") 
                print()

        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    while validation:
        name=input("Please, Enter the new student's name: ").lower().strip()  #Enter the student's name and converts everything to lowercase
        if name:    #Verify that the user has entered something
            
            break
            
        else: 
            print()
            print("Error! You must enter the new student's name.") 
            print()

    while validation:
        try:
            age=int(input("Please, Enter the new student's age: "))

            if age:

                break

            else: 
                print("Error! You must enter a age.")

        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    while validation:
        course=input("Please, Enter the new student's couse: ").lower().strip()  #Enter the student's name and converts everything to lowercase
        if course:    #Verify that the user has entered something
            
            break
            
        else: 
            print()
            print("Error! You must enter the new student's course.") 
            print()

    while validation:

        print(Option)

        try:
            intStatus=int(input("Please, Enter the new student's status: "))  #Enter the student's name and converts everything to lowercase

            if intStatus== 1:    #Verify that the user has entered something

                status=True
                break
                
            elif intStatus== 2:
                status=False
                break
                
            else: 
                print()
                print("Error! wrong option. Try Again") 

        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    if validation: 
        student={   #If the product is not already in the inventory, it creates a new product with the entered name, price and quantity and adds it to the inventory list.
        'id' : id,
        'name' : name,
        'age' : age,
        'course' : course,
        'status' : status
        }

        sstudents.append(student)   #Add the new product to the list

        print()
        print("Student added successfully!")

def theStudentsList():
    return sstudents

def showTheStudentsList():

    number=0
    
    print("The Students List")
    print("--------------------------------")
    if sstudents: 
        for student in sstudents:    #Scroll through the product list and display each product with its price and quantity.
            number += 1
            if student['status']==True:
                Status='Asset'
            else: Status='Idle'

            print(f"Student {number} \n" \
                f"ID: {student['id']} \n" \
                f"Name:  {student['name'].capitalize()} \n" \
                f"Age: {student['age']} \n" \
                f"Course: {student['course'].capitalize()} \n" \
                f"Status: {Status.upper()}\n"\
                "")
            
        print("--------------------------------")
        print()

    else: print("There are no products yet"), print("--------------------------------"), print()

def searchStudent ():
    validation = True

    print("Search Product")
    print("--------------------------------")
        
    if sstudents:  
        try:
            searchID=int(input("Please, Enter the ID of the student you wish to search: "))

            if searchID:
                for student in sstudents:    #Scroll through the product list and display each product with its price and quantity.
                    if student['id'] == searchID:

                        print()
                        print("--------------------------------")

                        if student['status']==True:
                            Status='Asset'
                        else: Status='Idle'

                        print(f"ID: {student['id']} \n" \
                            f"Name:  {student['name'].capitalize()} \n" \
                            f"Age: {student['age']} \n" \
                            f"Course: {student['course'].capitalize()} \n" \
                            f"Status: {Status.upper()}" )
                        
                        print("--------------------------------")
                        
                        break

                    elif student == sstudents[-1]:
                        print()
                        print(f"The ID ({searchID}) has not been found")

            else:
                print()
                print("Error! You must enter a ID.") 
                print()

        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    else: print("There are no products yet")

def updateStudent():

    validation=True
    menu='''What do you want to update?
1. Name
2. Age
3. Course
4. Status
0. Cancel
Please, choose an option: '''

    print("Update Student Data ")
    print("--------------------------------")
        
    if sstudents: 
        while validation: 
            try:
                searchID=int(input("Please, Enter the ID of the student you wish to update: "))
            
                for student in sstudents:    #Scroll through the product list and display each product with its price and quantity.
                    if student["id"] == searchID:
                        print()
                        print("--------------------------------")

                        if student['status']==True:
                            Status='Asset'
                        else: Status='Idle'

                        print(f"ID: {student['id']} \n" \
                            f"Name:  {student['name'].capitalize()} \n" \
                            f"Age: {student['age']} \n" \
                            f"Course: {student['course'].capitalize()} \n" \
                            f"Status: {Status.upper()}" )
                        
                        print("--------------------------------")

                        while validation: 
                            try:    #Catch the error if there is one and repeat the request
                                print()
                                option = int(input(menu))    #Request an option and this must be an integer value
                                if option == 1 :    #It allows the user to update the name of the product
                                    while validation:
                                        print()
                                        print("---------------------------------")
                                        print(f"The actual name is: {student['name'].capitalize()}")
                                        newFeature=input(f"Please, enter the new name of the student ({student["name"].capitalize()}): ").lower().strip()
                                        if newFeature:
                                            print("--------------------------------")
                                            student["name"] = newFeature
                                            print(f"The new name is: {student["name"].capitalize()}")
                                            print("--------------------------------")
                                            print("¡Updated Name!")
                                            validation=False
                                        else: 
                                            print()
                                            print(f"Error! You must enter the new name of the student ({student["name"].capitalize()})") 
                                
                                elif option == 2:
                                    print()
                                    while validation:
                                        try:
                                            print("---------------------------------")
                                            print(f"The actual age is {student["age"]} of the student {student["name"].capitalize()}")
                                            newFeature=int(input(f"Please, enter the new age of the student ({student["name"].capitalize()}): "))
                                            if newFeature<=0: #Verify that the value is greater than 0
                                                print()
                                                print("The age must be greater then zero")
                                                print()
                                                continue
                                            print("--------------------------------")
                                            student["age"] = newFeature
                                            print(f"The new age is: {student["age"]} of the student {student["name"].capitalize()}")
                                            print("--------------------------------")
                                            print(f"¡Updated age!")
                                            validation=False

                                        except ValueError:
                                            print()
                                            print("Error! Type a number")
                                            print()

                                elif option == 3:
                                    while validation:
                                        print()
                                        print("---------------------------------")
                                        print(f"The actual course is: {student['course'].capitalize()}")
                                        newFeature=input(f"Please, enter the new course of the student ({student["name"].capitalize()}): ").lower().strip()
                                        if newFeature:
                                            print("--------------------------------")
                                            student["course"] = newFeature
                                            print(f"The new course is: {student["course"].capitalize()}")
                                            print("--------------------------------")
                                            print("¡Updated course!")
                                            validation=False
                                        else: 
                                            print()
                                            print(f"Error! You must enter the new name of the student ({student["name"].capitalize()})") 

                                elif option == 4:
                                    while validation:
                                        if student['status']==True:
                                            Status='Asset'
                                        else: Status='Idle'

                                        print()
                                        print("---------------------------------")
                                        print(f"The actual status is: {Status}")
                                        while validation:

                                            print(Option)

                                            try:
                                                intStatus=int(input("Please, Enter the new student's status: "))  #Enter the student's name and converts everything to lowercase

                                                if intStatus== 1:    #Verify that the user has entered something

                                                    student['status']=True
                                                    print("--------------------------------")
                                                    print(f"The new status is: {Status}")
                                                    print("--------------------------------")
                                                    print("¡Updated Status!")
                                                    validation=False
                                                    break
                                                    
                                                elif intStatus== 2:
                                                    student['status']=False
                                                    print("--------------------------------")
                                                    print(f"The new status is: {Status}")
                                                    print("--------------------------------")
                                                    print("¡Updated Status!")
                                                    validation=False
                                                    break
                                                    
                                                else: 
                                                    print()
                                                    print("Error! wrong option. Try Again") 

                                                if student['status']==True:
                                                    Status='Asset'
                                                else: Status='Idle'

                                            except ValueError:
                                                print()
                                                print("Error: Please enter a valid numeric value")
                                                print()
                                                

                                elif option == 0:
                                    validation=False

                                else:
                                    print("Invalid option. Try again")  
                                    print()

                            except ValueError:  #Catch the error if there is one and repeat the request
                                print("Error! Type a number")
                                print()
                        
                    elif student == sstudents[-1] and validation: #If the product is not found after scrolling through the entire list, it displays a message indicating that the product was not found.
                        print()
                        print(f"The ID student {searchID} has not been found")
                        validation=False

            except ValueError:
                print()
                print("Error: Please enter a valid numeric value")
                print()

def deleteStudent():
    validation=True

    print("Delete Student")
    print("--------------------------------")
        
    if sstudents: 
        try:
            searchID=int(input("Please, Enter the ID of the student you wish to delete: "))

            if searchID:
                for student in sstudents:    #Scroll through the product list and display each product with its price and quantity.
                    if student['id'] == searchID:

                        print()
                        print("--------------------------------")

                        if student['status']==True:
                            Status='Asset'
                        else: Status='Idle'

                        print(f"ID: {student['id']} \n" \
                            f"Name:  {student['name'].capitalize()} \n" \
                            f"Age: {student['age']} \n" \
                            f"Course: {student['course'].capitalize()} \n" \
                            f"Status: {Status.upper()}" )
                        
                        print("--------------------------------")

                        while validation:
                            print()
                            confirmation=input(f"Are you sure you want to delete the student {student["name"].capitalize()}? (Yes or No): ").lower().strip()
                            if confirmation == "yes":
                                sstudents.remove(student)
                                print()
                                print(f"The student {student["name"].upper()} has been deleted")
                                validation=False
                            elif confirmation == "no":
                                print()
                                print(f"The student {student["name"].upper()} has not been deleted")
                                validation=False
                            else:
                                print("Invalid option. Try again")  
                                print()
                        
                        break

                    elif student == sstudents[-1]:
                        print()
                        print(f"The ID ({searchID}) has not been found")
                        break

            else:
                print()
                print("Error! You must enter a ID.") 
                print()

        except ValueError:
            print()
            print("Error: Please enter a valid numeric value")
            print()

    else: 
        if validation:
            print("There are no products yet")
