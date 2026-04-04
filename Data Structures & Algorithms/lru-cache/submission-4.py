from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key) 
        return self.cache[key]
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity: 
                self.cache.popitem(last=False)
            self.cache[key] = value 
        self.cache.move_to_end(key)

    
    def delete(self, key: int) -> bool:
        if key in self.cache:
            del self.cache[key]
            return True
        return False
    
    def last(self) -> int:
        if not self.cache:
            return -1
        key, value = self.cache.popitem(last=False) 
        self.cache[key] = value                      
        self.cache.move_to_end(key, last=False)     
        return value

        
