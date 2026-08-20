/*
 * @lc app=leetcode.cn id=53 lang=golang
 *
 * [53] 最大子数组和
 */

package main

// 1 和 2 两种解法的区别是 curSum 初始化为 0 还是第一个元素，
// 会导致下面 for 遍历起点的不同和 if curSum < 0 条件的写法不一样
func maxSubArray1(nums []int) int {
	// 可能有负数，所以 maxSum 初始化不能为 0，初始成数组里的第一个元素
	maxSum := nums[0]
	curSum := 0
	for i := 0; i < len(nums); i++ {
		if curSum < 0 {
			// 说明前面的和对面没有帮助，舍弃前面的子数组
			curSum = 0
		}
		curSum += nums[i]
		maxSum = max(maxSum, curSum)
	}

	return maxSum
}

// @lc code=start
func maxSubArray2(nums []int) int {
	// 边界处理：防御 nil 或者空切片
	if len(nums) == 0 {
		return 0
	}

	// 初始化 currentSum 和 maxSum 为第一个元素
	currentSum := nums[0]
	maxSum := nums[0]

	// 从第二个元素开始遍历
	for i := 1; i < len(nums); i++ {
		// 如果当前累加和小于 0，说明前面的积累只会拖累当前值，果然重新开始
		if currentSum < 0 {
			currentSum = nums[i]
		} else {
			currentSum += nums[i]
		}

		// 实时更新全局最大值
		if currentSum > maxSum {
			maxSum = currentSum
		}
	}

	return maxSum
}

// @lc code=end
