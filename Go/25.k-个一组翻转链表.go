/*
 * @lc app=leetcode.cn id=25 lang=golang
 *
 * [25] K 个一组翻转链表
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

func reverseKGroup(head *ListNode, k int) *ListNode {
	// 结合用到“两两交换链表中的节点”和“反转链表”这两道题的逻辑
	// 一定要画图画图，然后按照画图去写，只在脑子里容易被绕进去
	// 反转链表指针：pre, cur
	// 两两交换链表中的节点用到的指针：pre, first, second, nxt
	// 结合到一起就是：groupPre, pre, cur, groupNxt
	dummy := &ListNode{Next: head}
	groupPre := dummy
	for {
		// 1. 先确定一组的 groupPre 和 groupNxt
		cur := groupPre
		kth := k
		for kth > 0 && cur != nil {
			cur = cur.Next
			kth--
		}

		// 此时 cur 是组里的最后一个元素， groupNxt 是 cur 的下一个元素
		// 如果 cur 为 null，说明组内元素的数量小于 k
		if cur == nil {
			break
		}

		groupNxt := cur.Next

		// 2. 对组内反转链表
		pre := groupNxt
		cur = groupPre.Next
		for cur != groupNxt {
			tmp := cur.Next
			cur.Next = pre
			pre = cur
			cur = tmp
		}
		//  3. grouppre 和组内第一个元素连起来
		tmp := groupPre.Next
		groupPre.Next = pre

		// 4. 这一组完成了，开始下一组
		groupPre = tmp
	}

	return dummy.Next
}

// @lc code=end
