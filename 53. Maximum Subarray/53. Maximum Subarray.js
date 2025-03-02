var maxSubArray = function(nums) {
    let res = nums[0]
    let current_max = 0

    for (let num of nums){
        if (current_max < 0){
            current_max=0
        }
        current_max+=num
        res = Math.max(res,current_max)
    }

    return res
};

console.log(maxSubArray(nums = [-7,-2,-10,-17,-1,-38,0,-2,-3]))