/*
 * @lc app=leetcode.cn id=98 lang=golang
 *
 * [98] 验证二叉搜索树
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

import "math"

func isValidBST(root *TreeNode) bool {
	// 验证是否是二叉搜索树，通过中序遍历确定这个数组是否是升序的(使用两个指针，pre 和 cur)
	// 但这需求用到一个额外的数组，我们可以在遍历树的时候去比较
	// 使用 pre 存储前面的节点值，每次 pre 和当前的节点的值进行比较

	// 必须要用 int64 类型，才可能比节点值的范围小 节点值的范围是 int32
	// 还有 pre 必须要声明 int64 类型，如果只写 pre := math.MinInt64
	// golang 会将 pre 推导为 int 类型。这在 32 位系统上会导致编译时溢出错误，因此在需要保证 64 位特性的场景下，推荐明确声明为 int64。
	// math.MinInt64 属于无类型整型常量。
	var pre int64 = math.MinInt64
	return help(root, &pre)

}

// 递归函数用来中序遍历，然后在遍历的过程中加入比较
// 必须传`*int`指针，才能做到多层递归修改同一个变量
// 如果不想传指针，就闭包写在一个函数里
func help(root *TreeNode, pre *int64) bool {
	if root == nil {
		return true
	}

	// 先遍历左子树
	if !help(root.Left, pre) {
		return false
	}
	if *pre >= int64(root.Val) {
		return false
	}
	// pre 更新为当前 root 节点的值
	*pre = int64(root.Val)
	if !help(root.Right, pre) {
		return false
	}

	return true
}

// @lc code=end
