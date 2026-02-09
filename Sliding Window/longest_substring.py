from collections import defaultdict

class Solution:
    def longestSubstring(self, s):
        longest = 0
        l = 0
        counter: dict[str, int] = defaultdict(int)
        
        for r in range(len(s)):
            counter[s[r]] += 1
            while counter[s[r]] > 1:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
    
''''Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000'''