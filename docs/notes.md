# 🐍 Python Notes — From Basics to Lists

---

## ✨ Introduction to Python

Python is a **high-level**, **interpreted**, and **object-oriented** programming language known for its simplicity and readability.  
It is widely used in:
- 💻 Software Development  
- 🌐 Web Development  
- 📊 Data Science  
- 🤖 Machine Learning  
- 🔬 Scientific Computing  

---

## ⚙️ Python Basics

python
# This is a single-line comment

"""
This is a
multi-line comment
"""

# ------------------------------------- 📥 Input and Output ------------------------------#

# Output
print("Hello, World!")

# Input
name = input("Enter your name: ")
print("Welcome,", name)


# ----------------------------------- 🧮 Variables and Data Types -------------------------#

Python variables are created when you assign a value:

x = 10           # Integer
y = 3.14         # Float
name = "Alice"   # String
is_active = True # Boolean

You can check the type of a variable using:
print(type(x))  # <class 'int'>


# ------------------------------- 🧺 Lists in Python ----------------------------------#

A List is an ordered, mutable collection that can hold elements of different data types.

🧱 Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

🧩 Accessing List Elements
fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple
print(fruits[-1])  # cherry


🔁 Modifying Lists
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

🧰 List Methods (with Examples)

➕ 1. append()

Adds an element to the end of the list.

fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']


🧱 2. insert()

Inserts an element at a specific position.

fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana']

🧹 3. remove()

Removes the first occurrence of a specified element.

fruits.remove("apple")
print(fruits)  # ['mango', 'banana']


❌ 4. pop()

Removes the element at a specified index (or last if not specified).

fruits.pop()      # removes last item
fruits.pop(0)     # removes first item

🔄 5. reverse()

Reverses the list in place.

numbers = [1, 2, 3]
numbers.reverse()
print(numbers)  # [3, 2, 1]


🔢 6. sort()

Sorts the list in ascending order (by default).

numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

For descending order:
numbers.sort(reverse=True)

➕ 7. extend()

Adds elements from another iterable (like list, tuple) to the end.

a = [1, 2, 3]
b = [4, 5]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5]


🧮 8. count()

Returns the number of occurrences of an element.

nums = [1, 2, 2, 3]
print(nums.count(2))  # 2


🧭 9. index()

Returns the index of the first occurrence of an element.

fruits = ["apple", "banana", "cherry"]
print(fruits.index("banana"))  # 1


🧽 10. clear()

Removes all elements from the list.

fruits.clear()
print(fruits)  # []


📋 11. copy()

Returns a shallow copy of the list.

fruits = ["apple", "banana"]
new_list = fruits.copy()
print(new_list)  # ['apple', 'banana']


⚙️ 12. len()

(Not a method, but commonly used)
Returns the number of elements in a list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

🌟 List Comprehension

A concise way to create lists.

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]


🧩 Nested Lists

Lists inside lists.
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[0][1])  # 2


# --------------------Questions to practice for lists-------------------------#

1.WAP to print elements of list from left to right using negative indices.
Sol:- [View Solution](../questions/question_1.py)

2.WAP to print the elemnts of list from right to left using positive indices.
Sol:- [View Solution](../questions/question_2.py)

3.WAP to calculate the average of first 10 natural numbers.
Sol:- [View Solution](../questions/question_3.py)

4.WAP to calculate the average of 10 numbers entered by the user.
Sol:-[View Solution](../questions/question_4.py)

5.Create a reportcard . It must contain the name of five subjects along with marks obtained in them out of 100.
Then calculate the total marks obtained, percentage, grade.
Grade must be calculated as per below criteria :-
Percentage           Grade
>=85                   A+
85 - 75                A
75-65                  B
65 - 55                C
55 - 50                D
<50                    Fail
Sol:- [View Solution](../questions/question_5.py)

6.Take any number of input from user and make a list with that and delete occurence of a single element entered by user from list except first occurence.
Sol:- [View Solution](../questions/question_6.py)




# ------------------------------- 🧺 String in Python ----------------------------------#

String is a sequence of characters enclosed with single, double and triple quotes

Syntax:- Name="Sunny Verma"

🧰 String Methods (with Examples)

1.isalpha():- returns True if string contains only alphabets otherwise false
Exm:- str = "sunny"                     Exm:- str="sunny156"
ans:- true                              Ans:- false

2.isdigit():- return True if string contains only digits
Exm:- str = "78"                     Exm:- str="sunny156"
ans:- true                           Ans:- false

3.isalnum():- return true if string contains either alphabets or numbers or both
Exm:- str = "sunny"                     Exm:- str="sunny156"
ans:- true                              Ans:- true

4.isspace():- return true if string contains only space
Exm:- str = " "                     Exm:- str="sunny156"
ans:- true                              Ans:- false

5.islower():- return true if string contains only smaller case letter
Exm:- str = "sunny"                     Exm:- str="Sunny"
ans:- true                              Ans:- false

6.isupper():- return true if string contains only uppercase characters
Exm:- str = "sunny"                     Exm:- str="SUNNY156"
ans:- false                             Ans:- true     //bcz it do not check for digits

7.istitle():- return true if string contains some words and each word has its first letter capital and rest are in small case
Exm:- str = "Sunny"                     Exm:- str="Sunny Verma 156"
ans:- true                             Ans:- true     //bcz it do not check for digits

8.lower():- return original string in lower case
Exm:- str = "Sunny"                     Exm:- str="Sunny Verma 156"
ans:- "sunny"                           Ans:- "sunny verma 156"     //bcz it do not check for digits

9.upper():- return original string in upper case
Exm:- str = "Sunny"                     Exm:- str="Sunny Verma 156"
ans:- "SUNNY"                           Ans:- "SUNNY VERMA 156"     //bcz it do not check for digits

10.title():- return original string in title case
Exm:- str = "Sunny"                     Exm:- str="sunny verma"
ans:- "Sunny"                             Ans:- "Sunny Verma"     //bcz it do not check for digits

11.swapcase():- return original string in case to convert upper to lower and vice versa
Exm:- str = "Sunny"                     Exm:- str="sunny verma"
ans:- "sUNNY"                             Ans:- "SUNNY VERMA"     //bcz it do not check for digits

# --------------------Questions to practice for Strings -------------------------#

1.WAP to count number of aphabets in given sentence.
Sol:- [View Solution](../questions/question_7.py)

2.WAP to count number of uppercase characters in given sentence.
Sol:- [View Solution](../questions/question_8.py)

3.WAP to count number of vowels in given sentence.
Sol:- [View Solution](../questions/question_9.py)

4.WAP to count frequency of each vowel in given sentence.
Sol:- [View Solution](../questions/question_10.py)

5.WAP to count number of special characters in given sentence.
Sol:- [View Solution](../questions/question_11.py)