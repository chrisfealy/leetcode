var numIslands = function (grid) {
    const visited = new Set()
    let islands = 0
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            if (grid[i][j] == 1 && !visited.has(`${i}-${j}`)) {
                bfs(i, j, grid, visited)
                islands++
            }
        }
    }
    return islands
};

const findNeighbors = (r, c, grid) => {
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    const neighbors = []
    for (const [dr, dc] of directions) {
        const row = dr + r
        const col = dc + c
        if (row >= 0 && row < grid.length && col >= 0 && col < grid[row].length)
            if (grid[row][col] == 1) neighbors.push([row, col])
    }
    return neighbors
}

const bfs = (r, c, grid, visited) => {
    if (grid[r][c] != 1) return false
    const queue = [[r, c]]
    visited.add(`${r}-${c}`)
    while (queue.length) {
        const [row, col] = queue.shift()
        const neighbors = findNeighbors(row, col, grid)
        for (const [nr, nc] of neighbors) {
            if (!visited.has(`${nr}-${nc}`)) {
                visited.add(`${nr}-${nc}`)
                queue.push([nr, nc])
            }
        }
    }
    return true
}

const grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
const grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

console.log(numIslands(grid1))
console.log(numIslands(grid2))
