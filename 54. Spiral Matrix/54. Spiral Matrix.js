/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const n = matrix.length
    const m = matrix[0].length
    let res = []
    let top =0 
    let left = 0
    let right = m -1
    let bottom = n-1 

    while (top<=bottom && left<=right){
        for (let i=left; i<=right;i++){
            res.push(matrix[top][i])
        }
        top++

        for (let i=top; i<=bottom;i++){
            res.push(matrix[i][right])
        }
        right--

        if (top<=bottom){
            for (let i=right; i>=left; i--){
                res.push(matrix[bottom][i])
            }
            bottom--
        }
        
        if (left<=right){
            for (let i=bottom; i>=top; i--){
                res.push(matrix[i][left])
            }
            left++
        }
        
    }
    return res
    
};

console.log(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))