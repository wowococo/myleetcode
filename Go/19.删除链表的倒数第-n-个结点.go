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

// 我们可以设想假设设定了双指针 p 和 q 的话，当 q 指向末尾的 NULL，p 与 q 之间相隔的元素个数为 n 时，那么删除掉 p 的下一个指针就完成了要求。

// 设置虚拟节点 dummyHead 指向 head
// 设定双指针 p 和 q，初始都指向虚拟节点 dummyHead
// 移动 q，直到 p 与 q 之间相隔的元素个数为 n
// 同时移动 p 与 q，直到 q 指向的为 NULL
// 将 p 的下一个节点指向下下个节点

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
