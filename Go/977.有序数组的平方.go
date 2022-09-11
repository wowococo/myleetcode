/*
 * @lc app=leetcode.cn id=977 lang=golang
 *
 * [977] 有序数组的平方
 */
package main

// @lc code=start
func sortedSquares(nums []int) []int {
	index := len(nums) - 1
	i, j := 0, index
	result := make([]int, len(nums))
	for i <= j {
		left, right := square(nums[i]), square(nums[j])
		if left < right {
			result[index] = right
			j--
		} else {
			result[index] = left
			i++
		}
		index--
	}

	return result
}

func square(num int) int {
	return num * num
}

// @lc code=end
