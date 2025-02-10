/**
 * @param {string} s
 * @return {string}
 */
var clearDigits = function(s) {
    let res = []
    for(let char of s){
        if ((char>'z' || char<'a') && res){
            res.pop()
            continue
        }
        res.push(char)
    }
    return res.join('')
};

console.log(clearDigits(s="abc"))
console.log(clearDigits(s="cb34"))