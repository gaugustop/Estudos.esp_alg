class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.index = int(query[1])
        else:
            self.string = query[1]

class MyHashTable:    

    def __init__(self, num_buckets):        
        self.num_buckets = num_buckets        
        self.buckets = [ [] for _ in range(num_buckets)]
        
    def get_key(self, value):
        x, p, key = 263, 1000000007, 0
        for c in reversed(value):
            key = (key * x + ord(c)) % p
        result = key % self.num_buckets
        return result

    def add(self, value):
        key = self.get_key(value)
        if not value in self.buckets[key]:
            self.buckets[key].append(value)
    
    def delete(self, value):
        key = self.get_key(value)
        if value in self.buckets[key]:
            self.buckets[key].remove(value)

    def find(self, value):
        key = self.get_key(value)        
        return value in self.buckets[key]

    def check(self, key):        
        for value in reversed(self.buckets[key]):
            print(value, end = ' ')                            
        print()        
            

def process_queries(hash_table, queries):         
    for query in queries:             
        if query.type == 'add':                           
            hash_table.add(query.string)
        elif query.type == 'del': 
            hash_table.delete(query.string)        
        elif query.type == 'find':                               
            if hash_table.find(query.string):
                print('yes')
            else:
                print('no')     
        else:                             
            hash_table.check(query.index)                       

if __name__ == '__main__':
    m, n = int(input()), int(input())
    queries = [Query(input().split()) for _ in range(n)] 
    hash_table = MyHashTable(m)
    process_queries(hash_table, queries)
