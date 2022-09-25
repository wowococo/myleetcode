/*
 * @lc app=leetcode.cn id=707 lang=golang
 *
 * [707] 设计链表
 */
package main

// @lc code=start
type MyLinkedList struct {
	Dummy *Node
	Size  int
}

type Node struct {
	Val  int
	Next *Node
}

func Constructor() MyLinkedList {
	return MyLinkedList{
		Dummy: &Node{
			Val:  0,
			Next: nil,
		},
	}
}

func (this *MyLinkedList) Get(index int) int {
	if index < 0 || index > this.Size-1 {
		return -1
	}

	cur := this.Dummy.Next
	for index > 0 {
		cur = cur.Next
		index--
	}

	return cur.Val
}

func (this *MyLinkedList) AddAtHead(val int) {
	dummy := this.Dummy
	node := &Node{Val: val}
	cur := dummy
	node.Next = cur.Next
	cur.Next = node
	this.Size++

}

func (this *MyLinkedList) AddAtTail(val int) {
	cur := this.Dummy
	node := &Node{Val: val}

	for cur.Next != nil {
		cur = cur.Next
	}

	cur.Next = node
	this.Size++
}

func (this *MyLinkedList) AddAtIndex(index int, val int) {
	if index < 0 {
		this.AddAtHead(val)
		return
	}
	if index == this.Size {
		this.AddAtTail(val)
		return
	}

	if index > this.Size {
		return
	}

	cur := this.Dummy
	node := &Node{Val: val}
	for index > 0 {
		cur = cur.Next
		index--
	}

	node.Next = cur.Next
	cur.Next = node
	this.Size++
}

func (this *MyLinkedList) DeleteAtIndex(index int) {
	if index < 0 || index > this.Size-1 {
		return
	}
	cur := this.Dummy
	for index > 0 {
		cur = cur.Next
		index--
	}
	if cur.Next != nil {
		cur.Next = cur.Next.Next
	}
	this.Size--
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */
// @lc code=end
