/*
 * @lc app=leetcode.cn id=105 lang=golang
 *
 * [105] 从前序与中序遍历序列构造二叉树
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

func buildTree(preorder []int, inorder []int) *TreeNode {
	// 根据前序遍历可以确定根节点，然后去中序遍历找到根节点的位置，
	// 然后可以确定左子树和右子树的范围，左子树和右子树各自有几个节点
	// 然后再去前序遍历中划分为左子树和右子树，继续各自左右子树这块，重复上述过程

	// 递归终止条件
	if len(preorder) == 0 || len(inorder) == 0 {
		return nil
	}

	// 前序遍历的第一个节点是根节点
	root := &TreeNode{Val: preorder[0]}
	// 在中序遍历中寻找根节点的位置
	index := 0
	for i := 0; i < len(inorder); i++ {
		if inorder[i] == preorder[0] {
			index = i
			break
		}
	}

	// 找到 根节点在中序数组中的索引后，确定左右子树各自在两个数组中的范围
	leftPreorder := preorder[1 : index+1]
	leftInorder := inorder[0:index]
	root.Left = buildTree(leftPreorder, leftInorder)

	rightInorder := inorder[index+1:]
	rightPreorder := preorder[index+1:]
	root.Right = buildTree(rightPreorder, rightInorder)

	return root
}

// 进一步节省内存和提升性能，可以使用哈希表（Map）记录中序遍历的索引，并
// 通过下标索引 (preStart, preEnd, inStart, inEnd) 进行递归。
func buildTreeBetter(preorder []int, inorder []int) *TreeNode {
	// 根据前序遍历可以确定根节点，然后去中序遍历找到根节点的位置，
	// 然后可以确定左子树和右子树的范围，左子树和右子树各自有几个节点
	// 然后再去前序遍历中划分为左子树和右子树，继续各自左右子树这块，重复上述过程
	mp := make(map[int]int, len(inorder))
	for i, val := range inorder {
		mp[val] = i
	}

	var helper func(preStart, preEnd, inStart, inEnd int) *TreeNode
	helper = func(preStart, preEnd, inStart, inEnd int) *TreeNode {
		// 递归终止条件
		if preStart > preEnd || inStart > inEnd {
			return nil
		}

		rootVal := preorder[preStart]
		root := &TreeNode{Val: rootVal}
		inIndex := mp[rootVal]

		leftLen := inIndex - inStart

		// 递归构造左右子树
		root.Left = helper(preStart+1, preStart+leftLen, inStart, inIndex-1)

		root.Right = helper(preStart+leftLen+1, preEnd, inIndex+1, inEnd)

		return root
	}

	return helper(0, len(preorder)-1, 0, len(inorder)-1)
}

// @lc code=end
