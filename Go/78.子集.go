/*
 * @lc app=leetcode.cn id=78 lang=golang
 *
 * [78] 子集
 */
package main

// @lc code=start
func subsets(nums []int) [][]int {
	// 有状态的递归=回溯
	// 每个元素有两种状态，可以包含它，也可以不包含它，
	// 所以对于[1,2,3],结果有 2*2*2=8
	// 递归的终止条件是路径=nums 的长度
	var res [][]int
	var tmp []int

	// 声明递归闭包函数 dfs
	// 闭包可以直接捕获外层的 res、tmp、和 nums，不需要作为参数频繁传递
	var dfs func(pathLen int)
	dfs = func(pathLen int) {
		// 递归终止条件
		if pathLen == len(nums) {
			// 将 tmp 进行深拷贝后加入结果集
			cp := make([]int, len(tmp))
			copy(cp, tmp)
			res = append(res, cp)
			return
		}

		// 可以包含 当前 nums 这个元素
		tmp = append(tmp, nums[pathLen])
		dfs(pathLen + 1)

		// 撤销选择（回溯）
		tmp = tmp[:len(tmp)-1]

		// 也可以不包含当前元素
		dfs(pathLen + 1)
	}

	// 从 index 0 开始递归
	dfs(0)

	return res
}

// @lc code=end
