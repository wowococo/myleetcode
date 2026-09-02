/*
 * @lc app=leetcode.cn id=34 lang=golang
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */
package main

// @lc code=start
func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}

	leftIndex := searchBinary(nums, target, true)
	rightIndex := searchBinary(nums, target, false)
	return []int{leftIndex, rightIndex}
}

// 查找目标值的左右边界，isLeft 表示找的是左边界还是右边界
func searchBinary(nums []int, target int, isLeft bool) int {
	left := 0
	right := len(nums) - 1
	index := -1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] < target {
			left = mid + 1
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			// 先更新 index 的值
			index = mid
			// 如果是寻找左边界,就去 mid 的左边寻找（不包括 mid）
			if isLeft {
				right = mid - 1
			} else {
				// 如果是寻找有边界，就去 mid 的右边寻找（不包括 mid）
				// 可以自己模拟走一遍
				left = mid + 1
			}
		}
	}

	return index
}

// @lc code=end
