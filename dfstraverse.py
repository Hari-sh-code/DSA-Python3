def dfs(G,s,dfstree):
    for n in G[s]:
        if n not in dfstree:
            dfstree[n]=s
            dfs(G,n,dfstree)
    return dfstree

graph={}
n=int(input("Enter the no:of nodes: "))
for i in range(n):
    neigh = []
    node = input("Enter the node name: ")
    neigh = input("Enter the neighbor node: ").split()
    graph[node]=neigh

S = input("Enter the starting node: ")
dfstree = {S:None}
print(graph)
print("DFS Tree")
print(dfs(graph,S,dfstree))