// Running Sum
// - Given an array nums, return the running sum of the array.
// - Running sum: runningSum[i] = sum(nums[0]...nums[i])
// - Can be solved iteratively with a single pass.
//- Time: O(n), Space: O(n)

using System;
using System.Collections.Generic;

public class Solution {
    public int[] RunningSum(int[] nums) {
        int[] res = new int[nums.Length];
        int currentSum = 0;
        for (int i = 0; i < nums.Length; i++) {
            currentSum += nums[i];
            res[i] = currentSum;
        }
        return res;
    }
}
