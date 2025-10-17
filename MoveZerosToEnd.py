# Move Zeros To End
# - Move all zeros in the array to the end while keeping order of non-zero elements.
# - Time: O(n), Space: O(1)
# - Example: [0,1,0,3,12] -> [1,3,12,0,0]

class Solution:
    def moveZerosToEnd(self, nums: list[int]) -> list[int]:
        j = 0  # index for placing non-zero
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
