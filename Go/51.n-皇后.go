/*
 * @lc app=leetcode.cn id=51 lang=golang
 *
 * [51] N 皇后
 */
package main

// @lc code=start
func solveNQueens(n int) [][]string {
	// 每一行遍历去枚举+如何判断在列、正对角线、反对角线已经有棋子了
	// col_set 列集合，如果前面列已经出现了，mp 里会存这个 {col}值
	// 正对角线add_set row+col 坐标值加起来都是相等的，如果前面正对角线已经出现了，mp 里会存这个 {row+col}值
	// 反对角线sub_set row-col 坐标值加起来都是相等的，如果前面反对角线已经出现了，mp 里会存这个 {row-col}值
	var res [][]string
	board := make([]string, n)
	for i := range board {
		row := make([]byte, n)
		for j := range row {
			row[j] = '.'
		}

		board[i] = string(row)
	}

	colSet := make(map[int]bool)
	addSet := make(map[int]bool)
	subSet := make(map[int]bool)

	dfs4NQueens(n, 0, colSet, addSet, subSet, &res, board)
	return res
}

// row 表示当前行，res 结果数组，board 表示棋盘
func dfs4NQueens(n int, row int, colSet, addSet, subSet map[int]bool, res *[][]string, board []string) {
	// 如果当前的行和棋盘的大小相等，说明这n 个行中所有的棋子都有合法的位置，就把当前的
	// 方案保存到结果中，然后回溯到上一行重新做选择，继续找下一个满足条件的方案
	if row == n {
		cp := make([]string, n)
		copy(cp, board)
		*res = append(*res, cp)
		return
	}

	// 当前 row，从 0 个位置开始选
	for col := 0; col < n; col++ {
		// 当前位置所在列、正对角线、反对角线有没有其他的棋子
		// 如果有，就跳过这个位置，选择下一列
		if colSet[col] || addSet[row+col] || subSet[row-col] {
			continue
		}

		// 修改棋盘
		rowBytes := []byte(board[row])
		rowBytes[col] = 'Q'
		board[row] = string(rowBytes)

		// 如果没有，就保存当前的坐标
		colSet[col] = true
		addSet[row+col] = true
		subSet[row-col] = true

		dfs4NQueens(n, row+1, colSet, addSet, subSet, res, board)

		// 选择完之后，无论是否找到满足条件的方案，都需要把当前的状态撤销掉，棋盘也需要恢复
		delete(colSet, col)
		delete(addSet, row+col)
		delete(subSet, row-col)

		rowBytes = []byte(board[row])
		rowBytes[col] = '.'
		board[row] = string(rowBytes)

	}
}

// @lc code=end
