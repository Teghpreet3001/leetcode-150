class Node:

    #doubly linked list
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.prev = None 
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.map = {} #maps keys to the nodes
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node): 

        #add to back of linked list
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    def removeNode(self, node): 

        #removing the node by breaking link
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:

        #if key not found return -1
        if key not in self.map:
            return -1

        #extract the value from the key node
        node = self.map[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        #if key present, remove node and delete key
        if key in self.map:
            old_node = self.map[key]
            del self.map[key]
            self.removeNode(old_node)
        
        #if map reaches capacity, remove from front
        if len(self.map) >= self.capacity:
            removed_node = self.head.next
            self.removeNode(removed_node)
            del self.map[removed_node.key]

        node = Node(key, value)
        self.addNode(node)
        self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)