/*
 * @lc app=leetcode.cn id=39 lang=golang
 *
 * [39] 组合总和
 */
package main

// @lc code=start
func combinationSum(candidates []int, target int) [][]int {
	// 也是一道回溯题，画出决策树就很清晰的，以 target为节点，路径写上选择的可能值val，
	// 下个节点就是 target-val,这里面每个节点下面的路径都可以选择candidates的任意一个元素
	// “如果至少一个数字的被选数量不同，则两种组合是不同的。 ”也就是说要进行剪枝，
	// 剪枝的逻辑是选择某个candidate时，它后面选的只能是当前candidate及以后的元素，不能选这个candidates之前的（结合决策树很好理解）

	// 老套路，定义结果变量和过程中的临时数组
	var res [][]int
	var tmp []int

	var helper func(start int, remainTarget int)
	helper = func(start int, remainTarget int) {
		// 递归结束条件：target <= 0
		// remainTarget == 0 时，将 tmp 加入结果数组
		if remainTarget == 0 {
			cp := make([]int, len(tmp))
			copy(cp, tmp)
			res = append(res, cp)
			return
		}

		// remainTarget < 0 时，不满足条件，直接 return
		if remainTarget < 0 {
			return
		}

		// remainTarget > 0 时，继续决策
		for i := start; i < len(candidates); i++ {
			// 这也是剪枝判断，为负的不满足条件，直接不要了
			if remainTarget-candidates[i] >= 0 {
				// 选择
				tmp = append(tmp, candidates[i])
				// 下一次从 i 开始，可以做到剪枝, 并且更新 target 值传递到下一层
				helper(i, remainTarget-candidates[i])
				// 回溯
				tmp = tmp[:len(tmp)-1]
			}
		}
	}

	helper(0, target)

	return res
}

// @lc code=end
