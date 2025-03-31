
// https://leetcode.com/problems/add-two-numbers/

// You are given two non-empty linked lists representing 
// two non-negative integers. The digits are stored in reverse 
// order and each of their nodes contain a single digit. Add 
// the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading 
// zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function(l1, l2) {
  let l3 = null;
  let current = null;
  let previous = null;
  let currentL1 = l1;
  let currentL2 = l2;
  let carryOver = 0;
  let next = true;
  while (next === true) {
    let temp = 0;
    if (currentL1 !== null) {
        temp += currentL1.val;
    }
    if (currentL2 !== null) {
        temp += currentL2.val;
    }
    current = new ListNode(temp + carryOver);
    if (previous !== null) {
      previous.next = current;
    }

    if (current.val > 9) {
      carryOver = Math.floor(current.val / 10);
      current.val = current.val % 10;
    } else {
      carryOver = 0;
    }

    if (l3 === null) {
      l3 = current;
    } 
    previous = current;

    if (currentL1 !== null) {
      currentL1 = currentL1.next;  
    }
      
    if (currentL2 !== null) {
      currentL2 = currentL2.next;
    }
      
    if (currentL1 === null && currentL2 === null && carryOver === 0) {
        next = false;
    }

  }

  return l3;
};
