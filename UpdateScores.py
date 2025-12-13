# - Updates student scores using update().
# - Demonstrates overwriting existing values safely.
# - Time: O(n), Space: O(1)

class Solution:
    def updateScores(self, scores: dict, new_scores: dict) -> dict:
        scores.update(new_scores)
        return scores
