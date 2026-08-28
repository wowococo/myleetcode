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
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

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
// 迭代写法（必考），使用栈来模拟，中序遍历是左根右
func inorderTraversalIter(root *TreeNode) []int {
	res := make([]int, 0)
	// 定义栈，使用切片
	stack := make([]*TreeNode, 0)
	cur := root
	for cur != nil || len(stack) > 0 {
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}
		// 直至cur 为 nil，取出此时栈顶元素，此时栈顶节点的左子树为 nil，
		// 栈顶算是当前这个节点的根节点
		top := stack[len(stack)-1]
		res = append(res, top.Val)
		stack = stack[:len(stack)-1]
		// 然后访问这个节点的右子树
		cur = top.Right
		// 以右子树为根节点继续下一轮 for 循环
	}
	return res
}
