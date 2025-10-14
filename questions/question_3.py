#------------WAP to calculate the average of first 10 natural numbers.-----------#


#initialise a list fisrt
list = [1,2,3,4,5,6,7,8,9,10]

average = 0

for i in range(len(list)):
    average += list[i]

print("Average is: ",average)