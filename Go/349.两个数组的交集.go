/*
 * @lc app=leetcode.cn id=349 lang=golang
 *
 * [349] 两个数组的交集
 */

// @lc code=start
package main

// 如果没有限定数组的值的大小的话，用 set 比较合适。
// 规定了 nums 的大小和数值大小，也可使用数组。
// 思路：将 nums1 的数存到一个哈希表里，遍历nums2，判断
// nums2 的每个元素是否在哈希表里，如果在的话就加入到
// 结果哈希表里(因为要去重)。
func intersection(nums1 []int, nums2 []int) []int {
	var result []int
	numsMap := make(map[int]int, len(nums1))
	resultMap := make(map[int]int)

	for _, num := range nums1 {
		numsMap[num] = 1
	}

	for _, num := range nums2 {
		if _, ok := numsMap[num]; ok {
			resultMap[num] = 1
		}
	}

	for num := range resultMap {
		result = append(result, num)
	}

	return result
}

// @lc code=end
