from services import *
import csv


def loadCSV ():
    try:
        with open('list_students.csv', mode='r') as file:
            reader = csv.DictReader(file)
            students = []

            for row in reader:
                
                student = {
                    'id': row['ID'],
                    'name': row['Name'],
                    'age': row['Age'],
                    'course': row['Course'],
                    'status': row['Status']
                }

                students.append(student)

            return students
        
    except FileNotFoundError:
        print("Error: Could not find the file to save the inventory.")
        return []    
    
