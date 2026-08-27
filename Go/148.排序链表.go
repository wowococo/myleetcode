/*
 * @lc app=leetcode.cn id=148 lang=golang
 *
 * [148] 排序链表
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

func sortList(head *ListNode) *ListNode {
	// 对于链表这种数据结构而言，合适的是归并排序
	// 先将链表一分为二，为二，为二，为成有序的链表（也就是剩下一个节点才有序了）
	// 然后再归并，不断合并两个有序链表，合，合，合
	// 所以适合用递归做，时间复杂度：O（nlogn）,空间复杂度：递归是用栈来实现的
	// 递归的层是是 O（logn），所以空间复杂度是 O（logn）
	// 递归终止条件
	if head == nil || head.Next == nil {
		return head
	}
	// 1. 一分为二，使用快慢指针
	slow := head
	fast := head.Next
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	// 此时 slow 是前半部分的最后一个元素
	second := slow.Next
	// 将 两部分切割
	slow.Next = nil
	first := head

	// 使用递归排序前半部分
	first = sortList(first)
	second = sortList(second)

	// 2. 合并两个有序链表
	return mergeLists(first, second)
}

// 按照合并两个有序链表的思路，定义一个虚拟节点 dummy 和一个尾节点 tail
func mergeLists(left, right *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for left != nil && right != nil {
		if left.Val <= right.Val {
			tail.Next = left
			left = left.Next
		} else {
			tail.Next = right
			right = right.Next
		}
		tail = tail.Next
	}

	if left != nil {
		tail.Next = left
	} else if right != nil {
		tail.Next = right
	}

	return dummy.Next
}

// @lc code=end
