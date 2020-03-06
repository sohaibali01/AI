graph = {'A': set(['B','C', 'F']),
         'B': set(['D','C', 'A']),
         'C': set(['A','B', 'D', 'F']),
         'D': set(['B','C','F','E']),
         'E': set(['D','F']),
         'F': set(['A','C','E'])}

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:  
                stack.append((next, path + [next]))

print((list(dfs_paths(graph, 'A', 'E'))))
