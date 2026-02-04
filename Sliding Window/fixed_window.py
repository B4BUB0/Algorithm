# def sliding_window_fixed(input, window_size):
#     ans = window = input[0:window_size]
#     for right in range(window_size, len(input)):
#         left = right - window_size
#         remove input[left] from window
#         append input[right] to window
#         ans = optimal(ans, window)
#     return ans

def sliding_window_fixed(arr, window_size):
    # first window sum
    window_sum = sum(arr[:window_size])
    ans = window_sum

    for right in range(window_size, len(arr)):
        left = right - window_size
        window_sum -= arr[left]     # remove left
        window_sum += arr[right]    # add right
        ans = max(ans, window_sum)  # optimal
    return ans
