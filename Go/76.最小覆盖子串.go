/*
 * @lc app=leetcode.cn id=76 lang=golang
 *
 * [76] 最小覆盖子串
 */
package main

import "math"

// @lc code=start
func minWindow(s string, t string) string {
	// 两个哈希表，一个哈希表用来存储 t 的字符频率，
	// 另一个哈希表用来存储 s 的在 t 里的字符频率，
	// 使用一个变量have存储符合的字符数量， 另外 tcount=len(tmap)
	// windowMap[char] >= tmap[char], 这个字符是符合条件的，不过 have++的时候判断windowMap[char] == tmap[char] 就行了，避免重复+have
	// 子串满足条件的时候，left++收缩窗口
	// 子串不满足条件的时候，right++扩大窗口

	m, n := len(s), len(t)
	if m == 0 || n == 0 {
		return ""
	}

	windowMap := make(map[byte]int, n)
	tmap := make(map[byte]int, n)
	for i := 0; i < n; i++ {
		tmap[t[i]]++
	}

	tcount := len(tmap)
	have := 0
	resStart, resLen := 0, math.MaxInt
	left, right := 0, 0
	for right < m {
		rightChar := s[right]
		// 如果字符在 tmap 里，存入 windowMap
		if _, ok := tmap[rightChar]; ok {
			windowMap[rightChar]++
			// 如果这个字符的频率等于 tmap 中的频率了，have++
			if windowMap[rightChar] == tmap[rightChar] {
				have++
			}
		}

		// 如果子串满足条件，准备收缩窗口
		for have == tcount {
			// 更新 resStart 和 resLen
			curWinLen := right - left + 1
			if curWinLen < resLen {
				resLen = curWinLen
				resStart = left
			}

			leftChar := s[left]
			// 如果字符在 tmap 里，windowMap 中频率--
			if _, ok := tmap[leftChar]; ok {
				windowMap[leftChar]--

				// 如果这个字符的频率小于 tmap 中的频率了，have--
				if windowMap[leftChar] < tmap[leftChar] {
					have--
				}
			}

			// 收缩窗口
			left++
		}

		// 子串不满足条件了，扩大窗口
		right++
	}

	if resLen == math.MaxInt {
		return ""
	}
	return s[resStart : resStart+resLen]
}

// @lc code=end
