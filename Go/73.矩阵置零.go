/*
 * @lc app=leetcode.cn id=73 lang=golang
 *
 * [73] 矩阵置零
 */
package main

// @lc code=start
func setZeroes(matrix [][]int) {
	// 另外复制一个矩阵使用空间 0（mn）
	// 使用两个额外的数组分别表示、对应的列是否需要置为 0、对应的行是否需要置为 0，使用空间 O（m+n）
	// 进一步想，这两个数组可以平移到矩阵的首行和首列，但是会重叠矩阵的第一个元素，
	// 我们可以使用一个额外的变量来存储，避免重叠
	// 矩阵第 0 行（蓝色） 用来存储对应的列是否需要置为 0
	// 矩阵第 0 列（绿色） 用来存储对应的行是否需要置为 0

	m, n := len(matrix), len(matrix[0])
	// 绿色，表示矩阵的第一行是否需要置为 0，初始为 1,1 表示不需要置为 0
	zeroRow := 1
	// 1. 遍历整个矩阵，如果当前坐标元素为 0，首先需要修改第 0 行和第 0 列对应的标记
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if matrix[row][col] == 0 {
				// 先修改第 0 行对应的标记（蓝色）
				matrix[0][col] = 0

				// 需要判断是否是第 0 行第 0 个元素，如果是，需要用到前面定义的变量
				// 如果不是，就修改对应位置的标记
				if row > 0 {
					matrix[row][0] = 0
				} else {
					zeroRow = 0
				}
			}
		}
	}
	// 2. 接着，根据前面做的标记，修改除了第 0 行和第 0 列以外的所有的元素
	for row := 1; row < m; row++ {
		for col := 1; col < n; col++ {
			if matrix[0][col] == 0 || matrix[row][0] == 0 {
				matrix[row][col] = 0
			}
		}
	}
	// 3. 修改第0列对应的元素
	if matrix[0][0] == 0 {
		for row := 1; row < m; row++ {
			matrix[row][0] = 0
		}
	}

	// 4. 修改第0行 对应的元素
	if zeroRow == 0 {
		for col := 0; col < n; col++ {
			matrix[0][col] = 0
		}
	}

}

// @lc code=end
