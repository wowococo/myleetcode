/*
 * @lc app=leetcode.cn id=347 lang=golang
 *
 * [347] 前 K 个高频元素
 */
package main

// @lc code=start
func topKFrequent(nums []int, k int) []int {
	// 使用最小堆的时间复杂度是 O（nlogk）
	// 使用桶排序的时间复杂度是 O（n）
	// 1. 哈希表存储数组的元素及对应的频率
	// 2. 大小为 n+1 的数组存储频率及对应的元素，这个数组索引是频率，值是个数组存储频率为它的元素们
	// 3. 倒序遍历这个数组，找出 k 个元素停止

	mp := make(map[int]int)
	freq := make([][]int, len(nums)+1)
	for _, num := range nums {
		mp[num]++
	}

	for key, val := range mp {
		freq[val] = append(freq[val], key)
	}

	// 逆序选取 k 个元素
	res := []int{}
	for i := len(freq) - 1; i >= 0; i-- {
		for _, num := range freq[i] {
			res = append(res, num)
			// 如果元素的数量达到 k 了，直接返回
			if len(res) == k {
				return res
			}
		}
	}

	// 如果 数量没有达到 k，也返回 res
	return res
}

// @lc code=end
