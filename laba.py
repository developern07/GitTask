def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return len(path)-1
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath is not None:
                return newpath

#какие то комментарии
#еще комментарии

graph = {1: [2,3], 2: [1,4], 3: [1], 4: [2]}
start = 2
end = 4
print(dfs(graph, start, end))