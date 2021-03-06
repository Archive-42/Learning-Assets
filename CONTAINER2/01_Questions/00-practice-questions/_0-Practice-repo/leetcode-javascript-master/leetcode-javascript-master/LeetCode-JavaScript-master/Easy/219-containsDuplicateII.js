/**
 * key: use JavaScript Object to keep track the num and its index
 * REMEBER: use if (key in Obj) to check if the Obj has the key 'key'
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
const containsNearbyDuplicate = (nums, k) => {
    const numIndex = {};
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in numIndex) {
            if (i - numIndex[nums[i]] <= k) {
                return true;
            }
        }
        numIndex[nums[i]] = i;
    }

    return false;
};
