const minimumIsland = (grid) => {
    const visited = new Set();

    const minSize = Infinity;
    for (let r = 0; r < grid.length; r += 1) {
        for (let c = 0; r < grid[0].length; c += 1) {
            const size = exploreSize(grid, r, c, visited);
            if (size > 0 && size < minSize) {
                minSize = size;
            }
        }
    }
}

const exploreSize = (grid, r, c, visited) => {
    const rowInbounds = 0 <= r && r < grid.length;
    const columnInbounds = 0 <= c && c < grid[0].length;
    if (!rowInbounds || !columnInbounds) return 0;

    if (grid[r][c] === 'W') return 0;

    const pos = r + ',' + c;
    if (visited.has(pos)) return 0;

    let size = 1
    size += exploreSize(grid, r - 1, c, visited);
    size += exploreSize(grid, r + 1, c, visited);
    size += exploreSize(grid, r, c - 1, visited);
    size += exploreSize(grid, r, c + 1, visited);
    return size;
}