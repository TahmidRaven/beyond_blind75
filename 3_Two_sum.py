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

