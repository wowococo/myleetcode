/*
 * @lc app=leetcode.cn id=234 lang=golang
 *
 * [234] 回文链表
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

func isPalindrome(head *ListNode) bool {
	// 1. 将链表一分为二,通过快慢指针将链表一分为二
	slow := head
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// 此时 slow 是前半部分的最后一个节点

	// 2. 反转后半段链表
	second := reverseListFoo(slow.Next)
	//  将前半段最后一个节点的 next 指向 null，正式变为前半段
	slow.Next = nil

	// 3. 对比两个链表, list2 可能会比 list1 的长度短 1（奇数个节点场景下）
	h1 := head
	h2 := second
	for h2 != nil {
		if h1.Val != h2.Val {
			return false
		}
		h1 = h1.Next
		h2 = h2.Next
	}

	return true
}

func reverseListFoo(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	var pre *ListNode
	cur := head
	for cur != nil {
		tmp := cur.Next
		cur.Next = pre
		pre = cur
		cur = tmp
	}

	return pre
}

// @lc code=end
