/*
 * @lc app=leetcode.cn id=344 lang=golang
 *
 * [344] 反转字符串
 */
package main

// @lc code=start
func reverseString(s []byte) {
	left, right := 0, len(s)-1

	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}

// @lc code=end
