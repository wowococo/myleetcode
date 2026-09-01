/*
 * @lc app=leetcode.cn id=437 lang=golang
 *
 * [437] 路径总和 III
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
package main

func pathSum(root *TreeNode, targetSum int) int {
	// 1. 找到每个顶点（可以使用 BFS 也可以使用 DFS,这里我们使用 BFS）
	// 2. 找个以顶点开始向下满足的路径条数，采用 DFS

	// bfs 遍历每个顶点,bfs 迭代写法用到队列
	if root == nil {
		return 0
	}

	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	// total 记录最后的结果
	total := 0
	for len(queue) > 0 {
		// 获取并弹出队首元素
		front := queue[0]
		queue = queue[1:]
		total += dfsPath(front, 0, targetSum)
		if front != nil {
			queue = append(queue, front.Left)
			queue = append(queue, front.Right)
		}
	}

	return total
}

// dfs 找到以某个点作为顶点开始的满足条件的路径，返回满足的路径数目
func dfsPath(node *TreeNode, curSum int64, targetSum int) int {
	// 终止条件
	if node == nil {
		return 0
	}
	// 以当前节点为顶点
	curSum += int64(node.Val)
	count := 0
	if curSum == int64(targetSum) {
		count++
	}

	count += dfsPath(node.Left, curSum, targetSum)
	count += dfsPath(node.Right, curSum, targetSum)
	return count
}

// @lc code=end
