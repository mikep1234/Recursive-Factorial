def factorial(n):
    if n == 2:
        return n
    print(str(n) + " * " + str(n-1))
    return n * factorial(n-1)

print(factorial(5))