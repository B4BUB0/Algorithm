def frequency_map(data):
    my_hash = {}
    for i in data:
        if i not in my_hash:
            my_hash[i] = 1
        else:
            my_hash[i] += 1
    return my_hash   # ← missing return

data = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(frequency_map(data))
