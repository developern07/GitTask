#комментарии
#Создаем граф
graph = {
    'a': ['b','c'],
    'b': ['d','e'],
    'c': ['f'],
    'd': [],
    'e': ['f'],
    'f': []
}

#Реализуем функцию обхода графа в глубину с проверкой на некорректные знавчения входных параметров
def dfs_path(graph, current_vertex, target_vertex, visited=[]):
    visited.append(current_vertex)

    if current_vertex==target_vertex: #комментарии1
        return visited

    if current_vertex not in graph:
        raise ValueError(f"Вершина {current_vertex} не найдена в графе")

    for neighbor in graph[current_vertex]: #комментарии2
        if neighbor not in visited:
            path = dfs_path(graph, neighbor, target_vertex, visited)
            if path:
                return path #комментарии3

    return None

#Вызываем функцию для проверки
try:
    a='a'
    b='e'
    path=dfs_path(graph, a, b) #комментарии4
    if path:
        print(f"Длина пути от вершины {a} до вершины {b} составляет {len(path) - 1} штрихов")
    else:
        print(f"Путь от вершины {a} до вершины {b} не найден")
except ValueError as e:
    print(str(e))