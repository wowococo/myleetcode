/*
 * @lc app=leetcode.cn id=165 lang=golang
 *
 * [165] 比较版本号
 */
package main

import (
	"strconv"
	"strings"
)

// @lc code=start
func compareVersion(version1 string, version2 string) int {
	m, n := len(version1), len(version2)
	i, j := 0, 0
	for i < m || j < n {
		var num1, num2 int

		for i < m && version1[i] != '.' {
			num1 = num1*10 + int(version1[i]-'0')
			i++
		}

		for j < n && version2[j] != '.' {
			num2 = num2*10 + int(version2[j]-'0')
			j++
		}

		if num1 > num2 {
			return 1
		}

		if num1 < num2 {
			return -1
		}

		// 跳过 "."
		i++
		j++
	}

	return 0
}

// 第一种解法思路比较直接，拆分字符串为数组，遍历比较
func compareVersion1(version1 string, version2 string) int {
	part1 := strings.Split(version1, ".")
	part2 := strings.Split(version2, ".")

	m, n := len(part1), len(part2)
	maxLen := m
	if n > maxLen {
		maxLen = n
	}

	for i := 0; i < maxLen; i++ {
		var num1, num2 int
		if i < m {
			num1, _ = strconv.Atoi(part1[i])
		}

		if i < n {
			num2, _ = strconv.Atoi(part2[i])
		}

		if num1 > num2 {
			return 1
		}

		if num1 < num2 {
			return -1
		}
	}

	return 0
}

// @lc code=end
