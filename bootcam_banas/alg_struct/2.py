import random
import time

"""
Notacja Big-O zawsze określa najgorszy scenariusz
"""

list_1 = []
start_time = 0
end_time = 0


def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1,99))
    return new_list


list_1 = generate_rand_list(10)


def add_item_to_list(num):
    """
    O(1)
    - Algorithm Executes is Same Amount of TimeRegardless of List Size
    - 10 Item List and 10,000 Item Lists Take the Same Time
    """
    list_1.append(num)




def linear_search(val):
    """
    O(N)
    - Algorithm Executes Directly Proportional to Amount of Data
    - Linear Search: Requires Looking at Each Item in a List
    """
    val_found = "Value not found"
    for i in list_1:
        if i == val:
            val_found = "Value found"
    print(val_found)

print("Testing Linear Search")
list_1 = generate_rand_list(10)
start_time = time.time()
#sprawdzam najgorszy scenarusz
linear_search(10000) # sprawdzam dla wartości dla której nie ma w liście
print(f"{time.time() - start_time} seconds")


list_1 = generate_rand_list(1000)
start_time = time.time()
#sprawdzam najgorszy scenarusz
linear_search(10000) # sprawdzam dla wartości dla której nie ma w liście
print(f"{time.time() - start_time} seconds")

list_1 = generate_rand_list(100000)
start_time = time.time()
#sprawdzam najgorszy scenarusz
linear_search(10000) # sprawdzam dla wartości dla której nie ma w liście
print(f"{time.time() - start_time} seconds")


def bubble_sort():
    """
    #grows exponentially

    THE BUBBLE SORT - O(N^2)
    - An outer loop decreases is size each time
    - Goal: Largest number at the end of the ist after cycle
    - Inner loop compares indexes at the beginning of the loop
    - Check if list[index] > list[index + 1]
    - If so swap the index values
    - When the inner loop completes the larges number is at the end of the list
    - Decrement the outer loop by 1
    # have nested iteration n^2 - dwie zagnieżdzone iteracje
    # have nested iteration n^3 - trzy zagnieżdzone iteracje
    """
    list_size = len(list_1)
    for i in range(list_size):
        for j in range(0, list_size -i - 1):
            if list_1[j] > list_1[j+1]:
                list_1[j], list_1[j+1] = list_1[j+1], list_1[j]

            # for k in list_1:
            #     print(k, end=", ")
            # print()


list_1 = generate_rand_list(100) #grows exponentially
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time} seconds")

list_1 = generate_rand_list(1000)
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time} seconds") #grows exponentially

list_1 = generate_rand_list(10000)
start_time = time.time()
bubble_sort()
print(f"{time.time() - start_time} seconds") #grows exponentially

