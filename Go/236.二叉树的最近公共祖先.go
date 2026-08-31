/*
 * @lc app=leetcode.cn id=236 lang=golang
 *
 * [236] 二叉树的最近公共祖先
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

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	// 使用 dfs 遍历找出 p 和 q 的路径
	// 对俩路径进行比较，最后一个相同的节点就是最近的祖先
	// dfs 递归构造 p 和 q 的路径, path 表示临时存储路径的变量，path_p 是 p的路径
	path := make([]*TreeNode, 0)
	var path_p []*TreeNode
	var path_q []*TreeNode

	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		// 如果节点为 nil 或者找到了 p 或者 q 的路径，可以返回
		if node == nil || (len(path_p) > 0 && len(path_q) > 0) {
			return
		}

		// 当前节点存入 path
		path = append(path, node)
		// 如果节点是 p，可以得到 path_p 的路径了，不能直接 path_p = path（底层指向同一个数组，path 修改 path_p 也受影响）
		// 要拷贝当前这个快照
		if node == p {
			path_p = append([]*TreeNode{}, path...)
		}
		if node == q {
			path_q = append([]*TreeNode{}, path...)
		}
		// 如果不是，继续递归 node 的左右子树
		if len(path_p) == 0 || len(path_q) == 0 {
			dfs(node.Left)
			dfs(node.Right)
		}
		// 将当前节点弹出来，后进先出
		path = path[:len(path)-1]
	}

	// 执行 DFS
	dfs(root)
	// 对比两条路径
	var res *TreeNode
	for i := 0; i < min(len(path_p), len(path_q)); i++ {
		if path_p[i] == path_q[i] {
			res = path_p[i]
		} else {
			break
		}
	}
	return res

}

// @lc code=end
