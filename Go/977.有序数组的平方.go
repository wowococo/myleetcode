/*
 * @lc app=leetcode.cn id=977 lang=golang
 *
 * [977] 有序数组的平方
 */
package main

// @lc code=start
func sortedSquares(nums []int) []int {
	n := len(nums)
	i, j, k := 0, n-1, n-1
	result := make([]int, len(nums))
	for i <= j {
		left, right := nums[i]*nums[i], nums[j]*nums[j]
		if left < right {
			result[k] = right
			j--
		} else {
			result[k] = left
			i++
		}
		k--
	}

	return result
}

// @lc code=end
