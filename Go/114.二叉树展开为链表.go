/*
 * @lc app=leetcode.cn id=114 lang=golang
 *
 * [114] 二叉树展开为链表
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

func flatten(root *TreeNode) {
	// 使用递归的思想先展开左子树，再展开右子树
	// 然后将根节点的左子树移动到根节点的右子树的位置，
	// 再把原来的展开后右子树移到新的右子树的后面

	// 千万不要忘了递归的边界条件：
	if root == nil {
		return
	}

	flatten(root.Left)
	flatten(root.Right)
	// 先存储下展开后的右子树
	tmp := root.Right
	// 当前节点右子树指向展开后的左子树
	root.Right = root.Left
	// 当前节点左子树指向 null
	root.Left = nil
	// 遍历当前右子树，最后指向原来的展开的右子树
	cur := root
	for cur.Right != nil {
		cur = cur.Right
	}

	cur.Right = tmp
}

// @lc code=end
