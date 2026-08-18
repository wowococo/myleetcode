/*
 * @lc app=leetcode.cn id=438 lang=golang
 *
 * [438] 找到字符串中所有字母异位词
 */
package main

// @lc code=start
func findAnagrams(s string, p string) []int {
	// 滑动窗口，两个 map ，一个 map need_match 用来存储 p 的每个字符频率
	// 另一个 map 用来存储窗口中每个字符的频率，只存储在 p 中的字符即可
	// 还需要用一个变量 match 存储窗口中字符频率 = p中字符频率 的个数，
	// 如果窗口的长度等于 p 的长度并且  match 的长度等于 len(need_match)的长度，将窗口的左侧索引加入结果中
	// 什么时候收缩窗口呢，就是窗口的长度等于 p 的长度时，需要找下一个这个长度的子串了
	// 将窗口的左侧索引加入结果中
	res := make([]int, 0)
	if len(s) < len(p) {
		return res
	}

	need_match := make(map[byte]int)
	window := make(map[byte]int)

	for i := 0; i < len(p); i++ {
		need_match[p[i]]++
	}

	left, right := 0, 0
	match := 0

	for right < len(s) {
		rightChar := s[right]
		right++

		if _, ok := need_match[rightChar]; ok {
			window[rightChar]++

			if window[rightChar] == need_match[rightChar] {
				match++
			}
		}

		for right-left == len(p) {
			if match == len(need_match) {
				res = append(res, left)
			}

			leftChar := s[left]
			left++
			if _, ok := need_match[leftChar]; ok {
				if window[leftChar] == need_match[leftChar] {
					match--
				}

				window[leftChar]--
			}
		}
	}

	return res
}

// @lc code=end
