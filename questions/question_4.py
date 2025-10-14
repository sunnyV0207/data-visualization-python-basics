#------------WAP to calculate the average of 10 numbers entered by the user..-----------#


#initialise a empty list fisrt
list = []

#take input from user
print("Enter numbers for list: ",end=" ")

for i in range(10):
    num = int(input())
    list.append(num)

print("List is: ",list)


#find average of those numbers
average = 0

for i in range(len(list)):
    average += list[i]

print("Average is: ",average)