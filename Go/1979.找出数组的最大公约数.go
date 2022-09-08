/*
 * @lc app=leetcode.cn id=1979 lang=golang
 *
 * [1979] 找出数组的最大公约数
 */
package main

// @lc code=start
func findGCD(nums []int) int {
	min, max := nums[0], nums[0]
	for _, num := range nums {
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}

	return gcd(min, max)
}

func gcd(a, b int) int {
	for a != 0 {
		a, b = b%a, a
	}
	return b
}

// func main() {
// 	a := []int{2, 5, 6, 9, 10}
// 	findGCD(a)
// }

// @lc code=end
