/*
 * @lc app=leetcode.cn id=108 lang=golang
 *
 * [108] 将有序数组转换为二叉搜索树
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

func sortedArrayToBST(nums []int) *TreeNode {
	// 二叉搜索树是这棵树中序遍历的结果是有序数组，也就是节点的左边比它小，右边比它大
	// 平衡指的是这棵树每个节点的左右子树的高度差不能超过 1
	// 所以不能 left.left.left ，right.right.right 一直延长
	// 要想构造平衡二叉树，核心有两点：
	// 1. 尽可能保证每个节点都有左右子树
	// 2. 左右子树的节点数量尽可能相等

	// 首先以数组的中间位置当做根节点，然后分成左右两边，左右两边再各自去
	// 取中间位置当根节点，所以适合的思路是递归
	return build(nums, 0, len(nums)-1)
}

// 递归函数返回每个范围的根节点
func build(nums []int, left, right int) *TreeNode {
	if left > right {
		return nil
	}

	mid := left + (right-left)/2
	root := &TreeNode{Val: nums[mid]}
	root.Left = build(nums, left, mid-1)
	root.Right = build(nums, mid+1, right)
	return root
}

// @lc code=end
