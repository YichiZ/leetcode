const undirectedPath = (edges, nodeA, nodeB) => {
    const graph = buildGraph(edges);
    return hasPath(graph, nodeA, nodeB, new Set());
}

// Step 1: Convert adjacent list into unidirectional path
// Step 2: Use depth search
// Step 3: Add visited property

const hasPath = (graph, src, dst, visited) => {
    if (src === dst) return true;

    if (visited.has(src)) return false;
    visited.add(src);

    for (let neighbor of graph[src]) {
        if (hasPath(graph, neighbor, dst, visited) === true) {
            return true;
        }
    }

    return false;
}

const buildGraph = (edges) => {
    const graph = {};

    for (let edge of edges) {
        const [a, b] = edge;
        if (!(a in graph)) graph[a] = [];
        if (!(b in graph)) graph[b] = [];

        graph[a].push(b);
        graph[b].push(a);
    }

    return graph;
}

const edges = [
    ['i', 'j'],
    ['k', 'i'],
]

undirectedPath(edges, 'j', 'm')