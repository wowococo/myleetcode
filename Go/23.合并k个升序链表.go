package main

/*
 * @lc app=leetcode.cn id=23 lang=golang
 *
 * [23] 合并K个升序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

//  迭代做法
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
// 迭代做法，将合并 k 个链表转化成多组 “合并 2 个升序链表”
// 时间复杂度：O（n * logk） n是每个链表的平均节点个数，k 是 k 个链表
func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}

	// 如果长度大于 1，也就是至少 2 个，将多个拆成 2 个，2 个，2个
	for len(lists) > 1 {
		// 临时存这次拆分后合并后的数组
		tmp := make([]*ListNode, 0)
		for i := 0; i < len(lists); i += 2 {
			list1 := lists[i]
			var list2 *ListNode
			if i+1 < len(lists) {
				list2 = lists[i+1]
			}

			tmp = append(tmp, merge2Lists(list1, list2))
		}

		// 将 tmp 新合并后的数组赋值给 lists，进行下一次两两合并
		lists = tmp
	}

	// 直至跳出循环时，更新后的lists长度等于 1，说明是合并好的结果
	return lists[0]
}

// 迭代写法实现合并 2 个升序链表，虚拟节点 dummy 加尾节点 tail
func merge2Lists(list1 *ListNode, list2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			tail.Next = list1
			list1 = list1.Next
		} else {
			tail.Next = list2
			list2 = list2.Next
		}

		// tail 始终指向链表的最后一个节点
		tail = tail.Next
	}

	if list1 != nil {
		tail.Next = list1
	} else if list2 != nil {
		tail.Next = list2
	}

	return dummy.Next
}

// 递归做法
func mergeKListsRecur(lists []*ListNode) *ListNode {
	n := len(lists)
	if n < 1 {
		return nil
	}
	if n == 1 {
		return lists[0]
	}

	num := n / 2
	left := mergeKListsRecur(lists[:num])
	right := mergeKListsRecur(lists[num:])
	return mergeTwoListRecur(left, right)
}

func mergeTwoListRecur(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}
	if list2 == nil {
		return list1
	}
	if list1.Val < list2.Val {
		list1.Next = mergeTwoListRecur(list1.Next, list2)
		return list1
	}

	list2.Next = mergeTwoListRecur(list1, list2.Next)
	return list2
}

// @lc code=end
