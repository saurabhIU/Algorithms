class LRUCache:

    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.current_size = 0
        self.cache = {}
        self.cache_list = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        # Write your code here.
        if key in self.cache:
            self.updateKey(key, value)
        else:
            if self.current_size == self.maxSize:
                self.removeTail()
            else:
                self.current_size += 1
            self.cache[key] = self.cache_list.setHead(LinkedListNode(key, value))

    def removeTail(self):
        keyToRemove = self.cache_list.tail.key
        self.cache_list.removeTail()
        self.cache.pop(keyToRemove)

    def updateKey(self, key, value):
        node = self.cache.get(key)
        node.value = value
        self.cache_list.setHead(node)


    def getValueFromKey(self, key):
        # Write your code here.
        if key not in self.cache:
            return None
        else:
            self.cache_list.setHead(self.cache.get(key))
            return self.cache.get(key).value


    def getMostRecentKey(self):
        # Write your code here.
        return self.cache_list.head.key


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def removeTail(self):
        self.tail.previous.next = None
        tail_key = self.tail.key
        self.tail = self.tail.previous
        return tail_key

    def setHead(self, node):
        if node == self.head:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
            return self.head
        elif self.head == self.tail:
            self.head.previous = node
            self.head = node
            self.head.next = self.tail
            self.tail = self.head.next
        else:
            self.shuffle_node(node)
        return self.head

    def shuffle_node(self, node):
        if node == self.tail:
            self.tail.previous.next = None
            self.tail = self.tail.previous

        elif node.next and node.previous:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.previous = None
        self.head.previous = node
        node.next = self.head
        self.head = node


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None


lru = LRUCache(4)

lru.insertKeyValuePair('a', 1)
lru.insertKeyValuePair('b', 2)
lru.insertKeyValuePair('c', 3)
lru.insertKeyValuePair('d', 4)
print(f'Most recent key is {lru.getMostRecentKey()}')
print(f'Value of key a is {lru.getValueFromKey("a")}')
lru.insertKeyValuePair('e', 5)
print(f'Value of key a is {lru.getValueFromKey("a")}')
