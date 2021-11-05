package main

import "testing"

func TestLongestPalindrome(t *testing.T) {
	cases := []struct {
		Name, A, Expected string
	}{
		{"one", "babad", "bab"},
		{"two", "cbbd", "bb"},
		{"three", "a", "a"},
		{"four", "ac", "a"},
	}

	for _, c := range cases {
		t.Run(c.Name, func(t *testing.T) {
			if ans := longestPalindrome(c.A); ans != c.Expected {
				t.Errorf("expected %s, but got %s", c.Expected, ans)
			}
		})
	}
}
