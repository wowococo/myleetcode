/*
 * @lc app=leetcode.cn id=704 lang=golang
 *
 * [704] 二分查找
 */
package main

// @lc code=start
func search(nums []int, target int) int {
	// 将 [left, right] 作为循环不变量
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			return mid
		}
	}

	return -1
}

// @lc code=end
