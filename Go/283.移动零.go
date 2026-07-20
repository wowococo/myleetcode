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
	// 双指针法, j指向非零元素的下标，i 指向当前遍历的元素下标
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
	}
	// 将剩余位置填充为0
	for j < len(nums) {
		nums[j] = 0
		j++
	}
}

// @lc code=end

// 一次遍历，借鉴快速排序的思路，快速排序的思想就是确定一个中间点 x，
// 把小于等于 x的元素放在其左边，大于x 的元素放在右边
// 应用在这里就是把 0 当做这个中间点，
// 不等于 0 的元素放在左边，等于 0 的元素放在右边

func moveZeroes2(nums []int) {
	// 双指针法, j指向非零元素的下标，i 指向当前遍历的元素下标
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j], nums[i] = nums[i], nums[j]
			j++
		}
	}
}
