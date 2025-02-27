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
    let queueP = [p];
    let queueQ = [q];

    while (queueP.length && queueQ.length) {
        let nodeP = queueP.shift();
        let nodeQ = queueQ.shift();

        if (!nodeP && !nodeQ) continue;
        if (!nodeP || !nodeQ || nodeP.val !== nodeQ.val) return false;

        queueP.push(nodeP.left);
        queueQ.push(nodeQ.left);
        queueP.push(nodeP.right);
        queueQ.push(nodeQ.right);
    }

    return queueP.length === 0 && queueQ.length === 0;
};
