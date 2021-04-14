from leezy import solution, Solution
from collections import Counter

class Q692(Solution):
    @solution
    def topKFrequent(self, words, k):
        # 80ms 16.42%
        words = sorted(words)
        ans = []
        res = Counter(words).most_common(k)
        for t in res:
            ans.append(t[0])
        return ans
    
    @solution
    def topKFrequent_learn(self, words, k):
        # 84 ms 11.47%
        counter = Counter(words)
        candidates = list(counter.keys())
        candidates = sorted(candidates, key=lambda w: (-counter[w], w))
        return candidates[:k]


def main():
    q = Q692()
    q.add_case(q.case(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2).assert_equal(["i", "love"]))
    q.add_case(q.case(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4).assert_equal(["the", "is", "sunny", "day"]))
    q.run()


if __name__ == '__main__':
    main()
