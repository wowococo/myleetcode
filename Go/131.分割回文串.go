/*
 * @lc app=leetcode.cn id=131 lang=golang
 *
 * [131] 分割回文串
 */
package main

// @lc code=start
func partition(s string) [][]string {
	// 回溯+动态规划，最重要的还是要画出决策树，这个决策树的核心是以哪里为分割点
	var res [][]string
	var tmp []string

	dp := make([][]bool, len(s))
	for i := range dp {
		dp[i] = make([]bool, len(s))
	}

	dfs4Partition(s, 0, &res, tmp, dp)

	return res
}

// index 表示要分割的字符串对应的起始索引, res是结果数组，
// tmp 是临时的分割方案
func dfs4Partition(s string, index int, res *[][]string, tmp []string, dp [][]bool) {
	// 递归终止条件：要分割的字符串对应的其实索引 >= 字符串的长度，表示已经分割完成
	if index >= len(s) {
		cp := make([]string, len(tmp))
		copy(cp, tmp)
		*res = append(*res, cp)
		return
	}

	// 对当前字符串进行分割
	for i := index; i < len(s); i++ {
		// 如果是回文字符串，加入 tmp
		// 这里相当于每次循环都要再循环一遍子串判断是否是回文，我们可以用一个二维数组
		// dp[left][right]来存储是回文字符串的子串，以空间换时间
		if isHW(s, index, i, dp) {
			tmp = append(tmp, s[index:i+1])
			// 下一个分割点
			dfs4Partition(s, i+1, res, tmp, dp)
			// 不管有没有找到满足条件的方案，都要把当前的状态撤销到上一个状态，回溯
			tmp = tmp[:len(tmp)-1]

		}
	}
}

// 判断是否是回文字符串， legt,right 双指针在字符串的左右两侧，同时向中间移动
func isHW(s string, left, right int, dp [][]bool) bool {
	if dp[left][right] {
		return true
	}
	// 先保存一份，因为下面 left 和 right 一直在变
	l, r := left, right

	for left < right {
		if s[left] == s[right] {
			left++
			right--
		} else {
			return false
		}
	}

	dp[l][r] = true
	// 当相遇的时候还没返回 false，说明就是回文
	return true
}

// @lc code=end
