/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start
func trap(height []int) int {
	left, right := 0, len(height)-1
	leftMax, rightMax := height[left], height[right]
	res := 0
	for left <= right {
		leftMax = max(height[left], leftMax)
		rightMax = max(height[right], rightMax)
		if leftMax < rightMax {
			res += leftMax - height[left]
			left++
		} else {
			res += rightMax - height[right]
			right--
		}
	}

	return res
}

// @lc code=end

