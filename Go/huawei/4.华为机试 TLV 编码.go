package main

import (
	"fmt"
	"strconv"
)

func parseTLV(s string) int {
	n := len(s)
	i := 0
	tagCount := 0

	for i < n {
		// 1. 至少需要包含 Tag(1位) + Length(1位)
		if i+2 > n {
			return 0
		}

		// 2. 读取第 2 位作为 Length（假设 '1'~'9' 对应长度 1~9）
		length := int(s[i+1] - '0')
		if length <= 0 {
			return 0 // 长度非法
		}

		// 3. 检查剩余字符是否够放 Value 部分
		if i+2+length > n {
			return 0
		}

		// 4. 提取 Value 并校验其数值范围是否在 1-99 之间
		valStr := s[i+2 : i+2+length]
		valNum, err := strconv.Atoi(valStr)
		if err != nil || valNum < 1 || valNum > 99 {
			return 0 // Value 的值不在 1-99 范围内，返回 0
		}

		// 5. 计算基础长度：Tag(1) + Length(1) + Value(length)
		baseLen := 1 + 1 + length

		// 6. 向上对齐到 4 的倍数
		groupLen := (baseLen + 3) / 4 * 4

		// 7. 检查补齐后的整组长度是否超出了字符串边界
		if i+groupLen > n {
			return 0
		}

		tagCount++
		i += groupLen // 跳到下一组
	}

	return tagCount
}

func main() {
	// 示例：Tag='2', Len='2'(表示后面Value占2位), Value="30"(值为30，在1-99之间)
	// baseLen = 1 + 1 + 2 = 4 (刚好是4的倍数，无需Padding)
	fmt.Println(parseTLV("22303230")) // 输出: 2
}
