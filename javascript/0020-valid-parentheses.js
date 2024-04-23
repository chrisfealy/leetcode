var isValid = function(s) {
    const map = {')': '(', '}': '{', ']': '['}
    const stack = []
    for(const c of s) {
        if(c in map) {
            if(!stack.length || stack[stack.length - 1] !== map[c]) return false
            stack.pop()
        }
        else stack.push(c)
    }
    return !stack.length
};
