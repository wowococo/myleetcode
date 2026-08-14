package main

import "fmt"

/*
接雨水
题目描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
下雨之后能接多少雨水

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1]表示的高度图，在这种情况下，
可以接 6 个单位的雨水（蓝色部分表示雨水）
示例：
输入：[0,1,0,2,1,0,1,3,2,1,2,1]
输出：6


*/

// 核心思路：木桶理论：对于任何位置 i 的柱子，它的存水量取决于左边最高柱子leftMax
// 和右边最高柱子 rightMax 中较矮的那一个（短板效应）
// 水高度[i] = min(leftMax, rightMax) - height[i]
// 如果短板 <= height[i], 则该位置无法存水
// 关键突破点：如果 leftMax < rightMax, 哪怕 right 指针左侧还有更高的柱子，此时
// left 处的短板也绝对是 leftMax, 因此可以放心计算 left 处的存水量，并将 left 右移。
// 反之如果 leftMax >= rightMax, 则 right 处的短板一定是 rightMax，计算right 处的存水量并将 right 左移。

// 双指针
// 时间复杂度：O(N) -- 两个指针相向而行，仅需遍历数组一次
// 空间复杂度：O(1) -- 仅使用常数级别的指针与临时变量
func collectingRainWater(height []int) int {
	// 边界处理：小于 3 根柱子无法形成水槽，直接返回 0
	if len(height) < 3 {
		return 0
	}

	// 这里 right 指向的是最后一个下标
	// 一般双指针左右两边相向而行遍历的时候，right 都是指向的是最后一个下标
	left, right := 0, len(height)-1
	leftMax, rightMax := 0, 0
	totalWater := 0

	// 左右指针相向移动，直到相遇，相遇就退出循环，因为相遇的时候不能存水了
	for left < right {
		// 1. 实时更新左右两边各自遍历过的最大高度
		if height[left] > leftMax {
			leftMax = height[left]
		}

		if height[right] > rightMax {
			rightMax = height[right]
		}

		// 2.依据短板效应进行状态转移
		if leftMax < rightMax {
			// 左侧是短板，left 处的接水量只由 leftMax 决定
			totalWater += leftMax - height[left]
			left++
		} else {
			// 右侧是短板，right 处的接水量只由 rightMax 决定
			totalWater += rightMax - height[right]
			right--
		}
	}

	return totalWater
}

func main5() {
	fmt.Println(collectingRainWater([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1})) // 打印出 6

	// 边界测试：长度小于 3
	fmt.Printf("边界用例 (<3): %d\n", collectingRainWater([]int{2, 1})) // 输出: 0

	// 边界测试：无法接水的梯形递增
	fmt.Printf("边界用例 (递增): %d\n", collectingRainWater([]int{1, 2, 3, 4})) // 输出: 0
}
