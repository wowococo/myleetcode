/*
 * @lc app=leetcode.cn id=124 lang=golang
 *
 * [124] 二叉树中的最大路径和
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

func maxPathSum(root *TreeNode) int {
	// 递归求每个节点作为根节点的最大路径和
	// 并且还要求每个节点不作为根节点能给它上面的父节点提供的最大路径和
	if root == nil {
		return 0
	}

	// 不能初始化为 0，万一都是负数，可以初始化为root.Val 或者 math.MinInt32
	res := root.Val

	// 函数 node 表示当前这个节点作为根节点
	// res 是最大路径和
	// 返回不以当前为根节点能给它上面的父节点提供的最大路径和

	var dfs func(node *TreeNode) int
	dfs = func(node *TreeNode) int {
		if node == nil {
			return 0
		}

		// 给 node 提供的最大路径和,如果左边为负，就用 0，相当于不用左子树，如果两边都为负
		// 相当于只用自己节点的值
		lmax := max(0, dfs(node.Left))
		rmax := max(0, dfs(node.Right))
		//    当前节点为根节点的最大路径和为
		curpathSum := lmax + rmax + node.Val
		// 更新 最大路径和
		res = max(res, curpathSum)
		//返回不以当前为根节点能给它上面的父节点提供的最大路径和
		// 不能两边都走，否则会重复走当前的 node
		return node.Val + max(lmax, rmax)

	}

	// 递归的过程在不断更新 res，如果函数要传递 res，必须使用指针
	dfs(root)
	return res

}

// @lc code=end
