/*
 * @lc app=leetcode.cn id=226 lang=golang
 *
 * [226] 翻转二叉树
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

func invertTree(root *TreeNode) *TreeNode {
	// 使用递归，递归的两个关键点：
	// 1. 子问题和原问题的关系：左子树和右子树各自翻转之后，交换左右子树的位置
	// 2. 递归结束条件：遇到 null 节点的时候，返回
	if root == nil {
		return root
	}

	root.Left = invertTree(root.Left)
	root.Right = invertTree(root.Right)

	// 交换左右子树的位置
	tmp := root.Left
	root.Left = root.Right
	root.Right = tmp

	return root
}

// @lc code=end
