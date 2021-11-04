from leezy import solution, Solution
from collections import Counter
from itertools import chain


class Q347(Solution):
    @solution
    def topKFrequent(self, nums, k):
        # 44ms 68.04%
        numcnt = {}
        for num in nums:   # O(n)
            if num in numcnt:  # O(1)
                numcnt[num] += 1
            else:
                numcnt[num] = 1
        
        numcntlist = sorted(numcnt.items(), key=lambda e: e[1], reverse=True)
        res = []
        for nc in numcntlist[:k]:
            res.append(nc[0])

        return res

    @solution
    def top_k(self, nums, k):
        return [item[0] for item in Counter(nums).most_common(k)]

    @solution
    def topK(self, nums, k):
        # bucket 代表从 0 到 len(nums) freq 的 num, 时间复杂度, O(n), 空间复杂度 O(n)
        # 48ms 51.48%
        bucket = [[] for _ in range(len(nums)+1)]
        count = Counter(nums).items()
        for num, freq in count:
            bucket[freq].append(num)
        flat_list = list(chain(*bucket))
        return flat_list[::-1][:k]

        

def main():
    q = Q347()
    q.add_case(q.case([1, 1, 1, 2, 2, 3], 2))
    q.add_case(q.case([1], 1))
    q.run()


if __name__ == '__main__':
    main()
