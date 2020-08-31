# function 3! = 3 * 2 * 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(33))
print(factorial(0))

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(f"fib(3): {fib(3)}")
print(fib(4))
print(fib(4))

how_many = int(input("How many Fibbonachi values should be found"))
fibo_list = []
i = 0
while len(fibo_list) <= how_many:
    fibo_list.append(fib(i))
    i += 1

print(fibo_list)