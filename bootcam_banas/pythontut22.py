import random

_sum = lambda x,y : x+y
print(_sum(4, 5))

can_vote = lambda age: True if age >= 18 else False
print("Can vote: ", can_vote(16))

power_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for func in power_list:
    print(func(4))

attack = {'quick': (lambda: print("Quick Attack")),
            'power': (lambda: print("Quick Power")),
            'missed': (lambda: print("Quick Missed"))
          }
attack['quick']()

attack_key = random.choice(list(attack.keys()))
attack[attack_key]()


flip_list = [random.choice(["H", "T"]) for i in range(100)]
print("Heads: ", flip_list.count("H"))
print("Tails: ", flip_list.count("T"))


one_to_10 = range(1, 11)
def dbl_num(num):
    return num * 2

print(list(map(dbl_num, one_to_10)))
print(list(map( lambda x: x*2, one_to_10) ))

a_list = list(map(lambda x, y: x+y, [1,2,3], [1,2,3]))
print(a_list)


# filter
print("tuuuuuuuu")
print(list(filter(lambda x: x% 2 == 0, range(1,11))))

rand_list = list(random.randint(1,1001) for i in range(100))
print(rand_list)
print(list(filter(lambda x: x % 9 ==0, rand_list)))

# reduce
from functools import reduce
print(reduce( lambda x, y: x+y, range(1,6)))