# def sliding_window_flexible_longest(input):
#     initialixe window, ans 
#     left = 0
#     for right in range(len(input)):
#         append input[right] to window 
#         while invalid(window):
#             remove input[left] from window 
#             left += 1
#         ans = max(ans, window)
#     return ans
############################################################
# def flexible_window(arr):
#     left = 0
#     ans = 0

#     for right in range(len(arr)):
#         # add arr[right] to window

#         while invalid_condition:
#             # remove arr[left]
#             left += 1

#         ans = max(ans, right - left + 1)

#     return ans
def sliding_window_flexible_longest(arr, target):
    left = 0
    window_sum = 0
    ans = 0

    for right in range(len(arr)):
        window_sum += arr[right]

        while window_sum > target:   # invalid
            window_sum -= arr[left]
            left += 1

        ans = max(ans, right - left + 1)

    return ans
