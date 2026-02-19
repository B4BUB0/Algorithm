class Solution(object):
    def characterReplacement(self, s, k):
        max_count = 0
        left = 0
        freq = {}
        
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            max_count = max(max_count, freq[s[right]])
            
            if right - left + 1 - max_count > k:
                freq[s[left]] -= 1
                left += 1
                
        return len(s) - left
    
"""Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too."""