/*
 * @lc app=leetcode.cn id=48 lang=golang
 *
 * [48] 旋转图像
 */
package main

// @lc code=start
func rotateImage(matrix [][]int) {
	// 按照一层一层旋转，每层旋转 n-1 次，n 是矩阵的长度或宽度
	// 旋转次数=4个角 1 次 + 偏移1位 + 偏移2位 + ... + 偏移n-2位
	// 不同层矩阵大小不一样，由四个边界确定矩阵的大小，这里右边界和下边界代表最后的元素 下标，
	// 而不是最后的元素下标+1
	n := len(matrix)
	left, right := 0, n-1
	// 层数
	for left < right {
		top, bottom := left, right
		// 每层旋转n-1次,n 的大小由左右边界决定，n=right-left+1, n-1 = right-left
		for i := 0; i < right-left; i++ {
			topleft := matrix[top][left+i]
			matrix[top][left+i] = matrix[bottom-i][left]
			matrix[bottom-i][left] = matrix[bottom][right-i]
			matrix[bottom][right-i] = matrix[top+i][right]
			matrix[top+i][right] = topleft
		}

		// 继续对里面层进行旋转
		left++
		right--
	}

}

// @lc code=end
