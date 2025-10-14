#------------WAP to print the elemnts of list from right to left using positive indices.-----------#


#initialise a list fisrt
list = [1,2,3,4,5,6,7,8,9,10]

#calculate end_index
start_ind = len(list)-1


for i in range(start_ind,-1,-1):
    print(list[i],end=",")