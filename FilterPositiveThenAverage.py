# Filter Positive Then Average
# - Given a list of integers, filter only positive numbers and calculate their average.
# - If there are no positive numbers, return 0.
# - Time: O(n), Space: O(n)

def filterPositiveThenAverage(nums: list[int]) -> float:
    positives = [x for x in nums if x > 0]
    return sum(positives) / len(positives) if positives else 0
