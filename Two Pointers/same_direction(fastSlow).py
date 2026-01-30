slow = 0

for fast in range(len(arr)):
    if condition:
        arr[slow] = arr[fast]
        slow += 1
        
"""
🧠 Mental model
👉 One pointer explores, the other builds result
🧪 Used for:
• Removing duplicates
• Filtering arrays
• In-place operations
"""