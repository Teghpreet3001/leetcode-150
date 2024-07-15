class TimeMap(object):

    def __init__(self):
        self.map = defaultdict(list) 

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.map[key].append([value, timestamp])

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        data = self.map.get(key, [])
        # Binary Search on the timestamps
        low = 0
        high = len(data) - 1
        result = ""
        while low <= high:
            mid = low + (high - low) // 2
            timestamp_prev = data[mid][1]
            if timestamp_prev <= timestamp:
                result = data[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return result
 
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)