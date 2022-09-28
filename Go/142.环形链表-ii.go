/*
 * @lc app=leetcode.cn id=142 lang=golang
 *
 * [142] 环形链表 II
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

func detectCycle(head *ListNode) *ListNode {
    // 快慢指针，快指针的速度是慢指针的2倍
	fast, slow := head, head
	for fast != nil && fast.Next != nil{
		fast = fast.Next.Next
		slow = slow.Next

		// 表示存在环
		if fast == slow {
			fast = head
			for slow != fast {
				fast = fast.Next
				slow = slow.Next
			}

			return fast
		}
	}

	return nil

}
// @lc code=end

