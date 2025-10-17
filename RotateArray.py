# Rotate Array
# - Rotate the array to the right by k steps.
# - Time: O(n), Space: O(n) for new array or O(1) for in-place
# - Example: [1,2,3,4,5], k=2 -> [4,5,1,2,3]

class Solution:
    def rotateArray(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        k %= n  # handle k > n
        return nums[-k:] + nums[:-k]  # simple new array solution

    # Optional: in-place rotation
    def rotateArrayInPlace(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
