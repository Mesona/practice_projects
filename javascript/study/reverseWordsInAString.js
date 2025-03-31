// https://leetcode.com/problems/reverse-words-in-a-string/submissions/

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let reversedString = s.split(' ').reverse().join(' ');
    if (reversedString[0] === " ") {
        while (reversedString[0] === " ") {
            reversedString = reversedString.slice(1);
        }
    }
    if (reversedString[reversedString.length - 1] === " ") {
        while (reversedString[reversedString.length - 1] === " ") {
            reversedString = reversedString.slice(0, reversedString.length - 1);
        }
    }
    return reversedString.replace(/  +/g, ' ');
};
