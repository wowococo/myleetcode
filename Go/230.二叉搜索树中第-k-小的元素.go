/*
 * @lc app=leetcode.cn id=230 lang=golang
 *
 * [230] 二叉搜索树中第 K 小的元素
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

func kthSmallest(root *TreeNode, k int) int {
	// 二叉搜索树中序遍历得到的是有序数组，第k 小的元素就是 数组里索引为 k-1 的
	// 使用迭代对二叉搜索树进行中序遍历，我们可以在遍历的过程中获取第 k 个元素
	cnt := 0
	cur := root
	stack := make([]*TreeNode, 0)
	for cur != nil || len(stack) > 0 {
		// 一直向左遍历
		for cur != nil {
			stack = append(stack, cur)
			cur = cur.Left
		}

		// 直到 cur==nil 的时候，弹出栈顶元素，栈顶这个元素相当于是左节点为 nil 的根节点
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		cnt++
		if cnt == k {
			return top.Val
		}

		// 继续遍历弹出的栈顶元素的右节点
		cur = top.Right
	}

	return -1
}

// @lc code=end
