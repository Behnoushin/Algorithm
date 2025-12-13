# - Extract digits from text, calculate rounded avg, max, min.
# - Time: O(n), Space: O(n)

class Solution:
    def analyzeNumbers(self, text: str):
        nums = [int(c) for c in text if c.isdigit()]
        if not nums:
            return (0.0, 0.0, 0.0)
        avg = round(sum(nums)/len(nums), 2)
        return avg, round(max(nums), 2), round(min(nums), 2)
