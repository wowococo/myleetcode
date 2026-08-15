/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */
package main

// @lc code=start
func maxArea(height []int) int {
	// 双指针分别在数组第一个和最后一个，计算每次移动时的面积
	// 关键是如何移动：每次移动短板的指针，因为如果移动长板指针，面积肯定是会缩小的（可以自己去推），如果移动短板指针，面积是有可能增大的
	// 面积公式：（R-L）* min(height[l], height[r])

	left, right := 0, len(height)-1
	res := 0
	for left < right {
		area := (right - left) * min(height[left], height[right])
		res = max(res, area)
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return res
}

// @lc code=end
