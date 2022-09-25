/*
 * @lc app=leetcode.cn id=206 lang=golang
 *
 * [206] 反转链表
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

func reverseList(head *ListNode) *ListNode {
	// 双指针
	var pre *ListNode
	pre = nil
	cur := head

	for cur != nil {
		temp := cur.Next
		cur.Next = pre
		pre = cur
		cur = temp
	}

	return pre

}

// 递归写法
func reverseListRecur(head *ListNode) *ListNode {
	return reverse(nil, head)
}

func reverse(pre, cur *ListNode) *ListNode {
	if cur == nil {
		return pre
	}
	temp := cur.Next
	cur.Next = pre
	return reverse(cur, temp)
}

// @lc code=end
