/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
class CustomDeque{
    constructor(){
        this.items = []
    }
    append(element) {
        this.items.push(element)
    }
    popleft() {
        if (this.isEmpty()) {
          return "Deque is empty"
        }
        return this.items.shift()
    }
    isEmpty() {
        return this.items.length === 0
    }
    
}
var highestPeak = function(isWater) {
    const n = isWater.length
    const m = isWater[0].length
    const q = new CustomDeque()
    const res = Array.from({ length: n }, () => Array(m).fill(-1))

    for (let row=0; row<n; row++){
        for (let col=0; col<m; col++){
            if (isWater[row][col]===1){
                q.append([row,col])
                res[row][col]=0
            }
        }
    }

    while (!q.isEmpty()){
        const [row,col] = q.popleft()
        const height = res[row][col]
        const neighbores = [[row+1,col],[row,col+1],[row-1,col],[row,col-1]]
        for (const [rowNei, colNei] of neighbores) {
            if (rowNei<0 || rowNei ===n || colNei<0 || colNei===m || res[rowNei][colNei]!=-1){
                continue
            }
            q.append([rowNei,colNei])
            res[rowNei][colNei]=height+1
        }
        
    }
    return res

};
console.log(highestPeak(isWater = [[0,1],[0,0]]))
