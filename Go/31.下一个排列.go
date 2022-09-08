package main

/*
 * @lc app=leetcode.cn id=31 lang=golang
 *
 * [31] 下一个排列
 */

// @lc code=start

func nextPermutation(nums []int) {
	// 1. 需要下一个数增长的幅度尽可能的小，因此从最右边开始查找
	// 2. 将右边一个尽可能小的大数与左边的小数交换
	// 3. 大数到前面后，需要将大数后面的所有数升序排列。
	n := len(nums)
	if n <= 1 {
		return
	}
	i, j, k := n-2, n-1, n-1
	// find A[i] < A[j]
	for i >= 0 && nums[i] >= nums[j] {
		i--
		j--
	}

	// find A[k] > A[I]
	if i >= 0 {
		for nums[k] <= nums[i] {
			k--
		}

		nums[i], nums[k] = nums[k], nums[i]
	}

	// reverse A[i+1:], A[i+1:] 降序变升序
	for i, j := i+1, n-1; i < j; i, j = i+1, j-1 {
		nums[i], nums[j] = nums[j], nums[i]
	}

}

// @lc code=end
