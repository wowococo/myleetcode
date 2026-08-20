/*
 * @lc app=leetcode.cn id=238 lang=golang
 *
 * [238] 除了自身以外数组的乘积
 */
package main

// @lc code=start
func productExceptSelf(nums []int) []int {
	// 前缀积、后缀积
	// answer[i] = prefix[i] * postfix[i]
	// prefix[i] = nums[0] * ... * nums[i-1]
	// postfix[i] = nums[i+1]*...* nums[n-1]
	ans := make([]int, len(nums))
	prefix := 1
	for i := 0; i < len(nums); i++ {
		ans[i] = prefix
		prefix = prefix * nums[i]
	}

	postfix := 1
	for j := len(nums) - 1; j >= 0; j-- {
		ans[j] = ans[j] * postfix
		postfix = postfix * nums[j]
	}

	return ans
}

// @lc code=end
