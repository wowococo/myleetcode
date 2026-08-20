/*
 * @lc app=leetcode.cn id=41 lang=golang
 *
 * [41] 缺失的第一个正数
 */
package main

// @lc code=start
func firstMissingPositive(nums []int) int {
	// 长度为n 的数组，正常填入正整数为[1, n],
	// 将数组中的正整数元素填入其该填的位置
	// 缺失的最小正整数的区间为[1, n+1]
	n := len(nums)
	for i := 0; i < n; i++ {
		for nums[i] >= 1 && nums[i] <= n && nums[i] != nums[nums[i]-1] {
			nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
		}
	}

	for i := 0; i < n; i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}

	return n + 1
}

// @lc code=end
