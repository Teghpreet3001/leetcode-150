class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashmap = [[] for i in range(self.size)]
    
    def put(self, key: int, value: int) -> None:
        hashkey = key % self.size
        bucket = self.hashmap[hashkey]
        for i, pair in enumerate(bucket):
            mkey, mvalue = pair 
            if mkey == key:
                bucket[i] = (key, value)
                return
        self.hashmap[hashkey].append((key, value))

    def get(self, key: int) -> int:
        hashkey = key % self.size
        bucket = self.hashmap[hashkey]
        for mkey, mvalue in bucket:
            if mkey == key:
                return mvalue
        return -1

    def remove(self, key: int) -> None:
        hashkey = key % self.size
        bucket = self.hashmap[hashkey]
        for i, pair in enumerate(bucket):
            mkey, mvalue = pair 
            if mkey == key:
                bucket.pop(i)
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)