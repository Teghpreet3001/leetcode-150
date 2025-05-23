from random import choice
class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.keys = []

    def insert(self, val: int) -> bool:
        if val in self.map: 
            return False
        self.map[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        lastElement = self.keys[-1]
        currIndex = self.map[val]
        self.keys[currIndex] = lastElement
        self.map[lastElement] = currIndex
        self.keys.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()