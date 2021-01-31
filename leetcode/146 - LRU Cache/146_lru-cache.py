from leezy import solution, Solution

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, k):
        self.k = k
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
            self.add(n)
            return n.val
        return -1
            
    def put(self, key, value):
        if key in self.dic:
            n = self.dic[key]
            self.remove(n)
        n = Node(key, value)
        self.add(n)
        self.dic[key] = n
        if len(self.dic) > self.k:
            _n = self.tail.prev
            self.remove(_n)
            del self.dic[_n.key]
    
    def remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def add(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    lrucache = LRUCache(2)
    operations = ['put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get']
    oprands = [[1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for opt, opd in zip(operations, oprands):
        if hasattr(lrucache, opt):
            print(getattr(lrucache, opt).__call__(*opd))


if __name__ == '__main__':
    main()
