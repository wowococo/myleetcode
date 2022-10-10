/*
 * @lc app=leetcode.cn id=242 lang=golang
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
package main

func isAnagram(s string, t string) bool {
	hash := make([]int, 26)
	for _, char := range s {
		hash[char-'a']++
	}

	for _, char := range t {
		hash[char-'a']--
	}

	for _, val := range hash {
		if val != 0 {
			return false
		}
	}

	return true
}

// @lc code=end
