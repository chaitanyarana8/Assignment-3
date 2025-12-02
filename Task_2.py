import math

user_input = float(input("Enter a Number: "))
#calculate  using math module
square_root = math.sqrt(user_input) if user_input>=0 else "undefined for negative numbers"
natural_log =math.log(user_input) if user_input>0 else "undefined for non-negative numbers"
sine_log = math.sin(user_input) if user_input>=0 else "undefined for negative numbers"

#print the results
print(f"Square root of {user_input} is: {square_root}")
print(f"Natural logarithm of {user_input} is: {natural_log}")
print(f"Sine of {user_input} is: {sine_log}")
