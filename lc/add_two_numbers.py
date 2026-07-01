from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, with each node containing a single digit.
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain leading zeros, except for the number 0 itself.

    --> Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

    --> Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    --> Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
    Explanation: 9,999,999 + 9,999 = 10,009,998.

    Return the resulting sum as a linked list in reverse order.

                resulting_l
                      │
                      ▼
                 ┌───────────┐      ┌───────────┐      ┌───────────┐      ┌───────────┐
    Nodes:       │  val: 0   │ ───> │  val: 7   │ ───> │  val: 0   │ ───> │  val: 8   │
                 └───────────┘      └───────────┘      └───────────┘      └───────────┘
                      ▲                  ▲
                      │                  │
                 Dummy Node          resulting_l.next
                (Discarded)         (Actual Answer Start)
            
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        My logic:
        I traverse both linked lists at the same time, adding the corresponding
        digits along with any carry from the previous addition. If one list is
        shorter than the other, I treat its missing values as 0. For each sum,
        I create a new node containing the current digit and continue until
        both lists and the carry have been fully processed.

        
        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
    
        """
        resulting_l = ListNode(0)  # Dummy head node to simplify building the resulting linked list
        curr = resulting_l     # Pointer used to append new nodes to the result
        carry = 0              # Variable to keep track of carry-over during addition

        while l1 or l2 or carry: 
            # If a list has ended, treat its value as 0
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 
            carry, total = divmod(val1 + val2 + carry, 10) # divmod returns (carry, current digit)
            # Append the current digit to the result list
            curr.next = ListNode(total)
            curr = curr.next 
            # Move to the next node in each list if possible
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

        return resulting_l.next

# Test the solution 

def buildLinkedList(values):
    """Converts Python list -> Linked List"""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def printLinkedList(head):
    """Converts Linked List -> Python list and prints it"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

def main():
    sol = Solution()
    # Example 1
    l1 = buildLinkedList([2, 4, 3])
    l2 = buildLinkedList([5, 6, 4])
    res = sol.addTwoNumbers(l1, l2)
    printLinkedList(res)  # [7,0,8]
    # Example 2
    l1 = buildLinkedList([0])
    l2 = buildLinkedList([0])
    res = sol.addTwoNumbers(l1, l2)
    printLinkedList(res)  # [0]
    # Example 3
    l1 = buildLinkedList([9,9,9,9,9,9,9])
    l2 = buildLinkedList([9,9,9,9])
    res = sol.addTwoNumbers(l1, l2)
    printLinkedList(res)  # [8,9,9,9,0,0,0,1]

if __name__ == "__main__":
    main()