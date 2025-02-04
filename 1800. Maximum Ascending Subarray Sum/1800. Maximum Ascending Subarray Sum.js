/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAscendingSum = function(nums) {
    
    const n = nums.length
    let max_sum = nums[0]
    let res = max_sum
    
    for (let i=1; i<n; i++){
        if (nums[i-1]<nums[i]){
            max_sum+=nums[i]
        }
        else{
            res = Math.max(res,max_sum)
            max_sum=nums[i]
        }
    }
    res = Math.max(res,max_sum)
    return res

};

console.log(maxAscendingSum(nums = [10,20,30,5,10,50]))
console.log(maxAscendingSum(nums = [10,20,30,40,50]))
console.log(maxAscendingSum(nums = [12,17,15,13,10,11,12]))