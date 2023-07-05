def print_star_pyramid(rows):
    # Initialize variables
    i = 0
    while i < rows:
        # Print spaces
        j = 0
        while j < rows - i - 1:
            print(" ", end="")
            j += 1

        # Print stars
        j = 0
        while j <= i:
            print("* ", end="")
            j += 1

        # Move to the next line
        print()
        i += 1


# Test the function
rows = int(input("Enter the number of rows: "))
print_star_pyramid(rows)
