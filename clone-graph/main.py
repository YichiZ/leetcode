
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        graph = {}
        stack = [node]
        visited = set()

        while len(stack) > 0:
            current = stack.pop()
            if current.val in visited:
                continue
            visited.add(current.val)
            if not current.val in graph:
                graph[current.val] = []

            for neighbor in current.neighbors:

                graph[current.val].append(neighbor.val)
                stack.append(neighbor)

        nodeMap = {}
        for nodeValue in graph:
            node = None
            if nodeValue in nodeMap:
                node = nodeMap[nodeValue]
            else:
                node = Node(nodeValue)
                nodeMap[nodeValue] = node

            for neighborValue in graph[nodeValue]:
                neighborNode = None
                if neighborValue in nodeMap:
                    neighborNode = nodeMap[neighborValue]
                else:
                    neighborNode = Node(neighborValue)
                    nodeMap[neighborValue] = neighborNode

                if not node.neighbors:
                    node.neighbors = []

                if not neighborNode in node.neighbors:
                    node.neighbors.append(neighborNode)

        for key, node in nodeMap.items():
            return node


sol = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]
res = sol.cloneGraph(node1)
print()
