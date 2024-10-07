class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} #maps keys to their nodes

    def addNode(self, prevNode, freq):
        newNode = Node(freq)
        newNode.prev = prevNode
        newNode.next = prevNode.next 
        prevNode.next.prev = newNode
        prevNode.next = newNode
        return newNode
    
    def removeNode(self, node):
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.map:
            currNode = self.map[key]
            currNode.keys.remove(key)

            nextFreq = currNode.freq + 1
            nextNode = currNode.next

            if nextNode == self.tail or nextNode.freq != nextFreq:
                nextNode = self.addNode(currNode, nextFreq)
            nextNode.keys.add(key)
            self.map[key] = nextNode
            self.removeNode(currNode)
        
        else:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq != 1:
                firstNode = self.addNode(self.head, 1)
            firstNode.keys.add(key)
            self.map[key] = firstNode

    def dec(self, key: str) -> None:
        if key not in self.map:
            return 
        currNode = self.map[key]
        currNode.keys.remove(key)
        if currNode.freq  == 1:
            del self.map[key]
        else:
            prevFreq = currNode.freq - 1
            prevNode = currNode.prev
            if prevNode == self.head or prevNode.freq != prevFreq:
                prevNode = self.addNode(currNode.prev, prevFreq)
            prevNode.keys.add(key)
            self.map[key] = prevNode
        self.removeNode(currNode)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))  # Get any key from the max frequency node

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))  # Get any key from the min frequency node



# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()