import random

print(list(map(lambda x: x*2, range(1,11))))

print([2 * x for x in range(1,11)])

print(list(filter(lambda x: x %2 != 0, range(1,11))))

print([x for x in range(1,11) if x%2!=0])

print([i ** 2 for i in range(50) if i % 8 ==0])

print([x*y for x in range(1,3) for y in range(11,16)])

print([x for x in [i*2 for i in range(10)] if x % 8 == 0])


#####################
rand_list= [x for x in [random.randint(1,1001) for i in range(15)] if x % 9 == 0]
print(rand_list)

#################
mult_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print([col[1] for col in mult_list])
print([mult_list[i][i] for i in range(len(mult_list))])


#######################################
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def gen_primes(max_number):
    for num1 in range(2, max_number):
        if is_prime(num1):
            yield num1


prime = gen_primes(16)
print("Prime", next(prime))
print("Prime", next(prime))
print("Prime", next(prime))
print("Prime", next(prime))
print("Prime", next(prime))


double = (x * 2 for x in range(10))
print("Double: ", next(double))
print("Double: ", next(double))

for num in double:
    print(num)