class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

    
def process_queries(queries):
    result = []
    hash_table = {}
    for query in queries:
        if query.type == 'add':
            hash_table[query.number] = query.name
        elif query.type == 'del':
            if query.number in hash_table:
                del hash_table[query.number]            
        else:
            if query.number in hash_table:
                response = hash_table[query.number]
            else:
                response = 'not found'            
            result.append(response)
    return result

if __name__ == '__main__':
    n = int(input())
    queries = []
    for _ in range(n):
        query = Query(input().split())
        queries.append(query)
    result = process_queries(queries)
    for response in result:
        print(response)

