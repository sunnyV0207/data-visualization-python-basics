#-------------------- Question --------------------------#
'''
Create a reportcard . It must contain the name of five subjects along with marks obtained in them out of 100.
Then calculate the total marks obtained, percentage, grade.
Grade must be calculated as per below criteria :-
Percentage           Grade
>=85                   A+
85 - 75                A
75-65                  B
65 - 55                C
55 - 50                D
<50                    Fail

'''


#------------------------ solution --------------------------#

#take input from user fo subject_count, subject_names and marks in respective subjects

subject_count = int(input("Enter number of subjects to prepare reportcard for: "))
data = []

if(subject_count >= 1):
    for i in range(subject_count):
        subject_name = input(f"Enter subject {i+1} name: ")
        if(subject_name.isalpha()):
            marks = int(input("Enter marks obtained: ",))
            if(marks >= 0 and marks <= 100):
                data.append([subject_name,marks])
            else:
                print("Invalid marks")
                break
        else:
            print("Subject name must be a string")
            break
else:
    print("Invalid subject_count")


#count total marks and total obtained marks
total_marks = subject_count * 100
total_obtained_marks = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if(j==1):
            total_obtained_marks += data[i][j]



#Printing output
print("-------------------- Result ----------------------")
print("Total obtained marks: ",total_obtained_marks)


#count percentage for marks
percentage = ((total_obtained_marks/total_marks) * 100)
print("Percentage: ",percentage)


#Assign Grade to student
scores = [ m[1] for m in data ]
if all(score >= 35 for score in scores ):

    if(percentage >= 85):
        print("Grade A+")
    elif(percentage >= 75 and percentage < 85):
        print("Grade A")
    elif(percentage >= 65 and percentage < 75):
        print("Grade B")
    elif(percentage >= 55 and percentage < 65):
        print("Grdae C")
    elif(percentage >= 45 and percentage < 55):
        print("Grade D")
    else:
        print("Fail")
else:
    print("Fail")