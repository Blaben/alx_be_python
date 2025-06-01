

# First, use a while loop to iterate through each row of the pattern.
# Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
# After completing each row, print a newline character to move to the next row.
# Continue until the pattern forms a square of the inputted size.


length = abs(int(input("Enter the size of the pattern: ")))
row = 0

while row < length:
    for i in range(length):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1

