/*
 * @lc app=leetcode.cn id=200 lang=golang
 *
 * [200] 岛屿数量
 */
package main

// @lc code=start
func numIslands(grid [][]byte) int {
	// 使用 bfs 进行广度优先搜索（上下左右）值为 1 的每个坐标的上下左右是否为 1，并且有没有被访问过
	// bfs 用到队列，队列存储每个为 1 的且没被访问过的坐标
	// 因此得有个变量visit 存储坐标是否被访问过

	// 定义结果变量
	nums := 0
	rows := len(grid)
	if rows == 0 {
		return nums
	}
	cols := len(grid[0])

	// 初始化 visit, 二维 bool 数组
	visit := make([][]bool, rows)
	for i := range visit {
		visit[i] = make([]bool, cols)
	}

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			//  0 跳过,已经访问过的 1跳过
			if grid[row][col] == '1' && !visit[row][col] {
				bfs(grid, row, col, visit)
				nums++
			}
		}
	}

	return nums
}

// bfs （队列+迭代）去遍历值为 1的坐标上下左右为 1 的，没被访问过的加入队列
func bfs(grid [][]byte, row, col int, visit [][]bool) {
	type pair struct {
		r, c int
	}
	// 当前坐标入队
	queue := []pair{{row, col}}
	// 当前坐标标记为已访问
	visit[row][col] = true
	// 四个方位的
	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	for len(queue) > 0 {
		// 访问并弹出队列头部元素
		front := queue[0]
		queue = queue[1:]

		for _, dir := range dirs {
			tmpRow := front.r + dir[0]
			tmpCol := front.c + dir[1]
			if tmpRow >= 0 && tmpRow < len(grid) &&
				tmpCol >= 0 && tmpCol < len(grid[0]) &&
				grid[tmpRow][tmpCol] == '1' && !visit[tmpRow][tmpCol] {
				queue = append(queue, pair{tmpRow, tmpCol})
				visit[tmpRow][tmpCol] = true
			}
		}
	}
}

// @lc code=end
