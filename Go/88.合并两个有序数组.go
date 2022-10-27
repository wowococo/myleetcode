/*
 * @lc app=leetcode.cn id=88 lang=golang
 *
 * [88] 合并两个有序数组
 */
package main

// @lc code=start
func merge(nums1 []int, m int, nums2 []int, n int) {
	// 使用一个额外的数组
	nums1_copy := make([]int, m)
	copy(nums1_copy, nums1[:m])

	var i, j, k int
	for i < m && j < n {
		if nums1_copy[i] < nums2[j] {
			nums1[k] = nums1_copy[i]
			i++
		} else {
			nums1[k] = nums2[j]
			j++
		}

		k++
	}

	for i < m && k < m+n {
		nums1[k] = nums1_copy[i]
		i++
		k++
	}

	for j < n && k < m+n {
		nums1[k] = nums2[j]
		j++
		k++
	}
}

// @lc code=end
