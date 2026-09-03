/*
 * @lc app=leetcode.cn id=215 lang=golang
 *
 * [215] 数组中的第K个最大元素
 */
package main

import "container/heap"

// @lc code=start
func findKthLargest(nums []int, k int) int {
	// 定义一个大小为 k 的最小堆
	h := &MinHeap{}
	heap.Init(h)

	for _, num := range nums {
		if h.Len() < k {
			heap.Push(h, num)
		} else if num > (*h)[0] {
			// 保持堆大小为 k，超出就弹出堆顶元素（最小的）
			heap.Pop(h)
			heap.Push(h, num)
		}
	}

	// 堆顶就是第 K 大的数
	return (*h)[0]
}

// 定义最小堆类型
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] } //最小堆
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// push 和 pop 必须用指针接收者，因为会修改切片长度
func (h *MinHeap) Push(val any) {
	*h = append(*h, val.(int))
}

func (h *MinHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

// @lc code=end
