/*
 * @lc app=leetcode.cn id=541 lang=golang
 *
 * [541] 反转字符串 II
 */
package main

// @lc code=start
func reverseStr(s string, k int) string {
	str := []byte(s)
	for i:=0; i < len(s); i+=2*k {
		// >=  2k
		// k <= 剩下字符 < 2k
		if i+k <= len(s) {
			reverseByteStr(str, i, i+k)
		} else {
			// < k
			reverseByteStr(str, i, len(s))
		}
	}

	return string(str)

}

func reverseByteStr(s []byte, start, end int) {
	left, right := start, end-1
	for left < right {
		s[left], s[right] = s[right], s[left]
		left++
		right--
	}
}

// @lc code=end
