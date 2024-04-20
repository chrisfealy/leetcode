var containsDuplicate = function(nums) {
    const dupes = new Set()
    for(const num of nums) {
        if(dupes.has(num)) return true
        dupes.add(num)
    }
    return false
};
