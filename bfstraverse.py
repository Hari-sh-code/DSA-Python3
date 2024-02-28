def bfs(G, s):
    visited = []
    queue = []
    queue.append(s)
    visited.append(s)
    bfstree = []
    while queue:
        t = queue.pop(0)
        bfstree.append(t)
        for n in G[t]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    
    return bfstree

graph = {}
n = int(input("Enter the no:of vertices: "))
for i in range(n):
    neigh = []
    node = input("Enter the name nodes: ")
    neigh = input("Enter the neighbor nodes: ").split()
    graph[node] = neigh

S = input("Enter the starting node: ")
print(graph)
print("BFS Traversal")
print(bfs(graph,S))