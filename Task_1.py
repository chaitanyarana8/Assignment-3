def factorial(n):
    if n <0:
        return "Factorial not defined for negative numbers"
    result =1
    for i in range(1,n+1):
        result *=i
    return result
    
# function call 
num = int(input())
print(f"Enter a number: {num}")
print(f"Factorial of {num} is:" , factorial(num))