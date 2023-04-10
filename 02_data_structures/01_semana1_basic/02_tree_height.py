# python3

import sys
import threading

class Node:
    def __init__(self,key):
        self.key = key
        self.childs = list()
    def addChild(self,child):
        self.childs.append(child)

def allocate_nodes(n, parents):
    tree = list()
    for key in range(n):
        tree.append(Node(key))
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].addChild(tree[i])
    return tree, root

def compute_height_bfs(tree,root):
    level_count = 1
    height = 0
    queue = [tree[root]]
    while len(queue) != 0:
        node = queue.pop(0)
        level_count -= 1
        queue.extend(node.childs)
        if level_count == 0:
            height +=1
            level_count = len(queue)
    return height



def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree,root = allocate_nodes(n,parents)
    height = compute_height_bfs(tree,root)
    # print(compute_height(n, parents))
    print(height)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
