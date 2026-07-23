/*
 * @lc app=leetcode.cn id=94 lang=golang
 *
 * [94] 二叉树的中序遍历
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

// 哪个序遍历是根节点在哪个位置，比如说中序遍历就是根节点在中间
// 左、中、右
// 递归做法，先定义一个内部函数
func inorderTraversal(root *TreeNode) (res []int) {
	var inorder func(root *TreeNode)
	inorder = func(root *TreeNode) {
		if root == nil {
			return
		}
		inorder(root.Left)
		res = append(res, root.Val)
		inorder(root.Right)
	}
	inorder(root)
	return res
}

// @lc code=end

// 迭代做法，通用模板颜色标记法，利用栈来实现
// 1. 新节点为白色，已访问过的节点为灰色
// 2. 当遇到白色节点时，标记为灰色，把节点的右侧、自身、左侧加入栈
// 3. 当遇到灰色节点时，则将节点的值输出。
// Go 里使用结构体来模拟 python 的元组，使用切片操作来模拟栈的 pop，stack[:len(stack)-1]来实现弹栈操作
type stackItem struct {
	color int
	node  *TreeNode
}

func inorderTraversal(root *TreeNode) []int {
	const (
		WHITE = 0
		GREY  = 1
	)

	var res []int

	stack := []stackItem{
		{color: WHITE, node: root},
	}

	for len(stack) > 0 {
		// pop操作
		topID := len(stack) - 1
		curr := stack[topID]
		stack = stack[:topID]

		if curr.node == nil {
			continue
		}

		if curr.color == WHITE {
			// 由于栈是后进先出的，为了实现“左根右“的中序遍历，入栈顺序必须反过来，即右根左
			stack = append(stack, stackItem{color: WHITE, node: curr.node.Right})
			stack = append(stack, stackItem{color: GREY, node: curr.node})
			stack = append(stack, stackItem{color: WHITE, node: curr.node.Left})
		} else {
			// GREY状态，直接记录数值
			res = append(res, curr.node.Val)
		}
	}

	return res
}
