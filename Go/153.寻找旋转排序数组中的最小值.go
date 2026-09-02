/*
 * @lc app=leetcode.cn id=153 lang=golang
 *
 * [153] 寻找旋转排序数组中的最小值
 */
package main

// @lc code=start
func findMin(nums []int) int {
	// 类似 33.搜索旋转排序数组的思路，两个单调递增的区间线段
	// 这里最小值是一定在第二个单调区间里的，第一段的最小值都会比第二段的最大值大（元素值 互不相同）

	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		// 按照这个思路一直收敛，可以收敛为一个单调递增的数组，这时候 nums 第一个元素就是最小值
		if nums[left] <= nums[mid] && nums[mid] <= nums[right] {
			return nums[left]
		} else if nums[mid] >= nums[left] {
			// 如果 mid 在第一段区间里,那么最小值在 [mid+1, right] 区间里
			left = mid + 1
		} else if nums[mid] <= nums[right] {
			// 如果 mid 在第二段区间里,那么最小值在[l, mid] 区间里
			right = mid
		}
	}

	return -1
}

// @lc code=end
