def partition(start, end):
    pivot = my_list[start]
    low = start + 1
    high = end
    while True:
        while low <= high and my_list[high] >= pivot:
            high = high - 1
        while low <= high and my_list[low] <= pivot:
            low = low + 1
        if low <= high:
            my_list[low], my_list[high] = my_list[high], my_list[low]
        else:
            break
    my_list[start], my_list[high] = my_list[high], my_list[start]
    return high


def quick_sort(start, end):
    if start >= end:
        return
    part = partition(start, end)
    quick_sort(start, part-1)
    quick_sort(part+1, end)


if __name__ == "__main__":
    my_list = [5, 4, 8, 2, 1, 0]
    quick_sort(0, len(my_list)-1)
    print(my_list) # [0, 1, 2, 4, 5, 8]
    sorted(my_list)



