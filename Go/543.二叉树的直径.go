/*
 * @lc app=leetcode.cn id=543 lang=golang
 *
 * [543] 二叉树的直径
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

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	// 将每个节点看作顶点，计算以每个顶点左右子树的高度，直径=leftHeight+rightHeight
	// 使用 dfs 进行深度遍历
	res := 0
	dfsGetHeight(root, &res)
	return res
}

func dfsGetHeight(node *TreeNode, res *int) int {
	if node == nil {
		return 0
	}

	leftHeight := dfsGetHeight(node.Left, res)
	rightHeight := dfsGetHeight(node.Right, res)

	// 更新 res
	*res = max(*res, leftHeight+rightHeight)

	// 当前节点的高度等于左右子树的高度最大值+1
	return max(leftHeight, rightHeight) + 1
}

func main() {
	a3 := &TreeNode{Val: 3, Left: nil, Right: nil}
	a4 := &TreeNode{Val: 4, Left: nil, Right: nil}
	a5 := &TreeNode{Val: 5, Left: nil, Right: nil}
	a2 := &TreeNode{Val: 2, Left: a4, Right: a5}
	a1 := &TreeNode{Val: 1, Left: a2, Right: a3}

	root := a1
	res := diameterOfBinaryTree(root)
	fmt.Println(res)
}

// @lc code=end
