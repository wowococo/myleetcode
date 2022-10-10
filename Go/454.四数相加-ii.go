/*
 * @lc app=leetcode.cn id=454 lang=golang
 *
 * [454] 四数相加 II
 */
package main

// @lc code=start
func fourSumCount(nums1 []int, nums2 []int, nums3 []int, nums4 []int) int {
	// 暴力法：四层循环遍历，统计a+b+c+d=0的个数，O(n^4)
	// 如何想到哈希法：查找一个元素是否在集合里出现过，
	// 使用哪种哈希结构：map。数组不合适，因为nums[i]太大，做下标的话会导致数组很大。
	// 因为需要有a+b的值，以及出现的次数，因此key-value结构的map更合适。
	// 思路：先统计a+b的次数，然后遍历计算c+d的时候，去哈希表中查找-(c+d)=a+b的次数
	m := make(map[int]int)
	for _, num1 := range nums1 {
		for _, num2 := range nums2 {
			m[num1+num2]++
		}
	}

	var result int
	for _, num3 := range nums3 {
		for _, num4 := range nums4 {
			val := -(num3 + num4)
			if count, ok := m[val]; ok {
				result += count
			}
		}
	}

	return result
}

// @lc code=end
