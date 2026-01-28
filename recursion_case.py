def countdown(i):
    print (i)
    if i <= 1: # Базовый случай
        return
    else:
        countdown(i-1) # Recursion case