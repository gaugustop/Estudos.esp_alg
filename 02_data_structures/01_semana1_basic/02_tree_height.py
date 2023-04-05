# python3

import sys
import threading

class Node:
    def __init__(self,key):
        self.key = key
        self.childs = list()
    def addChild(self,ChildKey):
        self.childs.append(Node(ChildKey))

def allocate_nodes(n, parents):
    tree = list
    for key in range(n):
        tree.append(Node(key))
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].addChild(i)
    return tree, root

# TODO: e se não tiver -1 ???

def compute_height_bfs(tree,root):
    height = 0
    queue = [tree[root]]
    while len(queue) != 0:
        



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
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
