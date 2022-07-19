"""
Code for assignment 2
"""
num = int(input("Enter number of rows to generate: "))
print("*")
row = 0
while row < num:
    row +=1
    if row == 1:
        continue
    else:
        print(" *"*row, end="")

    print()