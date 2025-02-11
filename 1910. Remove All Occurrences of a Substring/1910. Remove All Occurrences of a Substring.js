/**
 * @param {string} s
 * @param {string} part
 * @return {string}
 */
var removeOccurrences = function(s, part) {
  let stack = []
  for (let char of s) {
    stack.push(char)
    if (stack.length>=part.length){
        const isPart = stack.slice(-part.length).join("")
        if(isPart===part){
            for(let _ =0 ; _<part.length;_++){
                stack.pop()
            }
        }
    }
  } 
  return stack.join("")
};