def mult_by_2(num):
    return num * 2

times_two = mult_by_2
print("4 * 2= ", times_two(4))


def do_math(func, num):
    return func(num) #funkcja przekazana jako argument jest tu wywolywana

print("8*2 = ", do_math(mult_by_2, 8))

def get_func_mult_by_number(num):
    # zwraca funckje
    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_number(5)
print("5 * 9 =", generated_func(9))

list_of_funcs = [times_two, generated_func]
print("5 * 9 = ", list_of_funcs[1](9))



############################
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def change_list(list, func): # func jako obiekt ; funkcja sprawdzajaca
    odd_list = []
    for i in list:
        if func(i):
            odd_list.append(i)
    return odd_list

a_list = range(1,29)
print(change_list(a_list, is_it_odd))

############################
def random_func(name:str, age:int, weight:float)->str:
    print("Name: ", name)
    print("age: ", age)
    print("weight: ", weight)
    return "{} is {} years old and weight {}".format(name, age, weight)

print(random_func("Derek", 41, 165.5))
print(random_func.__annotations__)

