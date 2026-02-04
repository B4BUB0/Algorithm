def sliding_window_flexible_longest(input):
    initialixe window, ans 
    left = 0
    for right in range(len(input)):
        append input[right] to window 
        while invalid(window):
            remove input[left] from window 
            left += 1
        ans = max(ans, window)
    return ans