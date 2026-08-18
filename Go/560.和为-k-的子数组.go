/*
 * @lc app=leetcode.cn id=560 lang=golang
 *
 * [560] 和为 K 的子数组
 */
package main

// @lc code=start
func subarraySum(nums []int, k int) int {
	// 任何子数组都的和可以表示为两个前缀和的差，包括前缀子数组本身，
	// 要想包括前缀子数组也成立，需要设置一个初始值，前缀和为 0 的数组个数为 1 个
	// 我们用 memo 存储前缀和及对应的前缀和的数量。
	res := 0
	mp := make(map[int]int, len(nums))
	preSum := 0
	mp[preSum] = 1
	for _, num := range nums {
		preSum += num
		if count, ok := mp[preSum-k]; ok {
			res += count
		}

		mp[preSum]++
	}

	return res
}

// @lc code=end

/*
为什么先看历史，再写历史，如果先写历史，历史就会被现在的动作污染了
主要是避免 k=0的情况，举个例子，数组为 nums[3], k=0 ，答案应该是 0，如果先更新 memo 的话，memo 先变为
{0:1, 3:1},那么 count 就会得到 memo[3]的值，，相当于 memo[3]刚写进去，就被查出来，查到的正是刚刚写进去的自己
这在逻辑上意味着，允许了一个前缀和减去他自己，从而拼出了一个“空数组“（长度为 0 的子数组），而题目要求子数组
必须是非空数列，所以计数就会偏大。
*/
