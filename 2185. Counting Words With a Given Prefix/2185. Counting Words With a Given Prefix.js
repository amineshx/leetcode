/**
 * @param {string[]} words
 * @param {string} pref
 * @return {number}
 */
var prefixCount = function(words, pref) {
  let res = 0
  for(let word of words){
    if (word.startsWith(pref)){
        res++
    }
  }
  return res  
};

const sol=prefixCount(words = ["pay","attention","practice","attend"], pref = "at")
console.log(sol)
