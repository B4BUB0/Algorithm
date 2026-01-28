def countdown(i):
    print (i)
    if i <= 1: # Normal case
        return
    else:
        countdown(i-1) # Recursion case