/*
 * @lc app=leetcode.cn id=138 lang=golang
 *
 * [138] 随机链表的复制
 */

// @lc code=start
/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Next *Node
 *     Random *Node
 * }
 */

package main

func copyRandomList(head *Node) *Node {
	// 两次遍历，第一次遍历时使用哈希表映射老节点和新节点
	// 第二次遍历补充 新节点的 next 和 random
	oldMapNew := make(map[*Node]*Node)
	// 1. 将 old 节点的全部和只有值的新节点映射起来
	cur := head
	for cur != nil {
		newNode := &Node{Val: cur.Val}
		oldMapNew[cur] = newNode
		cur = cur.Next
	}

	// 2. 重新遍历，补充新节点的 next 和 random ,确保指向的是新节点
	cur = head
	for cur != nil {
		newNode := oldMapNew[cur]
		newNode.Next = oldMapNew[cur.Next]
		newNode.Random = oldMapNew[cur.Random]
		cur = cur.Next
	}

	return oldMapNew[head]
}

// @lc code=end
