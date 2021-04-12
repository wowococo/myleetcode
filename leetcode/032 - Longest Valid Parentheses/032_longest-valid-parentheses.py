from leezy import solution, Solution


class Q032(Solution):
    @solution
    def longestValidParentheses(self, s):
        farest = -1
        ans = 0
        stack = []
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    ans = max(ans, i-(stack[-1] if stack else farest))
                else:
                    farest = i

        return ans


def main():
    q = Q032()
    q.add_case(q.case('(()').assert_equal(2))
    q.add_case(q.case(")()())").assert_equal(4))
    q.add_case(q.case(')').assert_equal(0))
    q.add_case(q.case('()').assert_equal(2))
    q.run()


if __name__ == '__main__':
    main()
