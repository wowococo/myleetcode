/*
 * @lc app=leetcode.cn id=101 lang=golang
 *
 * [101] 对称二叉树
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

func isSymmetric(root *TreeNode) bool {
	// 循环判断每一层是否是对称的，如何判断每一层是对称的，
	// 使用两个队列，左子树从左向右存储节点，右子树从右向左存储节点
	// 取出两个队列的元素，挨个判断是否相等
	// 有点麻烦，不如直接合并成一个队列，
	// 队列中的元素是左右子树对应节点的节点对
	if root == nil {
		return true
	}

	queue := make([][]*TreeNode, 0)
	queue = append(queue, []*TreeNode{root.Left, root.Right})
	for len(queue) > 0 {
		// 取并弹出队列的第一个元素
		front := queue[0]
		queue = queue[1:]
		left, right := front[0], front[1]
		if left == nil && right == nil {
			continue
		}
		if left == nil || right == nil {
			return false
		}
		if left.Val != right.Val {
			return false
		}

		// 将left.left 和 right.right 入队
		queue = append(queue, []*TreeNode{left.Left, right.Right})
		// 将 left.right 和 right.left 入队
		queue = append(queue, []*TreeNode{left.Right, right.Left})
	}

	// 都遍历完了，有问题的话，上面循环里就直接返回 false 了
	return true
}

// @lc code=end
