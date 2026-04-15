class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for index, element in enumerate(nums):
            complement = target - element
            if complement in prev_map:
                return [prev_map[complement], index]
            prev_map[element] = index
