from leezy import solution, Solution

# dict + 双向链表实现
class Node:
    def __init__(self, k, v):
        self.key = k 
        self.val = v 
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        # key是 key, value 是 node
        self.dic = {}
        self.capacity = capacity
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1


    def put(self, key, value):
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
        node = Node(key, value)
        self.add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            _n = self.tail.prev
            del self.dic[_n.key]
            self.remove(_n)

    # 头插
    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node

        self.head.next = node
        node.prev = self.head

    # 移除某个节点
    def remove(self, node):
        p = node.prev
        n = node.next

        p.next = n 
        n.prev = p

# Your Cache object will be instantiated and called as such:
# obj = Cache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    cache = LRUCache(2)
    operations = ['put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
    oprands = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for opt, opd in zip(operations, oprands):
        if hasattr(cache, opt):
            print(getattr(cache, opt).__call__(*opd))


if __name__ == '__main__':
    main()
