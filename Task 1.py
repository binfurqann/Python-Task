# Declare two variables, num1 and num2, with any integer values. Use these to calculate their sum and print the result. Understand how variables store numerical values and perform basic arithmetic in Python.
# Taking Input
number1 = int(input("Enter Your First Number"))
number2 = int(input("Enter Your Second Number"))

# Printing Output
print("First Number Is:",number1)
print("Second Number Is:",number2)

a=number1+number2
print(a)

# Create a variable called message and give it a string value. Append the string " World!" to it and print the updated message. Explore basic string operations in Python.
message="Hello"
# Append the string "World!" to it
message+= " World"
print(message)


# Declare a variable is_python_fun and assign it a boolean value
is_python_fun = True  # You can change this to False if you don't find Python fun

# Print a statement based on whether Python is considered fun
a=is_python_fun
b=is_python_fun
print(a==b)

# Create a list called fruits with at least three different fruit names
fruits = ["Apple", "Banana", "Mango"]

# Print the original list
print("the list of fruits:", fruits)

# Add a new fruit to the list
newfruit = "Orange"
fruits.append(newfruit)

# Print the updated list
print("Updated list of fruits:", fruits)

# Declare a variable called price with a floating-point value
price = 27.33

# Convert the floating-point value to an integer
price_as_integer = int(price)

# Print both the original and converted values
print("Original price:", price)
print("Price as an integer:", price_as_integer)

# # Create a dictionary named student_info
student_info = {
    'name': 'Muhammad',
    'age': 17,
    'grade': 'A+'
}

# Print the dictionary
print("Student Information:")
print("Name:", student_info['name'])
print("Age:", student_info['age'])
print("Grade:", student_info['grade'])

