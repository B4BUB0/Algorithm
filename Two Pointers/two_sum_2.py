class Solution:
    def twoSum2(self, numbers, target):
        left, right = 0, len(numbers) -1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return [left +1, right +1]
            elif curSum < target:
                left += 1
            else:
                right -= 1
        return -1 
    
# Example usage
sol = Solution()
print(sol.twoSum2([2, 7, 11, 15], 9))