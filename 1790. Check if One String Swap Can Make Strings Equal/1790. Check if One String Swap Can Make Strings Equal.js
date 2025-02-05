/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var areAlmostEqual = function(s1, s2) {
    let mismatches = []
    let charCount = new Map()

    for (let i = 0; i < s1.length; i++) {
        if (s1[i] !== s2[i]) mismatches.push(i)
        
        charCount.set(s1[i], (charCount.get(s1[i]) || 0) + 1)
        charCount.set(s2[i], (charCount.get(s2[i]) || 0) - 1)
    }

    for (const count of charCount.values()) {
        if (count !== 0) return false
    }

    return mismatches.length === 0 || 
           (mismatches.length === 2 && s1[mismatches[0]] === s2[mismatches[1]] && s1[mismatches[1]] === s2[mismatches[0]])
}


console.log(areAlmostEqual(s1 = "caa", s2 = "aaz"))
console.log(areAlmostEqual(s1 = "bank", s2 = "kanb"))
console.log(areAlmostEqual(s1 = "attack", s2 = "defend"))
console.log(areAlmostEqual(s1 = "kelb", s2 = "kelb"))