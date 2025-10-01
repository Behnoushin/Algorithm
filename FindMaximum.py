# Find Maximum
# - Given a list of integers, find the maximum value.
# - You can use the built-in `max()` function or implement it manually with a loop.

nums = [3, 7, 2, 10, 4]
maximum = nums[0]

for num in nums[1:]:
    if num > maximum:
        maximum = num

