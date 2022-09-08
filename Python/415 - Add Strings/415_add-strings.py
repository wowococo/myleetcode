from leezy import solution, Solution


class Q415(Solution):
    @solution
    def addStrings(self, num1, num2):
        # 模拟加法过程
        ans = []
        num1 = [int(ch) for ch in num1]
        num2 = [int(ch) for ch in num2]
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            x = num1[i] + num2[j] + carry
            carry, v = divmod(x, 10)
            ans.append(str(v))
            i -= 1
            j -= 1
        rest = num1
        if i < 0:
            rest = num2
            i = j
        while i >= 0:
            x = rest[i] + carry
            carry, v = divmod(x, 10)
            ans.append(str(v))
            i -= 1
        if carry:
            ans.append("1")
        return "".join(reversed(ans))
        



def main():
    q = Q415()
    q.add_case(q.case('11', '123').assert_equal("134"))
    q.add_case(q.case("1", "9").assert_equal("10"))
    q.run()


if __name__ == '__main__':
    main()
