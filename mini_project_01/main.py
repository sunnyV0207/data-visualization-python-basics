print("\n\n" + "-" * 71)
print("----------------------------Student Portal-----------------------------\n")


#initialise list for operations user can perform
operations = [
    "Registration of new student",
    "Student profile",
    "Delete student",
    "List of all students sorted as per standard",
    "List of students of particular standard",
    "List of students with attendance greater then 50% standard wise"
    ]

#print list for user to select any one operation
for i in range(1,len(operations)+1):
    print( str(i) + "." + operations[i-1] ) 

print("\n" + "-" * 71)



#-------------------------------------------------------------------------------------------

#make functions for particular operations

def register_student():
    print("--------------------Student Registration-------------------")
    return

def student_profile():
    print("--------------------Student Profile-------------------")
    return

def delete_student():
    print("--------------------Delete Student-------------------")
    return

def list_all_students():
    print("--------------------List of all Students-------------------")
    return

def list_students_of_standard():
    print("--------------------List of all Students for particular standard-------------------")
    return

def list_high_attendance():
    print("--------------------List of all Students with attendance greater than 50%-------------------")
    return


#store these functions in a list
functions = [
    "register_student",
    "student_profile",
    "delete_student",
    "list_all_students",
    "list_students_of_standard",
    "list_high_attendance"
    ]

#let the user select any one operation out of all the above
selected_operation = int(input("Select any one operation: "))
if selected_operation not in range(1,len(operations)+1):
    print("Invalid operation")
else:
    # print("Valid operation")
    print("-" * 71)
    functions[selected_operation-1]()
