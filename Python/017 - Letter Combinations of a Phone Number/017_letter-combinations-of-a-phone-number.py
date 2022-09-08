from leezy import solution, Solution


class Q017(Solution):
    @solution
    def letterCombinations(self, digits):
        # 32ms, 91.87%
        if digits == "":
            return []
        dial = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        total = []
        self.dfs(digits, dial, 0, '', total)
        return total

    def dfs(self, digits, dial, i, cur, total):
        # i 表示后面参数 cur 的长度
        if i == len(digits):
            total.append(cur)
            return
        for ch in dial[digits[i]]:
            self.dfs(digits, dial, i+1, cur+ch, total)


def main():
    q = Q017()
    q.add_case(q.case('23'))
    q.run()


if __name__ == '__main__':
    main()
