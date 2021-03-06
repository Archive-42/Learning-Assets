const { tree } = require("./index");

const nums = tree();
nums.insert(23);
nums.insert(45);
nums.insert(16);
nums.insert(37);
nums.insert(3);
nums.insert(99);
nums.insert(22);

console.log("Inorder traversal: ");
nums.inOrder(nums.getRoot());
console.log("\nPreorder traversal: ");
nums.preOrder(nums.getRoot());
console.log("\nPostorder traversal: ");
nums.postOrder(nums.getRoot());
console.log(`Find value 45: `);
console.log(nums.find(45));

test("Binary tree", (assert) => {
  assert.equal(nums.totalNodes(), 7, `Total of nodes is ${nums.totalNodes()}`);
  assert.equal(
    nums.totalEdges(nums.getRoot()),
    4,
    `Total of edges is ${nums.totalEdges(nums.getRoot())}`
  );
  assert.equal(
    nums.maxValue(),
    99,
    `Max value of the tree is ${nums.maxValue()}`
  );
  assert.equal(
    nums.minValue(),
    3,
    `Min value of the tree is ${nums.minValue()}`
  );
});
