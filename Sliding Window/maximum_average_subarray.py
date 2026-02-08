class Solution:
    def findMaxAverage(self, nums, k):
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        largest = window_sum

        for right in range(k, len(nums)):
            left = right - k 
            window_sum -= nums[left]
            window_sum += nums[right]
            largest = max(largest, window_sum)

        return largest / k
    
    # class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         window_sum = sum(nums[:k])
#         largest = window_sum


#         for right in range(k, len(nums)):
#             left = right - k
#             window_sum += nums[right] - nums[left]
#             largest = max(largest, window_sum)

#         return largest / k



''''Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000'''
