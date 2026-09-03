/*
 * @lc app=leetcode.cn id=155 lang=golang
 *
 * [155] 最小栈
 */
package main

// @lc code=start
// 用两个栈实现最小栈，一个栈 保存正常 push 的元素，另一个栈保存栈中最小的元素
type MinStack struct {
	stack    []int
	minStack []int
}

func ConstructorMinStack() MinStack {
	return MinStack{
		stack:    make([]int, 0),
		minStack: make([]int, 0),
	}
}

// push 的时候把元素压入栈，把最小元素（当前元素和 minStack 的栈顶元素比较）压入minst
func (this *MinStack) Push(value int) {
	this.stack = append(this.stack, value)

	minVal := value
	if len(this.minStack) > 0 {
		minVal = min(minVal, this.minStack[len(this.minStack)-1])
	}
	this.minStack = append(this.minStack, minVal)
}

// pop 的时候把两个栈的元素都 pop
func (this *MinStack) Pop() {
	this.stack = this.stack[:len(this.stack)-1]
	this.minStack = this.minStack[:len(this.minStack)-1]
}

// top 获取第一个栈的栈顶元素
func (this *MinStack) Top() int {
	return this.stack[len(this.stack)-1]
}

// 获取第二个最小元素栈的栈顶元素
func (this *MinStack) GetMin() int {
	return this.minStack[len(this.minStack)-1]
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(value);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end
