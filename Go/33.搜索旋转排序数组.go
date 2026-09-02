/*
 * @lc app=leetcode.cn id=33 lang=golang
 *
 * [33] 搜索旋转排序数组
 */
package main

// @lc code=start
func searchRotateSortArray(nums []int, target int) int {
	// 画一个坐标，拆分成两段单调递增的折线
	// L， R 初始值还是第一个和最后一个元素，看 mid 落在第一个递增的线段区间里，
	// 还是第二个递增的线段区间里
	// 如果是第一个，对应的特征是[L, mid] 这个区间是单调递增的
	// 如果是第二个，对应的特征是[mid, R] 这个区间是单调递增的

	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + (right-left)/2
		if nums[mid] == target {
			return mid
		}

		// 在第一个线段区间里
		if nums[left] <= nums[mid] {
			// 如果 target 在[left, mid]里，更新右边界
			if nums[left] <= target && target < nums[mid] {
				right = mid - 1
			} else {
				left = mid + 1
			}
		} else {
			// 在第二个线段区间里,如果在[mid, right],更新左边界
			if nums[mid] < target && target <= nums[right] {
				left = mid + 1
			} else {
				right = mid - 1
			}

		}
	}

	return -1
}

// @lc code=end
