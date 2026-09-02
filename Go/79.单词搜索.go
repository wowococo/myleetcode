/*
 * @lc app=leetcode.cn id=79 lang=golang
 *
 * [79] 单词搜索
 */
package main

// @lc code=start
func exist(board [][]byte, word string) bool {
	// 矩阵的问题好像都是穷举
	// 遍历每一个矩阵坐标，然后以这个坐标开始进行 dfs ，看其上下左右，
	// 满足等于 word 下一个字符的路径继续走
	rows := len(board)
	cols := len(board[0])
	// 初始化二维 visited 数组
	visit := make([][]bool, rows)
	for i := range visit {
		visit[i] = make([]bool, cols)
	}

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if dfs4WordSearch(board, word, row, col, 0, visit) {
				return true
			}
		}
	}

	return false
}

// 辅助函数 dfs
//
//	index 表示 word 的索引, visit 表示是否被访问过
func dfs4WordSearch(board [][]byte, word string, row, col int, index int, visit [][]bool) bool {
	// 递归终止条件：index=word 的长度，说明已经在矩阵中搜索到了 word
	if index == len(word) {
		return true
	}

	// 如果坐标不合法，或者当前矩阵的值不等于 word 中的字符，或者已经访问过了，返回 false
	rows := len(board)
	cols := len(board[0])
	if row < 0 || row >= rows || col < 0 || col >= cols || board[row][col] != word[index] || visit[row][col] {
		return false
	}

	// 将当前坐标标记为已访问
	visit[row][col] = true
	// 递归探索四个方向，收集“上下左右”四个方向中是否至少有一个方向能成功找到单词
	res := dfs4WordSearch(board, word, row-1, col, index+1, visit) ||
		dfs4WordSearch(board, word, row+1, col, index+1, visit) ||
		dfs4WordSearch(board, word, row, col-1, index+1, visit) ||
		dfs4WordSearch(board, word, row, col+1, index+1, visit)

	// 回溯，还原访问状态
	// 我刚才以某个位置为主线去试错，发现走不通；现在我退出来了，把占用的格子还给后面的其他路径使用
	visit[row][col] = false

	return res
}

// @lc code=end
