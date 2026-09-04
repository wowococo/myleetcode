/*
 * @lc app=leetcode.cn id=295 lang=golang
 *
 * [295] 数据流的中位数
 */

// 大根堆存储较小的元素，小根堆存储较大的元素
// 1. 大根堆的最大值不能大于小根堆的最小值
// 2. 两个堆的元素个数不能超过 1

// 一开始往哪个堆存都行，我们这边就用往大根堆去存，
// 最后的中位数：
// 1. 如果大根堆元素多，就是大根堆的最大值
// 2. 如果小根堆元素多，就是小根堆的最小值
// 3. 如果两边元素相等，就是（大根堆的最大值+小根堆的最小值）/ 2
package main

import "container/heap"

type MedianFinder struct {
	left  *MaxHeap
	right *MinHeap
}

func Constructor() MedianFinder {
	maxH := &MaxHeap{}
	heap.Init(maxH)
	minH := &MinHeap{}
	heap.Init(minH)
	return MedianFinder{
		left:  maxH,
		right: minH,
	}
}

func (this *MedianFinder) AddNum(num int) {
	heap.Push(this.left, num)
	// 如果大根堆的最大值(堆顶) > 小根堆的最小值（堆顶），不满足条件了，
	// 将大根堆的最大值移到小根堆去
	if this.left.Len() > 0 && this.right.Len() > 0 && (*this.left)[0] > (*this.right)[0] {
		heap.Push(this.right, (*this.left)[0])
		heap.Pop(this.left)
	}

	// 平衡一下两边的堆元素的数量
	// 如果大根堆比小根堆的数量相差超过 1，将大根堆的最大值移到小根堆去
	if this.left.Len() > this.right.Len()+1 {
		heap.Push(this.right, (*this.left)[0])
		heap.Pop(this.left)
	}

	if this.right.Len() > this.left.Len()+1 {
		heap.Push(this.left, (*this.right)[0])
		heap.Pop(this.right)
	}
}

//  1. 如果大根堆元素多，就是大根堆的最大值
//
// 2. 如果小根堆元素多，就是小根堆的最小值
// 3. 如果两边元素相等，就是（大根堆的最大值+小根堆的最小值）/ 2
func (this *MedianFinder) FindMedian() float64 {
	if this.left.Len() > this.right.Len() {
		return float64((*this.left)[0])
	}
	if this.right.Len() > this.left.Len() {
		return float64((*this.right)[0])
	}

	return float64((*this.left)[0]+(*this.right)[0]) / 2

}

// 定义大根堆存储小的元素
type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MaxHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MaxHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// 定义小根堆存储大的元素
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */
// @lc code=end
