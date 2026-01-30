def two_sum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        summa = target - nums[i]
        if summa in hashmap:
            return[i, hashmap[summa]]
        hashmap[nums[i]] = i
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)