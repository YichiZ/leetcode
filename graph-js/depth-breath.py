def depthFirstPrint(graph, initialNode):
    stack = [initialNode]
    while len(stack) > 0:
        node = stack.pop()
        print(node)
        for neighbor in graph[node]:
            stack.append(neighbor)


def breathFirstPrint(graph, initialNode):
    queue = [initialNode]
    while len(queue) > 0:
        node = queue.pop()
        print(node)
        for neighbor in graph[node]:
            queue.insert(0, neighbor)


def depthRecursivePrint(graph, initialNode):
    print(initialNode)
    for neighbor in graph[initialNode]:
        depthFirstPrint(graph, neighbor)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

# depthFirstPrint(graph, 'a')

# depthRecursivePrint(graph, 'a')

breathFirstPrint(graph, 'a')
