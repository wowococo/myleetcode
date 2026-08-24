/*
 * @lc app=leetcode.cn id=160 lang=golang
 *
 * [160] 相交链表
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

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// h1 先走 A 再走 B 链表，h2 先走 B 再走 A 链表
	h1 := headA
	h2 := headB
	for h1 != h2 {
		if h1 != nil {
			h1 = h1.Next
		} else {
			h1 = headB
		}

		if h2 != nil {
			h2 = h2.Next
		} else {
			h2 = headA
		}
	}

	return h1
} // @lc code=end
