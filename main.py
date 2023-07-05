num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")
string_ = """In Python, using curly braces {} within a string is a way to perform string formatting or interpolation. It allows you to embed values or expressions inside a string.

The notation {num} within a string is a placeholder that represents a variable or value that will be replaced during string formatting. The num in {num} refers to a variable name or expression that you want to substitute into the string."""

for i in range(1, 19):
    print(i)
    product = num * i
    print(f"{num} x {i} = {product}")
