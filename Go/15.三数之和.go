/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */
package main

import "sort"

// @lc code=start
func threeSum(nums []int) [][]int {
	// 去重可以通过哈希表或者排序的方式，这种情况比较适合的情况是排序
	// 先对数组进行排序，固定一个a 之后，剩下的是求两数之和等于-a，可以参考
	// 两数之和双指针的解法，核心逻辑是遍历的时候，如果 a 和 left 都和上一位
	// 相同，则跳过，
	// 如果 nums[a]+nums[left]+nums[right] == 0: 将三元组填入结果
	// 如果 nums[a]+nums[left]+nums[right] < 0: 因为是排序的，所以可以left++
	// 如果 nums[a]+nums[left]+nums[right] > 0: right--

	sort.Ints(nums)
	res := [][]int{}
	for a := 0; a < len(nums); a++ {
		// a 去重
		if a > 0 && nums[a] == nums[a-1] {
			continue
		}

		left, right := a+1, len(nums)-1
		for left < right {
			sum := nums[a] + nums[left] + nums[right]
			if sum == 0 {
				res = append(res, []int{nums[a], nums[left], nums[right]})
				left++
				// [-1, -1, -1, 0, 2]
				//   a, left       right
				// 避免这种情况，命中解之后，left 去重
				for left < right && nums[left] == nums[left-1] {
					left++
				}
				// right 去不去重都行，因为已经对a 和 left 去重了，不会出现同样的a+b+c=0的三元组
			} else if sum < 0 {
				left++
			} else {
				right--
			}
		}
	}

	return res
}

// @lc code=end
