/*
查找两个字符串的最长公共子串
*/
package main

import "fmt"

/*
核心思路：DP 动态规划
首先定义一个二维数组：dp[i][j] 表示以 a[i-1]、b[j-1] 为结尾时，能匹配的最长连续公共子串的长度

状态转移方程：
1. 如果 a[i-1] = b[j-1], 说明在前面连续的基础上，又续了一个，dp[i][j] = dp[i-1][j-1] + 1
2. 如果a[i-1] != b[j-1]，说明连续断了，此时重置 dp[j][j] = 0
*/
// 时间复杂度 O(m*n), 空间复杂度 O(m*n)
func LongestCommonSubString(a, b string) string {
	// 边界情况：任一字符串为空，直接返回空串
	if len(a) == 0 || len(b) == 0 {
		return ""
	}

	// 用 rune 避免多字节字符（如中文）被截断
	ra, rb := []rune(a), []rune(b)
	m, n := len(ra), len(rb)

	// 定义二维切片 dp[i][j] 表示：A 前 i 个字符和 B 前 j 个字符的最长公共子序列的长度。
	// dp[i][j] = 表示：以 A 的第 i 个字符结尾、以 B 的第 j 个字符结尾时，能匹配的最长连续公共子串长度
	// dp[i][j] 表示：以 ra[i-1] 结尾、以 rb[j-1] 结尾的最长公共子串长度
	// 上面三种表述是一样的
	// 多开一行一列（第 0 行、第 0 列），代表和空字符串比较，值全部是 0
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	maxLen := 0    // 记录目前为止的最长长度
	endIndexA := 0 // 记录最长公共子串在 a 中的结束位置，方便最后截取结果

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if ra[i-1] == rb[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1

				if dp[i][j] > maxLen {
					maxLen = dp[i][j]
					endIndexA = i
				}

			} else {
				dp[i][j] = 0
			}
		}
	}

	if maxLen == 0 {
		return ""
	}

	return string(ra[endIndexA-maxLen : endIndexA])
}

func main() {
	fmt.Println(LongestCommonSubString("abcde", "abfde"))     // ab 或者 de
	fmt.Println(LongestCommonSubString("abcdxyz", "xyzabcd")) // abcd
	fmt.Println(LongestCommonSubString("", "abc"))            // ""
	fmt.Println(LongestCommonSubString("abc", "abc"))         // abc
	fmt.Println(LongestCommonSubString("abc", "def"))         // ""
	fmt.Println(LongestCommonSubString("我是", "我是哪吒"))         // "我是"

}
