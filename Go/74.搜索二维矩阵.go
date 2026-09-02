/*
 * @lc app=leetcode.cn id=74 lang=golang
 *
 * [74] 搜索二维矩阵
 */
package main

// @lc code=start
func searchMatrix(matrix [][]int, target int) bool {
	// 二维矩阵展开为一维的去做二分查找
	// 假设一维的索引是 i，对应到二维矩阵的位置：
	// row = i / n
	// col = i % n
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	m := len(matrix)
	n := len(matrix[0])

	left, right := 0, m*n-1
	for left <= right {
		mid := left + (right-left)/2
		row := mid / n
		col := mid % n

		val := matrix[row][col]
		if val == target {
			return true
		} else if val < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false
}

// @lc code=end
