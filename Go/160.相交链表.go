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

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	curA, curB := headA, headB
	var lenA, lenB int
	for curA != nil {
		lenA++
		curA = curA.Next
	}

	for curB != nil {
		lenB++
		curB = curB.Next
	}

	if lenB > lenA {
		lenA, lenB = lenB, lenA
		headA, headB = headB, headA
	}

	gap := lenA - lenB
	curA, curB = headA, headB

	for gap > 0 {
		curA = curA.Next
		gap--
	}

	for curA != nil {
		if curA == curB {
			return curA
		}
		curA = curA.Next
		curB = curB.Next
	}

	return nil

}

// @lc code=end
