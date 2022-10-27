/*
 * @lc app=leetcode.cn id=18 lang=golang
 *
 * [18] 四数之和
 */
package main

import "sort"

// @lc code=start
func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)

	var result [][]int

	for i := 0; i < len(nums); i++ {
		// 剪枝
		if nums[i] > target && nums[i] >= 0 {
			break
		}

		// 对a去重
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		for j := i + 1; j < len(nums); j++ {
			// 剪枝
			if nums[i]+nums[j] > target && nums[i]+nums[j] >= 0 {
				break
			}

			// 对b去重
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			left, right := j+1, len(nums)-1
			for right > left {
				sum := nums[i] + nums[j] + nums[left] + nums[right]
				if sum < target {
					left++
				} else if sum > target {
					right--
				} else {
					result = append(result, []int{nums[i], nums[j], nums[left], nums[right]})
					// 对c去重
					for right > left && nums[left] == nums[left+1] {
						left++
					}
					// 对d去重
					for right > left && nums[right] == nums[right-1] {
						right--
					}

					left++
					right--
				}
			}

		}
	}

	return result
}

// @lc code=end
