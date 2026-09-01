/*
 * @lc app=leetcode.cn id=17 lang=golang
 *
 * [17] 电话号码的字母组合
 */
package main

// @lc code=start
func letterCombinations(digits string) []string {
	// 回溯，哈希表存储数字和字符串的映射, tmp 存临时字符串 bytes 数组
	// 这几道题递归都是用到的是dfs 深度优先遍历
	var res []string
	if len(digits) == 0 {
		return res
	}

	// 用 []byte 切片方便 append 和 pop
	var tmp []byte
	mp := map[byte]string{
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
	}

	// index 表示 digits 的索引
	var dfs func(index int)
	dfs = func(index int) {
		// 递归终止条件是index 到达 digits 的长度，表示已经处理完输入的最后一个数字
		if index == len(digits) {
			res = append(res, string(tmp))
			return
		}

		// 遍历当前的数字对应的字母
		letters := mp[digits[index]]
		for i := 0; i < len(letters); i++ {
			// 做选择：加入字符串，或者说是路径
			tmp = append(tmp, letters[i])
			// 递归处理下一个数字对应的字母
			dfs(index + 1)
			// 撤销选择，回溯，将当前数字从 tmp弹出来
			tmp = tmp[:len(tmp)-1]
		}
	}

	// 从第一个数字（index 0）开始递归
	dfs(0)

	return res
}

// @lc code=end
