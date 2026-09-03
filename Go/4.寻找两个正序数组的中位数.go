/*
 * @lc app=leetcode.cn id=4 lang=golang
 *
 * [4] 寻找两个正序数组的中位数
 */
package main

import "math"

// @lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// 一条绳子串起两个数组的左半部分，i 可以看作 nums[1]的分割点，nums[:i-1]为 nums1
	// 的左半部分，nums[:j-1]为 nums2的左半部分
	// 1. 左半部分的元素个数要么等于右半部分，要么比右半部分大 1
	// 2. nums1[i-1] <= nums2[j]
	// 3. nums2[j-1] <= nums1[i]
	// 4. 左半部分的数量,也就是绳子的总长度：(m+n+1)/2 = i + j，也就是说确定了i，j 就确定了

	// 遍历较短的那个数组
	if len(nums1) > len(nums2) {
		nums1, nums2 = nums2, nums1
	}
	m, n := len(nums1), len(nums2)

	// 二分查找查找 i
	left, right := 0, m
	for left <= right {
		i := left + (right-left)/2
		j := (m+n+1)/2 - i
		var left1, left2, right1, right2 int
		// 边界条件，绳子全部在nums2
		if i == 0 {
			left1 = math.MinInt
		} else {
			left1 = nums1[i-1]
		}

		if i == m {
			right1 = math.MaxInt
		} else {
			right1 = nums1[i]
		}

		if j == 0 {
			left2 = math.MinInt
		} else {
			left2 = nums2[j-1]
		}

		if j == n {
			right2 = math.MaxInt
		} else {
			right2 = nums2[j]
		}
		// 满足条件，计算中位数
		if left1 <= right2 && left2 <= right1 {
			// 奇数个
			if (m+n)%2 == 1 {
				return float64(max(left1, left2))
			}
			return float64(max(left1, left2)+min(right1, right2)) / 2.0

		} else if left1 > right2 {
			// 说明绳子在 nums1 太靠右了，需要往左挪挪
			right = i - 1
		} else if left2 > right1 {
			// 说明绳子在 nums1 太靠左了，需要往右挪挪
			left = i + 1
		}
	}

	// 返回默认值 0
	return 0.0

}

// @lc code=end
