// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    let queueP = [p]
    let queueQ = [q]

    while (queueP.length && queueQ.length) {
        let nodeP = queueP.shift()
        let nodeQ = queueQ.shift()

        if (!nodeP && !nodeQ) continue
        if (!nodeP || !nodeQ || nodeP.val !== nodeQ.val) return false

        queueP.push(nodeP.left)
        queueQ.push(nodeQ.left)
        queueP.push(nodeP.right)
        queueQ.push(nodeQ.right)
    }

    return queueP.length === 0 && queueQ.length === 0
};

function buildTree(values) {
    if (!values.length) return null;

    let root = new TreeNode(values[0]);
    let queue = [root];
    let i = 1;

    while (i < values.length) {
        let node = queue.shift();
        if (values[i] !== null) {
            node.left = new TreeNode(values[i]);
            queue.push(node.left);
        }
        i++;

        if (i < values.length && values[i] !== null) {
            node.right = new TreeNode(values[i]);
            queue.push(node.right);
        }
        i++;
    }

    return root;
}

// Test Cases
let p1 = buildTree([1, 2, 3]);
let q1 = buildTree([1, 2, 3]);
console.log(isSameTree(p1, q1));  // true

let p2 = buildTree([1, 2]);
let q2 = buildTree([1, null, 2]);
console.log(isSameTree(p2, q2));  // false

let p3 = buildTree([1, 2, 1]);
let q3 = buildTree([1, 1, 2]);
console.log(isSameTree(p3, q3));  // false
