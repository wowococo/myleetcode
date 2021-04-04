from leezy import solution, Solution


class Q020(Solution):
    @solution
    def isValid(self, s):
        # 列表本身的右进右出， 本身就是后进先出， 就是栈的特性
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}
        for x in s:
            if x in "([{":
                stack.append(x)
            else:
                if stack and pair[x] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
        
def main():
    q = Q020()
    q.add_case(q.case('()').assert_equal(True))
    q.add_case(q.case('(}{').assert_equal(False))
    q.add_case(q.case('][').assert_equal(False))
    q.add_case(q.case('{[()]}').assert_equal(True))
    q.add_case(q.case('[').assert_equal(False))
    q.add_case(q.case('}').assert_equal(False))
    q.run()


if __name__ == '__main__':
    main()
