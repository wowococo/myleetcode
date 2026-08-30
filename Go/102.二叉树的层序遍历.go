/*
 * @lc app=leetcode.cn id=102 lang=golang
 *
 * [102] 二叉树的层序遍历
 */
package main

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
	// 层序遍历就是 bfs，bfs 算法用到队列
	res := make([][]int, 0)
	if root == nil {
		return res
	}

	queue := []*TreeNode{root}
	for len(queue) > 0 {
		// 每一层维护一个临时数组
		tmp := make([]int, 0)
		// 获取队列的长度，在这个长度范围内，逐个pop 出这一层的节点
		// 要提前获取，因为这个 for 循环内 queue 长度一直在变化
		qLen := len(queue)
		for i := 0; i < qLen; i++ {
			front := queue[0]
			queue = queue[1:] // pop front
			tmp = append(tmp, front.Val)

			if front.Left != nil {
				queue = append(queue, front.Left)
			}
			if front.Right != nil {
				queue = append(queue, front.Right)
			}
		}

		res = append(res, tmp)
	}

	return res
}

// @lc code=end
