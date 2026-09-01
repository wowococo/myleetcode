/*
 * @lc app=leetcode.cn id=994 lang=golang
 *
 * [994] 腐烂的橘子
 */
package main

// @lc code=start
type pair struct {
	r, c int
}

func orangesRotting(grid [][]int) int {
	// 也是采用 bfs（一层一层遍历，队列+迭代）
	// 首先需要统计出新鲜橘子和初始腐烂橘子的个数，
	// 如果最后把腐烂橘子周围全都腐烂完，还有新鲜橘子，就返回-1

	// 首先初始化
	time := 0
	fresh := 0
	queue := make([]pair, 0)

	rows := len(grid)
	if rows == 0 {
		return time
	}
	cols := len(grid[0])

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if grid[row][col] == 1 {
				fresh++
			} else if grid[row][col] == 2 {
				queue = append(queue, pair{row, col})
			}
		}
	}

	dirs := [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	// 当队列不为空并且新鲜橘子个数大于 0 的时候,
	// 队列里存的都是坏橘子，弹出队列头部，将队列的四个方位的新鲜橘子都变坏，并入队
	for len(queue) > 0 && fresh > 0 {
		qsize := len(queue)

		for i := 0; i < qsize; i++ {
			front := queue[0]
			queue = queue[1:]
			for _, dir := range dirs {
				tmpRow := front.r + dir[0]
				tmpCol := front.c + dir[1]

				// 如果越界或者不是新鲜橘子就跳过
				if tmpRow < 0 || tmpRow >= len(grid) || tmpCol < 0 || tmpCol >= len(grid[0]) || grid[tmpRow][tmpCol] != 1 {
					continue
				}

				// 将新鲜橘子变成坏橘子
				grid[tmpRow][tmpCol] = 2
				queue = append(queue, pair{tmpRow, tmpCol})
				//  新鲜数量--
				fresh--
			}
		}
		time++

	}

	if fresh > 0 {
		return -1
	} else {
		return time
	}

}

// @lc code=end
