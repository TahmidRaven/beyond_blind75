# Problem 001 LEETCODE

- [Two Sum – LeetCode](https://leetcode.com/problems/two-sum/)


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- could brute force into it by pairing each numbers; but gives TC: $$O(n^2)$$   

- Again, using hashmap by mapping them into it then iterating might do the job 

# Approach
<!-- Describe your approach to solving the problem. -->
- Followed neetcode on YT
# Complexity
- Time complexity: $$O(n)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
 
- Space complexity: $$O(n)$$
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_hash_map = {} # value : index mapping
        # Using a hash map to store the indices of the numbers
        # This allows us to find the complement in O(1) time

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in prev_hash_map:
                return [prev_hash_map[diff], i]
            prev_hash_map[num] = i
        return

```