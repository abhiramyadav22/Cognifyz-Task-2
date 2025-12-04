print("Where Data Meets Intelligence")
print("Task 2: Generate and Print Number Pattern\n")

# Take input from user
rows = int(input("Enter number of rows: "))

print("\nGenerated Number Pattern:\n")

# Outer loop controls the rows
for i in range(1, rows + 1):

    # Inner loop prints numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")

    # Move to next line after each row
    print()

print("\nPattern printed successfully.")
