/*
 * @lc app=leetcode.cn id=240 lang=golang
 *
 * [240] 搜索二维矩阵 II
 */
package main

// @lc code=start
func searchMatrixII(matrix [][]int, target int) bool {
	// 最上面一行到最后一行这条路都是升序的
	// 整行整列切除，从右上角开始比较，根据大小决定切右边的列还是切上面行
	m, n := len(matrix), len(matrix[0])
	startRow, startCol := 0, n-1
	for startRow < m && startCol >= 0 {
		val := matrix[startRow][startCol]
		if val == target {
			return true
		} else if val < target {
			startRow++
		} else {
			startCol--
		}
	}

	return false
}

// @lc code=end
