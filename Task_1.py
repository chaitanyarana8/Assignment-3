def my_factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
    
while True:
    try:
        user_input = int(input("Enter a non-negative integer to calculate its factorial:"))
        if user_input<0:
            print("Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

print(f"factorial of {user_input} is: {my_factorial(user_input)}")
