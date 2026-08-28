/*
 * @lc app=leetcode.cn id=146 lang=golang
 *
 * [146] LRU 缓存
 */
package main

// @lc code=start
// 使用双向链表+哈希表可以实现 get+set  时间复杂度都是 O（1）

type DNode struct {
	Key  int
	Val  int
	Pre  *DNode
	Next *DNode
}

type LRUCache struct {
	Capacity   int
	Head, Tail *DNode
	Memo       map[int]*DNode
}

func Constructor(capacity int) LRUCache {
	// 定义两个虚拟节点 head 和 tail
	head := &DNode{}
	tail := &DNode{}
	head.Next = tail
	tail.Pre = head
	return LRUCache{
		Capacity: capacity,
		Head:     head,
		Tail:     tail,
		Memo:     make(map[int]*DNode),
	}
}

// get 操作判断 key 是否在 map 里，如果在，将节点移动到头部，返回值
// 不在则直接返回-1
func (this *LRUCache) Get(key int) int {
	if node, ok := this.Memo[key]; ok {
		this.remove(node)
		this.headInsert(node)
		return node.Val
	}

	return -1
}

// put 操作判断 key 是否在 map 里，
// 如果在，更新 value，移到前面（删除当前节点，新插入节点），
// 如果不在，就新建节点，移到前面
func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.Memo[key]; ok {
		this.remove(node)
		delete(this.Memo, key)
	}
	newNode := &DNode{Key: key, Val: value}
	this.headInsert(newNode)
	this.Memo[key] = newNode

	if len(this.Memo) > this.Capacity {
		todel := this.Tail.Pre
		this.remove(todel)
		delete(this.Memo, todel.Key)
	}
}

func (this *LRUCache) remove(node *DNode) {
	pre := node.Pre
	nxt := node.Next
	pre.Next = nxt
	nxt.Pre = pre
}

func (this *LRUCache) headInsert(node *DNode) {
	head := this.Head
	nxt := head.Next

	head.Next = node
	node.Pre = head
	node.Next = nxt
	nxt.Pre = node
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
// @lc code=end
