/*
 * @lc app=leetcode.cn id=209 lang=golang
 *
 * [209] 长度最小的子数组
 */
package main

import "math"

// @lc code=start
func minSubArrayLen(target int, nums []int) int {
	l := len(nums)
	max := l + 1
	minSubLength := max
	var sum, i, subLength int
	for j := 0; j < l; j++ {
		sum += nums[j]
		for sum >= target {
			subLength = j - i + 1
			if subLength < minSubLength {
				minSubLength = subLength
			}
			sum -= nums[i]
			i++
		}
	}
	if minSubLength == max {
		return 0
	}

	return minSubLength
}

// 暴力法，超时
func minSubArrayLenSolution1(target int, nums []int) int {
	max := int(math.Pow(5, 10)) + 1
	minSubLength := max
	for i, _ := range nums {
		var sum, subLength int
		for j := i; j < len(nums); j++ {
			sum += nums[j]
			subLength = j - i + 1
			if sum >= target && subLength < minSubLength {
				minSubLength = subLength
			}
		}
	}

	if minSubLength == max {
		return 0
	}
	return minSubLength
}

// @lc code=end

