/*
 * @lc app=leetcode.cn id=199 lang=golang
 *
 * [199] 二叉树的右视图
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

func rightSideView(root *TreeNode) []int {
	// c层序遍历，每一层从左到右，每一层的最后那一个元素就是每一层看到的节点值
	// 层序遍历用到队列
	res := make([]int, 0)
	queue := make([]*TreeNode, 0)
	// 首先第一次先将 root 入队
	queue = append(queue, root)
	// 当队列不为空时
	for len(queue) > 0 {
		// 遍历每一层
		levelSize := len(queue)
		// 维护一个变量表示最右边的节点，遍历到这一层的最后rightNode 当然就更新为最后一个节点了
		var rightNode *TreeNode
		for i := 0; i < levelSize; i++ {
			// 取出并弹出队列头部的元素
			front := queue[0]
			queue = queue[1:]
			if front != nil {
				rightNode = front
				// 将当前节点的左右节点入队
				queue = append(queue, front.Left)
				queue = append(queue, front.Right)
			}
		}
		// 当前这一层遍历完，如果 rightNode 不为null，将最右边节点的值存入结果数组
		if rightNode != nil {
			res = append(res, rightNode.Val)
		}
	}

	return res
}

// @lc code=end
