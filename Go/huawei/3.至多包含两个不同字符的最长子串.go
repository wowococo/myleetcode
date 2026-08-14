package main

import (
	"fmt"
	"testing"
)

// 滑动窗口
// 看到单个子串问题可能要想到滑动窗口，滑动窗口意味着双指针[left, right],
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
		rightChar := s[right]
		memo[rightChar]++

		// 当不同字符种类超过 2 个时，移动 left 收缩窗口，将左边向右移
		for len(memo) > 2 {
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

func main3() {
	fmt.Println(lengthOfLongestSubstringTwoDistinct2("eceba"))   // 输出: 3 (子串 "ece")
	fmt.Println(lengthOfLongestSubstringTwoDistinct2("ccaabbb")) // 输出: 5 (子串 "aabbb")
}

func lengthOfLongestSubstringTwoDistinct2(s string) int {
	if len(s) <= 2 {
		return len(s)
	}

	left := 0
	memo := make(map[byte]int)
	res := 0

	// right 向右移动表示扩大窗口，left 向右移动表示缩小窗口
	for right := 0; right < len(s); right++ {
		rightChar := s[right]
		memo[rightChar]++

		for len(memo) > 2 {
			leftChar := s[left]
			memo[leftChar]--
			if memo[leftChar] == 0 {
				delete(memo, leftChar)
			}
			left++
		}

		res = max(res, right-left+1)
	}

	return res
}

func TestRun(t *testing.T) {
	cases := []struct {
		name string
		arg  string
		want int
	}{
		{"1", "eceba", 3},
		{"2", "ccaabbb", 5},
		{"空串", "", 0},
	}

	for _, tt := range cases {
		t.Run(tt.name, func(t *testing.T) {
			if got := lengthOfLongestSubstringTwoDistinct2(tt.arg); got != tt.want {
				t.Errorf("result=%d, want=%d", got, tt.want)
			}
		})
	}
}
