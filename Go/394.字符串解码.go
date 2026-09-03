/*
 * @lc app=leetcode.cn id=394 lang=golang
 *
 * [394] 字符串解码
 */
package main

import "strconv"

// @lc code=start
func decodeString(s string) string {
	// 1.元素入栈直到遇到 ']'
	// 2. 遇到']'时就不断弹出栈顶元素直到遇到 '['：找到方括号里面的字符串
	// 3. 继续弹出数字直到栈顶元素不为数字：找到 k
	// 4. 根据 k 和括号里字符串拼接解码后的字符串，压入栈
	// 5. 继续遍历字符串，直至遍历完
	// 6. 最后的栈里存的是最后解码后的字符串

	// 栈里存储字符串
	stack := make([]string, 0)
	for i := 0; i < len(s); i++ {
		// byte 类型，单引号
		if s[i] != ']' {
			// 转成字符串压入栈
			tmp := string(s[i])
			stack = append(stack, tmp)

		} else {
			// 否则
			// 遇到 ']'了，开始弹出字符串,直到遇到 '['
			var tmp string
			// 字符串，双引号
			for stack[len(stack)-1] != "[" {
				tmp = stack[len(stack)-1] + tmp
				stack = stack[:len(stack)-1]
			}

			//  弹出 "["
			stack = stack[:len(stack)-1]

			// 继续弹出数字
			var num string
			for len(stack) > 0 && isDigit(stack[len(stack)-1][0]) {
				num = stack[len(stack)-1] + num
				stack = stack[:len(stack)-1]
			}

			// 将数字字符串转换为数字
			cnt, _ := strconv.Atoi(num)
			// 拼接字符串
			var str string
			for cnt > 0 {
				str = tmp + str
				cnt--
			}

			// 将拼后的字符串压入栈
			stack = append(stack, str)
		}
	}

	var res string
	for len(stack) > 0 {
		res = stack[len(stack)-1] + res
		stack = stack[:len(stack)-1]
	}

	return res
}

func isDigit(b byte) bool {
	if b >= '0' && b <= '9' {
		return true
	}
	return false
}

// @lc code=end
