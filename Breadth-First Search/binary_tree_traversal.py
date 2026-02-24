from collections import deque 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def level_order_traversal(root):
        if not root:
            return []
        
        res = []
        queue = deque([root])
        while len(queue) > 0:
            n = len(queue) # how many nodes in this level
            new_level = []
            for _ in range(n): # n is the number of nodes on current level
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            res.append(new_level)
        return res          

### Given the root of a binary tree, return the level order traversal of its nodes' values. 
# (i.e., from left to right, level by level). ####

""" Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: [] """