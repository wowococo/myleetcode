/*
 * @lc app=leetcode.cn id=208 lang=golang
 *
 * [208] 实现 Trie (前缀树)
 */
package main

// @lc code=start
// word 和 prefix 仅由小写英文字母组成，
// 前缀树节点，每个节点当前题可能有 26 个孩子节点，使用哈希表存储
// 还有个标识是标识当前节点是否是结尾
type TrieNode struct {
	children map[byte]*TrieNode
	isEnd    bool
}

func newTrieNode() *TrieNode {
	return &TrieNode{
		children: make(map[byte]*TrieNode),
		isEnd:    false,
	}
}

// 前缀树固定有个根节点
type Trie struct {
	root *TrieNode
}

func ConstructorTrie() Trie {
	return Trie{
		root: newTrieNode(),
	}
}

func (this *Trie) Insert(word string) {
	cur := this.root
	for i := 0; i < len(word); i++ {
		char := word[i]
		if _, ok := cur.children[char]; !ok {
			cur.children[char] = newTrieNode()
		}

		cur = cur.children[char]
	}
	cur.isEnd = true
}

func (this *Trie) Search(word string) bool {
	cur := this.root
	for i := 0; i < len(word); i++ {
		char := word[i]
		if _, ok := cur.children[char]; !ok {
			return false
		}

		cur = cur.children[char]
	}

	return cur.isEnd
}

func (this *Trie) StartsWith(prefix string) bool {
	cur := this.root
	for i := 0; i < len(prefix); i++ {
		char := prefix[i]
		if _, ok := cur.children[char]; !ok {
			return false
		}

		cur = cur.children[char]
	}

	return true
}

/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */
// @lc code=end
