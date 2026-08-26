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
	// 四个指针，pre, first, second, nxt
	dummy := &ListNode{Next: head}
	pre := dummy
	first := head

	for first != nil && first.Next != nil {
		second := first.Next
		nxt := second.Next

		pre.Next = second
		second.Next = first
		first.Next = nxt

		pre = first
		first = nxt
	}

	return dummy.Next
}

// @lc code=end
