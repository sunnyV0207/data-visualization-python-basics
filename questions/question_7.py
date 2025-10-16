# ---------------------- WAP to count number of aphabets in given sentence. ---------------------#


#take sentence as input from user
str = input("Enter any sentence: ")


#initialise alpha_count as 0
alpha_count = 0

#increase alpha_count if char is alphabet
for i in str:
    if(i.isalpha()):
        alpha_count += 1


#print alpha_count
print("Alpha Count is : ",alpha_count)