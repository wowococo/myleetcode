package main

import "fmt"

// 记住一个原则：用数组的第一个元素 nums[0] 来初始化 currentSum
// 和 maxSum, 这是处理这类"最大子数组和"问题最无懈可击的写法，能天然防御全负数边界。

/*
求数组的最大区间和

题目描述：
输出一个 int 型数组的最大连续子数组（所有元素加和最大）各个元素之和
# 保证数组中至少有一个正数

例：
输入： {1,2,3,-7,8,-10}
输出 9（子数组为： {1,2,5,-7,8}）
*/

// 假设没有"保证数组至少有一个正数"这个提示，最标准的做法是：
// 1. maxSum 和 currentSum 初始为 nums[0]
// 2. 遍历 nums 时，对于当前元素 num，我们需要决定的是：
// 2.1: 加入前面的子数组和
// 2.2: 抛弃前面的子数组和，从当前 num 开始 （如果 currentSum < 0 就抛弃，
// 因为一个负数加上任何数都会把这个数拉低）
// 只要边遍历边维护一个全局的最大值 maxSum，遍历完一次数组就能得到最终答案

// 时间复杂度：O(N)：只需对数组进行一次单向遍历
// 空间复杂度：O(1)：仅使用了常数级的变量存储状态，无需额外空间
func maxSubArray(nums []int) int {
	// 边界处理：防御 nil 或者空切片
	if len(nums) == 0 {
		return 0
	}

	// 初始化 currentSum 和 maxSum 为第一个元素
	currentSum := nums[0]
	maxSum := nums[0]

	// 从第二个元素开始遍历
	for i := 1; i < len(nums); i++ {
		// 如果当前累加和小于 0，说明前面的积累只会拖累当前值，果然重新开始
		if currentSum < 0 {
			currentSum = nums[i]
		} else {
			currentSum += nums[i]
		}

		// 实时更新全局最大值
		if currentSum > maxSum {
			maxSum = currentSum
		}
	}

	return maxSum
}

/*
💡 面试加分项（追问处理）
如果面试官追问：“如果我不光要输出最大和，还要求输出具体是哪个子数组（比如输出 {1, 2, 5, -7, 8}），该怎么写？”

你可以立刻补上记录索引的逻辑：只要在 currentSum < 0 重置起点时更新临时左边界 tempStart，在更新 maxSum 时同步记录最终的 bestStart 和 bestEnd 即可。
*/

// "保证数组中至少有一个正数"是降难度的提示，提示子数组和肯定是大于 0 的，因为最差可以只用这1 个正数
// 在这种前提下，有个简化写法
func maxSubArrayEasy(nums []int) int {
	// 保证有正数的前提下，可以初始化为 0
	currentSum := 0
	maxSum := 0

	for _, num := range nums {
		currentSum += num
		if currentSum < 0 {
			currentSum = 0 // 累加和小于 0 就归零重来
		}

		if currentSum > maxSum {
			maxSum = currentSum
		}
	}

	return maxSum
}

func maxSubArrayOutputSubArray(nums []int) (int, []int) {
	// 边界处理：防御 nil 或者空切片
	if len(nums) == 0 {
		return 0, nil
	}

	// 初始化 currentSum 和 maxSum 为第一个元素
	currentSum := nums[0]
	maxSum := nums[0]
	// 记录全局最大和的子数组边界 [bestStart, bestEnd]
	bestStart, bestEnd := 0, 0
	// 记录当前累加部分的临时起点
	tempStart := 0

	// 从第二个元素开始遍历
	for i := 1; i < len(nums); i++ {
		// 如果当前累加和小于 0，说明前面的积累只会拖累当前值，果然重新开始
		if currentSum < 0 {
			currentSum = nums[i]
			tempStart = i // 重新记录候选子数组的起点
		} else {
			currentSum += nums[i]
		}

		// 实时更新全局最大值
		if currentSum > maxSum {
			maxSum = currentSum
			// 同时更新最佳子数组的左右边界
			bestStart = tempStart
			bestEnd = i
		}
	}

	return maxSum, nums[bestStart : bestEnd+1]
}

/*
	核心结论
	tempStart 绝对不能省略。

	必须遵循“候选与转正分离”的原则：

	在 currentSum < 0 时：只更新候选起点 tempStart；

	只有在真正刷新了 maxSum 的那一刻（即 currentSum > maxSum），才能把 tempStart 的值赋给 bestStart，
	完成“转正”。
*/

func main3() {
	fmt.Println(maxSubArray([]int{1, 2, 5, -7, 8, -10})) // 输出 9
	fmt.Println(maxSubArray([]int{-1, -2, -5, -7, -10})) // 输出 -1
	fmt.Println(maxSubArray([]int{5}))                   // 输出 5

	fmt.Println(maxSubArrayOutputSubArray([]int{1, 2, 5, -7, 8, -10})) // 输出 [1, 2, 5, -7, 8]
	fmt.Println(maxSubArrayOutputSubArray([]int{-1, -2, -5, -7, -10})) // 输出 [-1]
	fmt.Println(maxSubArrayOutputSubArray([]int{5}))                   // 输出 [5]
}
