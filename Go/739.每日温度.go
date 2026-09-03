/*
 * @lc app=leetcode.cn id=739 lang=golang
 *
 * [739] 每日温度
 */
package main

// @lc code=start
func dailyTemperatures(temperatures []int) []int {
	// 单调栈：栈里面的元素始终保存单调递减的顺序
	// 将数组的下标入栈，比将数组元素入栈更方便，因为结果数组会用到下标
	// 遍历数组，将 nums[i]和栈顶元素进行比较，如果比栈顶元素大，可以得出
	// res[index] = i-index, res[index]得到了，栈顶元素没用了，要弹出来，
	// 继续比较nums[i]和下一个栈顶元素，如果不比栈顶元素大，暂时也得不出来 res[index]
	// 的值，就将 nums[i]入栈
	res := make([]int, len(temperatures))
	stack := make([]int, 0)
	for i := 0; i < len(temperatures); i++ {
		// temperatures[i] 可以和多个栈顶元素比
		for len(stack) > 0 && temperatures[i] > temperatures[stack[len(stack)-1]] {
			index := stack[len(stack)-1]
			// 更新 res
			res[index] = i - index
			// 弹出栈顶元素
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, i)

	}

	return res
}

// @lc code=end
