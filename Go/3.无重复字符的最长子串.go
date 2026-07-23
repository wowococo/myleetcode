/*
 * @lc app=leetcode.cn id=3 lang=golang
 *
 * [3] 无重复字符的最长子串
 */
package main

import "fmt"

// @lc code=start
func lengthOfLongestSubstring(s string) int {
	// 遇到子串问题就要想到滑动窗口，滑动窗口意味着双指针，还有一个或者两个哈希表存储窗口里的值
	// 滑动窗口就是向右移动，不满足条件的就把左边的移出去，然后继续向右移动
	left := 0
	var res int
	// memo 用来存储每个字符出现的次数
	memo := make(map[byte]int)
	for right := 0; right < len(s); right++ {
		rightChar := s[right]
		memo[rightChar]++
		for memo[rightChar] > 1 {
			leftChar := s[left]
			memo[leftChar]--
			left++

		}

		res = max(res, right-left+1)
	}

	return res
}

// @lc code=end
// 至多包含两个不同字符的最长子串
// 至多包含两个不同字符的最长子串
func lengthOfLongestSubstringTwoDistinct(s string) int {
	if len(s) <= 2 {
		return len(s)
	}

	// 哈希表：记录窗口内每个字符出现的次数
	counts := make(map[byte]int)
	left := 0
	maxLen := 0

	// right 移动代表扩大窗口
	for right := 0; right < len(s); right++ {
		c := s[right]
		counts[c]++

		// 当不同字符种类超过 2 个时，移动 left 收缩窗口
		for len(counts) > 2 {
			leftChar := s[left]
			counts[leftChar]--
			// 频次归零后，从 map 中移除该键，确保 len(counts) 代表真正的不同字符数
			if counts[leftChar] == 0 {
				delete(counts, leftChar)
			}
			left++
		}

		// 更新最大长度
		if right-left+1 > maxLen {
			maxLen = right - left + 1
		}
	}

	return maxLen
}

func main() {
	fmt.Println(lengthOfLongestSubstringTwoDistinct("eceba"))   // 输出: 3 (子串 "ece")
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaabbb")) // 输出: 5 (子串 "aabbb")
}
