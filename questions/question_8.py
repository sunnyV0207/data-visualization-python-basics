# ----------------------- WAP to count number of uppercase characters in given sentence. --------------#


#take a sentence as input
sentence = input("Enter sentence: ")


#initialise upper count as 0
upper_count = 0


#increase count if character is in uppercase
for ch in sentence:
    if(ch.isupper()):
        upper_count += 1


#print count
print("Upper count in sentence is : ",upper_count)