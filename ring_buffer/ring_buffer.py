class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        # * IF LESS STORAGE IS LESS THAN, APPEND USING LIST METHOD
        if len(self.storage) != self.capacity:
            self.storage.append(item)
        else:
            # * ELSE MAKE FIRST INDEX AVAILABLE FOR ITEM
            self.storage[self.current] = item
            
            # * SHIFT INDEX AND RESET
            if self.current < self.capacity - 1:
                self.current += 1
            else: 
                self.current = 0

    def get(self):
        return self.storage
