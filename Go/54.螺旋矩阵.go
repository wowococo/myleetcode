/*
 * @lc app=leetcode.cn id=54 lang=golang
 *
 * [54] 螺旋矩阵
 */
package main

// @lc code=start
func spiralOrder(matrix [][]int) []int {
	// 模拟遍历，关键点是：
	// 1. 确定上下左右四个边界
	// 2. 实时更新边界
	m, n := len(matrix), len(matrix[0])
	res := make([]int, 0, m*n)
	left, right, top, bottom := 0, n, 0, m
	for left < right && top < bottom {
		// 1.从左到右最上面一行
		for i := left; i < right; i++ {
			res = append(res, matrix[top][i])
		}
		top++
		if top >= bottom {
			break
		}

		// 2. 从上到下遍历最右边一列
		for j := top; j < bottom; j++ {
			res = append(res, matrix[j][right-1])
		}
		right--
		if left >= right {
			break
		}

		// 3. 从右到左遍历最下面一行
		for k := right - 1; k >= left; k-- {
			res = append(res, matrix[bottom-1][k])
		}
		bottom--
		if top >= bottom {
			break
		}

		// 4. 从下到上遍历最左边一列
		for h := bottom - 1; h >= top; h-- {
			res = append(res, matrix[h][left])
		}
		left++
	}

	return res
}

// @lc code=end
