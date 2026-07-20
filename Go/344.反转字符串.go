/*
 * @lc app=leetcode.cn id=344 lang=golang
 *
 * [344] 反转字符串
 */
package main

// @lc code=start
func reverseString(s []byte) {
	// left, right 也是[] 左闭右闭
	left, right := 0, len(s)-1

	// left=right的时候没必要替换值，所以left<right
	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}

// @lc code=end
