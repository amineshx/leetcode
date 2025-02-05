/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const getFrequencyMap = (str) => {
    const map = new Map();
    for (const char of str) {
        map.set(char, (map.get(char) || 0) + 1)
    }
    return map;
}
var areAlmostEqual = function(s1, s2) {
    const n = s1.length
    let count_diff = 0
    const map1 =getFrequencyMap(s1)
    const map2 =getFrequencyMap(s2)
    for (const [char, count] of map1) {
        if (map2.get(char) !== count) return false
    }
    for (let i = 0; i<n; i++){
        if (s1[i]!=s2[i]){
            count_diff++
        }
    }
    if (count_diff>2) return false
    return true
};


console.log(areAlmostEqual(s1 = "caa", s2 = "aaz"))