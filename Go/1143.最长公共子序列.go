/*
 * @lc app=leetcode.cn id=1143 lang=golang
 *
 * [1143] 最长公共子序列
 */
package main

/*
一、 动态规划与二维数组设计
1. 状态定义定义二维切片 dp[i][j] 表示：str1 前 i 个字符和 str2 前 j 个字符的最长公共子序列的长度。
2. 状态转移方程对于位置 (i, j)（对应字符 r1[i-1] 与 r2[j-1]）：
若字符相等 (r1[i-1] == r2[j-1])：说明找到了公共字符，继承对角线的长度并加 1：dp[i][j] = dp[i-1][j-1] + 1

若字符不相等 (r1[i-1] != r2[j-1])：因为子序列允许不连续，
所以尝试抛弃 r1 的当前字符或 r2 的当前字符，取两者的最大值：dp[i][j] = max(dp[i-1][j], dp[i][j-1])
*/

// @lc code=start
// 动态规划题
// 先定义 dp[i][j] 表示 text1 前 i 个字符、text2 前 j 个字符的最长公共子序列的长度
// 状态转移方程：
// 1. 的 ，如果 text1[i-1] = text2[j-1]; dp[i][j] = dp[i-1][j-1] + 1
// 2. 如果 text1[i-1] != text2[j-1], 就抛弃 i 位置 的或者 j 位置的
// dp[i][j] = max(dp[i-1]j, dp[i][j-1])

// 时间复杂度：O（M * N）
// 空间复杂度：O（M * N） -- 用于存储 DP 表
func longestCommonSubsequence(text1 string, text2 string) int {
	// 边界防御
	if len(text1) == 0 || len(text2) == 0 {
		return 0
	}

	// 转换为 []rune ,支持多 byte 字符，比如中文
	rt1, rt2 := []rune(text1), []rune(text2)
	m, n := len(rt1), len(rt2)

	// 创建 (m + 1) * (n + 1) 的二维数组
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if rt1[i-1] == rt2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {

				if dp[i-1][j] > dp[i][j-1] {
					dp[i][j] = dp[i-1][j]
				} else {
					dp[i][j] = dp[i][j-1]
				}
			}
		}
	}

	return dp[m][n]
}

// @lc code=end
