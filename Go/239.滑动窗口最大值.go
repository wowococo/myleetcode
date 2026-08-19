/*
 * @lc app=leetcode.cn id=239 lang=golang
 *
 * [239] 滑动窗口最大值
 */
package main

// @lc code=start
func maxSlidingWindow(nums []int, k int) []int {
	// 头尾既可以删除数据、尾部还可以插入数据，适合的数据结构是双端队列
	n := len(nums)
	res := make([]int, 0, n-k+1)
	// 双端队列存的是元素的下标，这样可以知道有没有过期，维持单调递减
	dq := make([]int, 0, k)
	for i := 0; i < n; i++ {
		// 1. 队首超出窗口范围，出队（对应 popleft）
		if len(dq) > 0 && dq[0] <= i-k {
			dq = dq[1:]
		}

		// 2. 维持单调递减：队尾小于等于当前值就弹出（对应 pop）
		for len(dq) > 0 && nums[i] >= nums[dq[len(dq)-1]] {
			dq = dq[:len(dq)-1]
		}

		// 3. 当前下标入队列
		dq = append(dq, i)

		// 4. 要窗口成型之后，记录队首为窗口最大值
		if i >= k-1 {
			res = append(res, nums[dq[0]])
		}
	}
	return res
}

// @lc code=end
