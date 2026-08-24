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
	// 这是一道数学题，结论是：
	// 当相遇后，快指针重新到 head 位置，走同样的距离就到入环点了
	// 要考虑到假设只有一个节点的边界情况
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next

		// 相遇之后 fast 到 head 位置，fast 和 slow 再重新走相同的距离
		if fast == slow {
			fast = head
			// 进入循环前有可能已经到达入口了，所以不能用 fast != nil 判断
			for fast != slow {
				fast = fast.Next
				slow = slow.Next
			}
			return fast
		}
	}

	return nil
}

// @lc code=end
