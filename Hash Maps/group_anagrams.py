from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            hashmap[key].append(word)
        return list(hashmap.values())
    
# Create an object of Solution
sol = Solution()

strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))