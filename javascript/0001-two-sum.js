var twoSum = function(nums, target) {
    map = {}
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i]
        if(complement in map) return [map[complement], i]
        map[nums[i]] = i
    }
    return []
};
