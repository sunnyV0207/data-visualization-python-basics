#Write a program in python to create a list of 10 number  given by user and display 2nd and 3rd largest value without using sort function

#initialise a list and let the user enter 10 numbers in the list
numbers = []
print("Enter 10 numbers to add in the list:",end=" ")
for i in range(10):
    num = int(input())
    numbers.append(num)

print("-"*71)
print("List created by user: ",numbers)

#sort list in ascending order
for i in range(len(numbers)):
    min_index = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_index]:
            min_index = j
    # swap
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("List after sorting in ascending order: ",numbers)


#print second and thirs largest element
print("-"*71)
unique_numbers = sorted(set(numbers))
#print(unique_numbers)
print("Second largest element from list is: ",unique_numbers[len(unique_numbers)-2])
print("Third largest element from list is: ",unique_numbers[len(unique_numbers)-3])
    