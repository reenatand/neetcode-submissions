class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.data_map = {}
    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        idx_to_remove = self.data_map[val]
        last_element = self.data_list[-1]
        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove
        self.data_list.pop()
        del self.data_map[val]

        return True 
    def getRandom(self) -> int: 
        return random.choice(self.data_list)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()