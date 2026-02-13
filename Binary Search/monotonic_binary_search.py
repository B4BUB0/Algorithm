def monotonic_binary_search(arr, target):
    l, r = 0, len(arr) - 1 
    firstT_index = - 1
    while l <= r:
        mid = (l + r) // 2
        if feasible(mid):
            firstT_index = mid
            r = mid - 1
        else: 
            l = mid + 1
    return firstT_index
