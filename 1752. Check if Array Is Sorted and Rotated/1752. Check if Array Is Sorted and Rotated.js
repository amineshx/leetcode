/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
    n = nums.length
    window_length = 1
    for (let i=1; i<2*n; i++){
        if (nums[(i-1)%n]<= nums[i%n]){
            window_length++
        }else{
            window_length=1
        }
        
        if (n===window_length){
            return true
        }
    }
    return n==1
};

console.log(check(nums = [3,4,5,1,2]))
console.log(check(nums = [2,1,3,4]))
console.log(check(nums = [1,2,3]))