class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_hashset = set()

        for i in nums:
            if i in my_hashset:
                return True
            
            # if not found, add to the set
            
            my_hashset.add(i)
        return False