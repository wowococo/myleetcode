/*
 * @lc app=leetcode.cn id=283 lang=golang
 *
 * [283] 移动零
 */

package main

//	二次遍历
//
// @lc code=start
func moveZeroes(nums []int) {
	// 双指针法
	// 不复制数组的情况下，使用快排的思想，但要保持非零元素的相对顺序
	// 这个双指针起始点都从数组的开始,left用来操作左侧非零元素的赋值，right 用来遍历数组找到非零元素
	left := 0
	for right := 0; right < len(nums); right++ {
		if nums[right] != 0 {
			nums[left], nums[right] = nums[right], nums[left]
			left++
		}
	}
}

// @lc code=end
