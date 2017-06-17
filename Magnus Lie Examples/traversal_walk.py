graph = {'A':['B','C'],
        'B':['C', 'D'],
        'C':['D'],
        'D':['C'],
        'E':['F'],
        'F':['C']
        }


#Let's write a simple function to determine a path between two nodes.

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not graph.has_key(start):
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths



def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None


def main():
    find_path(graph, 'D', 'C')
    find_all_paths(graph, 'A', 'D')

if __name__ == '__main__':
    main()
