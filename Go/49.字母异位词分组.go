/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 */
package main

import "sort"

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	// 不用排序，天然利用 26 个英文字母的有序性，统计字符出现的频率
	// key 为 长度为 26 的字符串，每个位置代表从 a 到 z 的字符，每个位置的值表示这个字符出现的次数
	memo := make(map[string][]string)

	for _, str := range strs {
		count := [26]byte{} // [26]byte 数组，初始全 0
		for _, char := range str {
			count[char-'a']++
		}

		key := string(count[:])
		memo[key] = append(memo[key], str)

	}

	res := make([][]string, 0, len(memo))
	for _, val := range memo {
		res = append(res, val)
	}

	return res
}

// @lc code=end

// 最朴素的想法
// 时间复杂度：O（m * n * logn)
// 空间复杂度：O（m * n）
func groupAnagramsMine(strs []string) [][]string {
	memoMap := make(map[string][]string, len(strs))
	for _, str := range strs {
		sorted := sortStr(str)
		if exist, ok := memoMap[sorted]; ok {
			exist = append(exist, str)
			memoMap[sorted] = exist
		} else {
			memoMap[sorted] = []string{str}
		}
	}

	res := make([][]string, 0, len(memoMap))
	for _, val := range memoMap {
		res = append(res, val)
	}

	return res
}

// 排序问题不会
func sortStr(s string) string {
	rStr := []rune(s)
	sort.Slice(rStr, func(i, j int) bool {
		return rStr[i] < rStr[j]
	})

	return string(rStr)
}
