package main

import "fmt"

// 滑动窗口
// 看到子串问题要想到滑动窗口，滑动窗口意味着双指针[left, right],
// 并且有一个或者两个哈希表来存储滑动窗口内的数据
func lengthOfLongestSubstringTwoDistinct(s string) int {
	if len(s) <= 2 {
		return len(s)
	}

	left := 0
	// 哈希表：记录窗口内每个字符出现的次数
	memo := make(map[byte]int)
	// 记录最终的答案
	res := 0

	// right移动表示扩大窗口
	for right := 0; right < len(s); right++ {
		// 先移动右边
		rightChar := s[right]
		memo[rightChar]++

		// 当不同字符种类超过 2 个时，移动 left 收缩窗口
		for len(memo) > 2 {
			// 将左边向右移
			leftChar := s[left]
			memo[leftChar]--
			// 如果减到 0 了，那么要及时从 memo 删掉，避免影响 len(memo)的判断
			if memo[leftChar] == 0 {
				delete(memo, leftChar)
			}
			left++
		}

		res = max(res, right-left+1)
	}

	return res
}

func main() {
	fmt.Println(lengthOfLongestSubstringTwoDistinct("eceba"))   // 输出: 3 (子串 "ece")
	fmt.Println(lengthOfLongestSubstringTwoDistinct("ccaabbb")) // 输出: 5 (子串 "aabbb")
}
