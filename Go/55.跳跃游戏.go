/*
 * @lc app=leetcode.cn id=55 lang=golang
 *
 * [55] 跳跃游戏
 */
package main

// @lc code=start
func canJump(nums []int) bool {
	// 定义目标下标 target 初始值为数组的最大的下标
	// 将数组从倒数第二个开始向左遍历，比如 i = 3 时，向后最大跳 nums[i] 步
	// i+nums[i] >= target, 说明 i 可以跳到 target，只要前面的能跳到 i 的位置，
	// 也就能跳到最后元素的位置，所以我们将 target 更新为 i，接下来继续看能不能跳跃到 i
	// 走到最后循环结束时 target 为 0 就表示 true
	n := len(nums)
	target := n - 1
	for i := n - 2; i >= 0; i-- {
		if i+nums[i] >= target {
			target = i
		}
	}

	if target == 0 {
		return true
	}
	return false
}

// @lc code=end
