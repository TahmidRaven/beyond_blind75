# Problem 217 LEETCODE

- [Contains Duplicate – LeetCode](https://leetcode.com/problems/contains-duplicate/)


# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
- Thought of looping it but gives TC: $$O(n^2)$$  SC: $$O(1)$$ 

- Again, using sort it'd give TC: $$O(nlogn)$$  SC: $$O(1)$$ 

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
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_hashset = set()

        for i in nums:
            if i in my_hashset:
                return True
            #if not
            #add to hashset
            my_hashset.add(i)
        return False
```