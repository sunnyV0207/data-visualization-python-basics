'''
Take any number of input from user and make a list with that and delete occurence of a single element entered by user from list except first occurence.

'''



#Remove duplicates of any number in list except 1st occurence

#initialise a list
numbers = []

#let user enter the elemnts of list
print("Enter numbers to add in list: ")
for i in range(6):
    num = int(input())
    numbers.append(num)


#printcomplete list
print("---------------------------------------------------")
print("List is: ",numbers)


#let user enter the number to delete occurence of:
print("---------------------------------------------------")
number_to_delete = int(input("Enter number to delete occurence of: "))
#print(number_to_delete)


#perform task
occurence = numbers.count(number_to_delete)
if(occurence == 0):
    print("Element does not present in list")
elif(occurence == 1):
    print("Element appears only once in list")
else:
    '''
    end_ind = len(numbers) * (-1)
    while(occurence > 1):
        for i in range(-1,end_ind-1,-1):
            if(numbers[i] == number_to_delete):
                numbers.pop(i)
                occurence -= 1
                break;'''
    numbers.reverse()
    for i in range(occurence-1):
        numbers.remove(number_to_delete)
    numbers.reverse()

print("---------------------------------------------")
print("List is now : ",numbers)
