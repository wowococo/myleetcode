package main

func longestPalindrome(s string) string {
	// 回文子串要想到从中间开始向两边扩展
	res := ""
	for i, _ := range s {
		odd := palindrome(i, i, s)
		if len(res) < len(odd) {
			res = odd
		}
		even := palindrome(i, i+1, s)
		if len(res) < len(even) {
			res = even
		}
	}

	return res
}

func palindrome(l, r int, s string) string {
	for l >= 0 && r < len(s) && s[l] == s[r] {
		l--
		r++
	}
	return s[l+1 : r]
}
