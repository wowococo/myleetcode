/*
 * @lc app=leetcode.cn id=202 lang=golang
 *
 * [202] 快乐数
 */

package main

// 如果 sum 重复出现了，表示进入了死循环
// 判断 sum 是否在集合里出现过，考虑哈希法

// @lc code=start
func isHappy(n int) bool {
	sumMap := make(map[int]int)
	for {
		currentSum := getSum(n)
		if currentSum == 1 {
			return true
		}

		if _, ok := sumMap[currentSum]; ok {
			return false
		}

		sumMap[currentSum] = 1
		n = currentSum
	}
}

// 各个位上的单数操作
func getSum(n int) int {
	var sum int
	for n != 0 {
		mod := n % 10
		sum += mod * mod
		n = n / 10
	}

	return sum
}

// @lc code=end
