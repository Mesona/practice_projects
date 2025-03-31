/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
 * @param {string} s
 * @return {number}
 */

var lengthOfLongestSubstring = function(s) {
    let longest = ""
    let current = ""
    for (i = 0; i < s.length; i++) {
        if (current.includes(s[i])) {
            current = current.slice(current.indexOf(s[i]) + 1)
            current += s[i];
        } else {
            current += s[i]
            if (current.length > longest.length) {
                longest = current;
            }
        }
    }
    
    return longest.length
};
