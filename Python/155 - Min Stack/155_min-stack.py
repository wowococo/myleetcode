class MinStack:
# 48ms 99.87% 
    def __init__(self):
        """
        initialize your data structure here.
        stack是正常栈，有其push,pop,top功能，辅助栈stack_min, 其栈顶元素表示栈stack 的最小值，辅助栈非严格降序
        """
        self.stack = []
        self.stack_min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.stack_min or val <= self.stack_min[-1]:  # 是 <=
            self.stack_min.append(val) 

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop()
        if val == self.stack_min[-1]:
            self.stack_min.pop()


    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return 


    def getMin(self):
        """
        :rtype: int
        """
        if self.stack_min:
            return self.stack_min[-1]
        else:
            return 



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def main():
    minstack = MinStack()
    operations = ['push', 'push', 'push', 'getMin', 'pop', 'top', 'getMin']
    oprands = [[-2], [0], [-3], [], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(minstack, opt):
            print(getattr(minstack, opt).__call__(*opd))


if __name__ == '__main__':
    main()
