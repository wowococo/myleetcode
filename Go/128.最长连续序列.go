/*
 * @lc app=leetcode.cn id=128 lang=golang
 *
 * [128] 最长连续序列
 */
package main

// @lc code=start
func longestConsecutive(nums []int) int {
	// 将数组中的元素都存到 map 里，遍历每一个元素，判断这个元素
	// 数组中的元素可以分为多个序列
	// 是不是序列的开头（-1 的值是否在数组中），如果是开头，就继续
	// 判断 +1， +2， +3 ..... +n 是不是在数组中（可以得出以这个开头的序列长度多少）

	mp := make(map[int]bool)
	for _, num := range nums {
		mp[num] = true
	}

	maxLen := 0
	// 这里很重要，要遍历去重后的 map，如果遍历 nums，就会超时
	for num := range mp {
		if !mp[num-1] {

			curLen := 1
			i := 1
			for mp[num+i] {
				curLen++
				i++
			}

			maxLen = max(maxLen, curLen)
		}
	}

	return maxLen
}

// @lc code=end
