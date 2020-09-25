import random
import time

def generate_rand_list(max_size):
    new_list = []
    for i in range(0, max_size):
        new_list.append(random.randint(1,99))
    return new_list



"""
# O (log N)
powoli rosnie, im większe n tym mniej rośnie
10^2 = 100 log10(100) = 2 logarytm zwraca tylko potęgę

binary search O(log N)
- zaczyna od połowy listy
- MINUS - działa tylko dla posorowanych list [!]

"""

list_1 = []
def binary_search(value: int):
    list_size = len(list_1)
    low_index = 0
    high_index = list_size - 1
    while low_index <= high_index:
        mid_index = int((high_index + low_index)/2)
        if list_1[mid_index] < value:
            low_index = mid_index + 1
        elif list_1[mid_index] > value:
            high_index = mid_index - 1
        else:
            print(f"Found a match for {value} at index {mid_index}")
            low_index = high_index + 1


def partition(start, end):
    pivot = list_1[start]
    low = start + 1
    high = end
    while True:
        while low <= high and list_1[high] >= pivot:
            print("high = high - 1")
            high = high - 1
        while low <= high and list_1[low] <= pivot:
            print("low = low + 1")
            low = low + 1
        if low <= high:
            print("list_1[low], list_1[high] = list_1[high], list_1[low]")
            list_1[low], list_1[high] = list_1[high], list_1[low]
        else:
            print("else: break")
            break
    print("Poza petla")
    list_1[start], list_1[high] = list_1[high], list_1[start]
    print("RERURN; ", high)
    return high



def quick_sort(start, end): #nlogn
    # Demonstrates how the Quick sort works
    for k in list_1:
        print(k, end=", ")
    print()
    if start >= end:
        return
    part = partition(start, end)
    quick_sort(start, part-1)
    quick_sort(part+1, end)


if __name__ == "__main__":
    # print("O(log N) Testing binary search - it works only for sorted list")
    # list_1 = [5, 9, 2, 8, 1, 4, 3]
    # quick_sort(0, len(list_1) - 1)
    # print(list_1)
    # binary_search(8)
    #
    #
    # list_1 = generate_rand_list(1000)
    # quick_sort(0, len(list_1) - 1)
    # start_time = time.time()
    # binary_search(150)
    # print(f"{time.time() - start_time} seconds")
    #
    # list_1 = generate_rand_list(50000)
    # quick_sort(0, len(list_1) - 1)
    # start_time = time.time()
    # binary_search(150)
    # print(f"{time.time() - start_time} seconds")

    list_1 = [5, 4, 8, 2, 1, 0]
    quick_sort(0, len(list_1)-1)
    print("End: ", list_1)
    #Comparisons = log N + log(N-1) +... | log(1)
    #Evaluate to N LOG N