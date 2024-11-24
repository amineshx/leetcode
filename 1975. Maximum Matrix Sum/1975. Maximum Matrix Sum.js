/**
 * @param {number[][]} matrix
 * @return {number}
 */
var maxMatrixSum = function(matrix) {
    let totalSum = 0
    let min_abs = Infinity
    let negative_nums = 0
    for (row of matrix){
        for (val of row){
            totalSum += Math.abs(val)
            min_abs=Math.min(min_abs,Math.abs(val))
            if (val<0){
                negative_nums++
            }
        }
    }
    if (negative_nums%2===1){
        totalSum-=2*min_abs
    }
    return totalSum
};

console.log(maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]))