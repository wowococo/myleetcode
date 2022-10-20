/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */
package main

import "sort"

// @lc code=start
// 使用哈希法太过繁琐，改用三指针法
func threeSum(nums []int) [][]int {
	var result [][]int

	sort.Ints(nums)
	for i, num := range nums {
		if num > 0 {
			return result
		}

		// 对 a 去重
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		left := i + 1
		right := len(nums) - 1
		for left < right {
			sum := num + nums[left] + nums[right]
			if sum > 0 {
				right--
			} else if sum < 0 {
				left++
			} else {
				result = append(result, []int{num, nums[left], nums[right]})
				// 对b去重
				for left < right && nums[left] == nums[left+1] {
					left++
				}

				// 对c去重
				for left < right && nums[right] == nums[right-1] {
					right--
				}
				
				left++
				right--
			}

		}
	}

	return result

}

// @lc code=end
