/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
class CustomQueue {
    constructor() {
        this.queue = []
        this.head = 0
    }

    enqueue(element) {
        this.queue.push(element)
    }

    dequeue() {
        if (this.isEmpty()) return null
        return this.queue[this.head++]
    }

    isEmpty() {
        return this.head >= this.queue.length
    }
}

var highestPeak = function(isWater) {
    const n = isWater.length
    const m = isWater[0].length
    const q = new CustomQueue()
    const res = Array.from({ length: n }, () => Array(m).fill(-1))

    for (let row = 0; row < n; row++) {
        for (let col = 0; col < m; col++) {
            if (isWater[row][col] === 1) {
                q.enqueue([row, col])
                res[row][col] = 0
            }
        }
    }

    const directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1]
    ]
    while (!q.isEmpty()) {
        const [row, col] = q.dequeue()
        const height = res[row][col]

        for (const [dRow, dCol] of directions) {
            const newRow = row + dRow
            const newCol = col + dCol

            if (
                newRow < 0 ||
                newRow >= n ||
                newCol < 0 ||
                newCol >= m ||
                res[newRow][newCol] !== -1
            ) {
                continue
            }

            res[newRow][newCol] = height + 1
            q.enqueue([newRow, newCol])
        }
    }

    return res
};
