/*
 * @lc app=leetcode.cn id=19 lang=golang
 *
 * [19] 删除链表的倒数第 N 个结点
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

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// 快慢指针找到倒数第 n 个结点
	dummy := &ListNode{}
	dummy.Next = head
	fast := dummy
	slow := dummy

	n++
	for n > 0 && fast != nil {
		fast = fast.Next
		n--
	}

	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}

	slow.Next = slow.Next.Next

	return dummy.Next
}

// @lc code=end
