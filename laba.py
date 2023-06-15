graph = {
    '1': ['3'],
    '2': ['4'],
    '3': [],
    '4': ['2']
}

def dfs(vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(neighbor, visited)

start_vertex = '1'
visited_vertices = set()

dfs(start_vertex, visited_vertices)