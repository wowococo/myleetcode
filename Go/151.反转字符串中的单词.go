/*
 * @lc app=leetcode.cn id=151 lang=golang
 *
 * [151] 反转字符串中的单词
 */
package main

import "strings"

// @lc code=start
func reverseWords2(s string) string {
	strs := strings.Fields(s)
	var newStrs []string
	for i := len(strs) - 1; i >= 0; i-- {
		newStrs = append(newStrs, strs[i])
	}
	return strings.Join(newStrs, " ")
}

// 1. 先去除多余空格，快慢指针, 参考 27(移除数组中多余元素)
// 2. 再反转整个字符串
// 3. 再把单词反转过来
// @lc code=start
func reverseWords(s string) string {
	byteStr := []byte(s)
	removeSpace(byteStr)
	reverseStr1(byteStr, 0, len(s)-1)
	start := 0
	for i := 0; i <= len(byteStr); i++ {
		if byteStr[i] == ' ' || i == len(byteStr) {
			reverseStr1(byteStr, start, i-1)
			start = i + 1
		}
	}

	return s
}

// 移除多余的空格，快慢指针,快指针遍历整个字符串
// 慢指针表示去除空格后新的字符串的下标
func removeSpace(byteStr []byte) {
	slow := 0
	for fast := 0; fast < len(byteStr); fast++ {
		if byteStr[fast] != ' ' {
			if slow != 0 {
				byteStr[slow] = ' '
				slow++
			}

			for fast < len(byteStr) && byteStr[fast] != ' ' {
				byteStr[slow] = byteStr[fast]
				fast++
				slow++
			}
		}
	}

}

// 左闭右闭区间的反转
func reverseStr1(byteStr []byte, start, end int) {
	for start < end {
		byteStr[start], byteStr[end] = byteStr[end], byteStr[start]
		start++
		end--
	}
}

// @lc code=end
