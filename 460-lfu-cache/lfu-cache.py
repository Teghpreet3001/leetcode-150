from collections import defaultdict, OrderedDict

class Node:

    #doubly linked list
    def __init__(self, key, val):
        self.key = key 
        self.val = val
        self.freq = 1

class LFUCache:

    # The keys are the frequency counts.
    # The values are OrderedDicts that store keys based on their LRU order. This helps efficiently track both frequency and recency of keys.
    # LF: Tracks the minimum frequency of the items in the cache, helping identify which items to evict when needed.

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.map = {} #maps keys to the nodes
        self.usage = defaultdict(OrderedDict)
        self.LF = 0

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1 
        node = self.map[key]
        self.update(node, node.val)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key not in self.map:
            if len(self.map) >= self.capacity:
                rkey, rval = self.usage[self.LF].popitem(last = False)
                self.map.pop(rkey)
            node = Node(key, value)
            self.map[key] = node 
            self.usage[1][key] = value
            self.LF = 1
        else:
            node = self.map[key]
            node.val = value
            self.update(node, value)
        
    
    def update(self, node, val):
        ukey, ufreq = node.key, node.freq
        self.usage[ufreq].pop(ukey)
        if not self.usage[ufreq] and self.LF == ufreq:
            self.LF += 1
        self.usage[ufreq + 1][ukey] = val
        node.freq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)