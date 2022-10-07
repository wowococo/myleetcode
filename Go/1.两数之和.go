/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

package main

// 使用哈希表存储已经遍历过的数
// 需要判断target-nums[i]是否在哈希表中，最后要求返回下标
// 因此哈希表的数据结构选择map，key存储num，value存下标
// @lc code=start
func twoSum(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	for index, num := range nums {
		if i, ok := m[target-num]; ok {
			return []int{i, index}
		}

		m[num] = index
	}

	return []int{}
}

// @lc code=end
