def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
my_list = [2,41,2,43,1,42,3,42,1,42,3,6,5,3,4,6,7,8,5,68]
print (binary_search(my_list, 3))
print (binary_search(my_list, -1))