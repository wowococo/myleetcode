/*
 * @lc app=leetcode.cn id=56 lang=golang
 *
 * [56] 合并区间
 */
package main

import "sort"

// @lc code=start
func mergeInterval(intervals [][]int) [][]int {
	// 尝试画一条线段，更方便理解，然后用程序模拟这个过程
	// 先对区间按照 start 排序，tempStart, tempEnd 初始化为第一个区间
	// 遍历后面区间的过程中，不断更新临时区间，如果碰见临时区间的终点 >= 当前区间的起点
	// 可以合并成一个新的临时区间
	res := make([][]int, 0)
	if len(intervals) < 1 {
		return res
	}

	// 按区间左端点排序
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	tempStart := intervals[0][0]
	tempEnd := intervals[0][1]

	for i := 1; i < len(intervals); i++ {
		if tempEnd >= intervals[i][0] {
			tempEnd = max(tempEnd, intervals[i][1])
			// 不用更新 tempStart，因为已经是排好序的
		} else {
			res = append(res, []int{tempStart, tempEnd})
			tempStart = intervals[i][0]
			tempEnd = intervals[i][1]
		}
	}
	res = append(res, []int{tempStart, tempEnd})
	return res
}

// @lc code=end
