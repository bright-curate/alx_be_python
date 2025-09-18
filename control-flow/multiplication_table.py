# multiplication_table.py

# Ask the user to enter a number
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate the table from 1 to 10
for i in range(1, 11):   # loop from 1 to 10
    product = number * i
    print(f"{number} * {i} = {product}")
