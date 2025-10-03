# Search Insert Position
# - Given a **sorted array of distinct integers** `nums` and a `target` value.  
# - Return the **index** if `target` is found.  
# - If not found, return the index where `target` would be **inserted to keep the array sorted**.  
# - Must use an algorithm with **O(log n)** runtime complexity.

def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return left
