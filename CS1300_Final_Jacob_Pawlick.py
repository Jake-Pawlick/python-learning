# Problem 1 — FizzBuzz

'''
# Print numbers 1 to 30 with FizzBuzz rules

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

# Problem 2 — Times Table Pattern

'''
# Print a 6x6 multiplication table

n = 6

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:4d}", end=" ")
    print()
'''

# Problem 3 — Remove Duplicates Preserving Order

'''
def unique_preserve_order(lst):
    result = []
    
    for item in lst:
        if item not in result:
            result.append(item)
    
    return result

# Example test
print(unique_preserve_order([1, 2, 2, 3, 1, 4]))
'''

# Problem 4 — Fibonacci Sequence Generator

'''
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]

    for i in range(2, n):
        next_value = fib[i - 1] + fib[i - 2]
        fib.append(next_value)

    return fib

# Test cases
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(7))
print(fibonacci(10))
print(fibonacci(0))
'''