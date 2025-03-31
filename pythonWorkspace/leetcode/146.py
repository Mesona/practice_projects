# https://leetcode.com/problems/lru-cache/submissions/

class LRUCache:

    def __init__(self, capacity: int):
        self.max_len = capacity
        self.cache = []
        self.quick_lookup = {}

    def get(self, key: int) -> int:
        try:
            val = self.quick_lookup[key]
            self.cache.append(self.cache.pop(self.cache.index(key)))
            return val
        except KeyError:
            val = -1
            return val

    def put(self, key: int, value: int) -> None:
        try:
            self.quick_lookup[key] = value
            self.cache.append(self.cache.pop(self.cache.index(key)))
        except:
            if self.max_len == len(self.cache):
                removed = self.cache.pop(0)
                del self.quick_lookup[removed]
                
            self.cache.append(key)
            self.quick_lookup[key] = value
        
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
