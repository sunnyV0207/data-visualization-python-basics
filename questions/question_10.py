#-------------------------------- WAP to count frequency of each vowel in given sentence. ---------------------#

#take input from user
sentence = input("Enter any sentence: ")

#convert original sentence to lower case
temp_sentence = sentence.lower()

#initialse a vowels string
vowels = "aeiou"

#initialse freaquency of each vowel as 0 in dictionary
frequency = {v:0 for v in vowels}

#increase count
for ch in temp_sentence:
    if(ch in vowels):
        frequency[ch] += 1


#print answers
for v, count in frequency.items():
    if(count > 0):
        print(f"The vowel {v} appears {count} times")