/*
 * @lc app=leetcode.cn id=24 lang=golang
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package main

func swapPairs(head *ListNode) *ListNode {
	// 交换两个结点需要知道这两个结点的前后两个结点
	dummy := &ListNode{}
	dummy.Next = head
	cur := dummy
	for cur.Next != nil && cur.Next.Next != nil {
		temp1 := cur.Next
		temp2 := cur.Next.Next.Next
		cur.Next = cur.Next.Next
		cur.Next.Next = temp1
		temp1.Next = temp2
		cur = cur.Next.Next
	}

	return dummy.Next
}

// @lc code=end
