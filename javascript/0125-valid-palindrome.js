var isPalindrome = function(s) {
    let l = 0
    let r = s.length - 1
    while(l <= r) {
        if(!/^[a-zA-Z0-9]+$/.test(s[l])) l++
        else if(!/^[a-zA-Z0-9]+$/.test(s[r])) r--
        else if(s[l].toUpperCase() !== s[r].toUpperCase()) return false
        else {
            l++
            r--
        }
    }
    return true
};
