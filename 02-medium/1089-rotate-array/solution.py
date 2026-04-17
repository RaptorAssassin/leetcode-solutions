class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        original = list(nums)
        for index, element in enumerate(original):
            new_index = (index + k) % len(nums)
            nums[new_index] = element
