package main

/*
 * @lc app=leetcode.cn id=713 lang=golang
 *
 * [713] 乘积小于 K 的子数组
 */

// @lc code=start
func numSubarrayProductLessThanK(nums []int, k int) int {
	ans := 0
	for i, j, cur := 0, 0, 1; j < len(nums); j++ {
		cur *= nums[j]
		for cur >= k && i <= j {
			cur /= nums[i]
			i++
		}
		ans += j - i + 1
	}

	return ans
}

// @lc code=end
