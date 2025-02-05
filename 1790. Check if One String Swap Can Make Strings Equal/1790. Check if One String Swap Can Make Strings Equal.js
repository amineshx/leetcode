/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    const n = s1.length
    let count_diff = 0
    const haveSameChars = (s1,s2) =>{
        const charCount = (str) =>
            str.split("").reduce((acc, char)=>{
                acc[char]=(acc[char] || 0)+1
                return acc
            },{})
        return JSON.stringify(charCount(s1)===JSON.stringify(charCount(s2)))
    }  
    if (haveSameChars(s1,s2)) return false
    for (let i = 0; i<n; i++){
        if (s1[i]===s2[i]){
            count_diff++
        }
    }
    if (count_diff>2) return false
    return true
};