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
func intersectionSet(nums1 []int, nums2 []int) []int {
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

// 数组形式, 存储 nums1 的用数组。
// 也可以存储 nums1 的哈希表用 set，存储 result 的用数组
func intersection(nums1 []int, nums2 []int) []int {
	numsSet := make([]int, 1001)
	resultSet := make(map[int]int, 0)
	var result []int
	for _, num := range nums1 {
		numsSet[num] = 1
	}

	for _, num := range nums2 {
		if numsSet[num] == 1 {
			resultSet[num] = 1
		}
	}

	for num := range resultSet {
		result = append(result, num)
	}

	return result
}

// @lc code=end
// func main() {
// 	nums1 := []int{1, 2, 2, 1}
// 	nums2 := []int{2, 2}
// 	intersection(nums1, nums2)
// }
