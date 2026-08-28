/*
 * @lc app=leetcode.cn id=104 lang=golang
 *
 * [104] 二叉树的最大深度
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

// 递归写法
func maxDepthRecur(root *TreeNode) int {
	// 递归终止条件，节点为 null 的时候
	if root == nil {
		return 0
	}
	return max(maxDepthRecur(root.Left), maxDepthRecur(root.Right)) + 1
}

// dfs 写法
// 栈的每个元素存节点和当前深度
type nodeDepth struct {
	node  *TreeNode
	depth int
}

// 有三种实现方法，递归，dfs，bfs
func maxDepthDFS(root *TreeNode) int {
	// dfs, 也是需要这个边界条件，实现深度优先搜索需要用到栈
	if root == nil {
		return 0
	}
	depth := 0
	stack := make([]*nodeDepth, 0)
	stack = append(stack, &nodeDepth{node: root, depth: 1})
	for len(stack) > 0 {
		// 栈不为空的时候，弹出栈顶元素
		top := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		curDepth := top.depth
		depth = max(depth, curDepth)

		// 如果右子树不为空，将右子树加入栈，栈后进先出，想要先左遍历，就先压右子树
		// 想要先右遍历，就压左子树
		if top.node.Right != nil {
			stack = append(stack, &nodeDepth{node: top.node.Right, depth: curDepth + 1})
		}
		// 然后如果左子树不为空，将左子树加入栈
		if top.node.Left != nil {
			stack = append(stack, &nodeDepth{node: top.node.Left, depth: curDepth + 1})
		}

	}

	return depth
}

// 有三种实现方法，递归，dfs，bfs
func maxDepthBFS(root *TreeNode) int {
	// bfs, 也是需要这个边界条件, 实现广度优先搜索需要用到队列
	if root == nil {
		return 0
	}

	depth := 0
	queue := make([]*nodeDepth, 0)
	queue = append(queue, &nodeDepth{node: root, depth: 1})
	// 当队列不为空的时候
	for len(queue) > 0 {
		// 取队头；弹出队列的第一个元素
		tmp := queue[0]
		queue = queue[1:]
		depth = max(depth, tmp.depth)

		if tmp.node.Left != nil {
			queue = append(queue, &nodeDepth{node: tmp.node.Left, depth: tmp.depth + 1})
		}

		if tmp.node.Right != nil {
			queue = append(queue, &nodeDepth{node: tmp.node.Right, depth: tmp.depth + 1})
		}
	}

	return depth
}

// @lc code=end
