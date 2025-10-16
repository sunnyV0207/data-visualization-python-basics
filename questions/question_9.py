# -------------------------------- WAP to count number of vowels in given sentence. -----------------#


#take a sentence as input
sentence = input("Enter any sentence: ")

#initialse a input string for vowels
vowels = "aeiouAEIOU"

#initialise vowel count as 0
vowel_count = 0

#increase count
for ch in sentence:
    if(ch in vowels):
        vowel_count += 1


#print count
print("Vowel count is: ",vowel_count)