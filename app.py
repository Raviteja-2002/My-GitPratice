def greet(name):
    """Function to print a greeting message."""
    return f"Hello, {name}!"

# Loop through a list of names
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(greet(name))

# Conditional statement example
number = 10
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
