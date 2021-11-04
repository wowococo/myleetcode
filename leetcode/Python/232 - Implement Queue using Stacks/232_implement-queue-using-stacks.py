
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pusher = []
        self.poper = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.pusher.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.poper) == 0:
            while self.pusher:
                self.poper.append(self.pusher.pop())
        return self.poper.pop()
        # return self.poper.pop() if self.poper else -1  # 此题没要求为空的时候如何返回


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.poper:
            return self.poper[-1]
        elif self.pusher:
            return self.pusher[0]
        # else:
        #     return -1
       
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.poper or self.pusher:
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

def main():
    myqueue = MyQueue()
    operations = ['push', 'push', 'peek', 'pop', 'empty']
    oprands = [[1], [2], [], [], []]
    for opt, opd in zip(operations, oprands):
        if hasattr(myqueue, opt):
            print(getattr(myqueue, opt).__call__(*opd))


if __name__ == '__main__':
    main()
