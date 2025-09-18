# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start with the first row
row = 0

# Use a while loop to go through each row
while row < size:
    # For each row, print stars using a for loop
    for col in range(size):
        print("*", end="")
    print()
    row += 1
