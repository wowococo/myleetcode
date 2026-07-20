/*
 * @lc app=leetcode.cn id=560 lang=golang
 *
 * [560] 和为 K 的子数组
 */
package main

// @lc code=start
func subarraySum(nums []int, k int) int {
	// 任意子数组（包括前缀子数组）都可以表示为两个前缀和的差
	// 要满足这个结论，需要定义一个初始值，前 0 个数的和为 0，前缀和为 0 的数组数量有 1 个
	// 使用一个哈希表 memo 来存储前缀和以及它对应的数量， key 是前缀和，value是这个前缀和有多少个
	memo := make(map[int]int, len(nums))
	memo[0] = 1
	ans := 0
	presum := 0
	for _, num := range nums {
		presum += num
		// 1. 先检查（此时 map 里只有历史前缀和，不包含当前这个）
		// 在 Go 语言中，从 map 里获取一个不存在的 key 时，会直接返回该类型的零值（对于 int 来说就是 0）。
		ans += memo[presum-k]
		// 2. 后更新，直接累加，即使 key 不存在，GO 会默认从 0 开始加
		memo[presum]++

	}

	return ans
}

// @lc code=end

/*
为什么先看历史，再写历史，如果先写历史，历史就会被现在的动作污染了
主要是避免 k=0的情况，举个例子，数组为 nums[3], k=0 ，答案应该是 0，如果先更新 memo 的话，memo 先变为
{0:1, 3:1},那么 count 就会得到 memo[3]的值，，相当于 memo[3]刚写进去，就被查出来，查到的正是刚刚写进去的自己
这在逻辑上意味着，允许了一个前缀和减去他自己，从而拼出了一个“空数组“（长度为 0 的子数组），而题目要求子数组
必须是非空数列，所以计数就会偏大。
*/
