def factorial(num):
    if num==0:
        return 1
    else:
        return num * factorial(num-1)
print(factorial(5)) # Output: 120
print(factorial(0)) # Output: 1
print(factorial(1)) # Output: 1
print(factorial(400))