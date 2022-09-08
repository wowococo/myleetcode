/*
 * @lc app=leetcode.cn id=27 lang=golang
 *
 * [27] 移除元素
 */
package main

// @lc code=start
func removeElement(nums []int, val int) int {
	var slow int
	for _, num := range nums {
		if num != val {
			nums[slow] = num
			slow++
		}
	}
	return slow
}

// @lc code=end
