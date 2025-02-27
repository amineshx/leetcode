/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    let arr_to_set = new Set(arr)  
    let res=0

    for (let i=0; i<arr.length-1;i++){
        for (let j=i+1; j<arr.length;j++){
            let prev = arr[i]
            let cur = arr[j]
            let next = prev+cur 
            let length = 2
            while (arr_to_set.has(next)){
                length++
                prev = cur 
                cur = next
                next = prev+cur
                res = Math.max(res,length)
            }
        }
    }
    return res
};

console.log(lenLongestFibSubseq(arr = [1,2,3,4,5,6,7,8]))
console.log(lenLongestFibSubseq(arr = [1,3,7,11,12,14,18]))