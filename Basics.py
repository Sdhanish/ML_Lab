# 1. Basic Arithmetic Operations
def arithmetic_operations(a, b):
    print(f"\nArithmetic Operations with a={a} and b={b}:")
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b if b != 0 else "undefined (division by zero)")
    print("Modulus:", a % b if b != 0 else "undefined (modulus by zero)")
    print("Exponent:", a ** b)

# 2. Conditionals
def check_even_odd(num):
    print(f"\nChecking if {num} is even or odd:")
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# 3. Loop Example: Sum of List Elements
def sum_list_elements(numbers):
    total = 0
    for number in numbers:
        total += number
    print(f"\nSum of the list elements {numbers}: {total}")

# 4. Function to Calculate Factorial (using recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 5. List Operations
def list_operations():
    fruits = ["apple", "banana", "cherry"]
    print("\nOriginal List of Fruits:", fruits)

    # Add an element
    fruits.append("date")
    print("After adding 'date':", fruits)

    # Remove an element
    fruits.remove("banana")
    print("After removing 'banana':", fruits)

    # Access elements
    print("First fruit:", fruits[0])
    print("Last fruit:", fruits[-1])

# 6. Dictionary Operations
def dictionary_operations():
    student = {"name": "Alice", "age": 20, "major": "Computer Science"}
    print("\nDictionary of Student Information:", student)

    # Access a value
    print("Student's Name:", student["name"])

    # Add a new key-value pair
    student["grade"] = "A"
    print("After adding grade:", student)

    # Update a value
    student["age"] = 21
    print("After updating age:", student)

    # Remove a key-value pair
    del student["major"]
    print("After removing major:", student)

# 7. Input/Output
def user_input_output():
    print("\nUser Input and Output:")
    name = input("Enter your name: ")
    print("Hello, " + name + "!")

# Main program to run all functions and demonstrate basic Python operations
if __name__ == "__main__":
    # 1. Arithmetic operations
    arithmetic_operations(10, 5)

    # 2. Check if a number is even or odd
    check_even_odd(7)

    # 3. Sum elements of a list
    sum_list_elements([1, 2, 3, 4, 5])

    # 4. Calculate factorial
    number = 5
    print(f"\nFactorial of {number} is:", factorial(number))

    # 5. List operations
    list_operations()

    # 6. Dictionary operations
    dictionary_operations()

    # 7. Input/Output
    user_input_output()
