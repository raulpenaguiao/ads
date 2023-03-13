class Hash_Table:
    def __init__(self, l = []):
        self.d = {}
    
    def fetch(self, key):
        return self.d[key]
    
    def has_key(self, key):
        return key in self.d
    
    def insert(self, key, item):
        self.d[key] = item
    
    def delete(self, key):
        del self.d[key]

    def keys(self):
        return list(self.d.keys())
    
