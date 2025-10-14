#------------WAP to print elements of list from left to right using negative indices.-----------#


#initialise a list fisrt
list = [1,2,3,4,5,6,7,8,9,10]

#calculate end_index
end_ind = len(list) * (-1)


for i in range(-1,end_ind-1,-1):
    print(list[i],end=",")