/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 */
package main

// @lc code=start
func generateParenthesis(n int) []string {
	// 假如 n=2, 那么就长度为 4（每个位置有 2 种可能），暴力穷举出 2 的 4 次方，有 16 个可能，
	// 然后再根据 20.有效的括号去判断

	// 回溯加剪枝，配合决策树很清晰
	// left: 递归过程中左侧括号的个数
	// right: 递归过程中右侧括号的个数
	// 根据下面的约束条件进行剪枝，其实也是在判断合法性
	// left < n: 可以选择左括号
	// right < left: 可以选择右括号

	var res []string
	var tmp []byte
	helper(n, 0, 0, &res, tmp)

	return res
}

// 辅助函数进行决策
func helper(n int, left, right int, res *[]string, tmp []byte) {
	// 递归的终止条件，左括号和右括号数都等于 n
	if left == n && right == n {
		// string(tmp) 这一步操作，本身就已经在底层触发了深拷贝
		*res = append(*res, string(tmp))
		return
	}

	if left < n {
		// 选择
		tmp = append(tmp, '(')
		helper(n, left+1, right, res, tmp)
		// 回溯
		tmp = tmp[:len(tmp)-1]
	}

	if right < left {
		tmp = append(tmp, ')')
		helper(n, left, right+1, res, tmp)
		// 回溯
		tmp = tmp[:len(tmp)-1]
	}

}

// @lc code=end
