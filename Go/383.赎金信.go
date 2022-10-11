/*
 * @lc app=leetcode.cn id=383 lang=golang
 *
 * [383] 赎金信
 */
package main

// @lc code=start
func canConstruct1(ransomNote string, magazine string) bool {
	// 和字母异位词差不多，使用的哈希表的数据结构是数组，
	// 思路：将ransonNote的各个字符存到数组中，数组的索引是字符 - a,
	// 值是这个字符出现的次数
	record := make([]int, 26)
	for _, char := range ransomNote {
		record[char-'a']++
	}

	for _, char := range magazine {
		record[char-'a']--
	}

	for _, val := range record {
		if val > 0 {
			return false
		}
	}

	return true
}

// @lc code=start
func canConstruct(ransomNote string, magazine string) bool {
	record := make([]int, 26)
	for _, char := range magazine {
		record[char-'a']++
	}

	for _, char := range ransomNote {
		record[char-'a']--
		if record[char-'a'] < 0 {
			return false
		}
	}

	return true
}

// @lc code=end
