# ---Problem 1: Remove Duplicates from an Unsorted Linked List---
# Description:
# Given the head node of an unsorted singly linked list, delete duplicate values from the list so that only distinct values remain.(Keep only the first occurrence of each value)
# Example:
# Input: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 2 -> 1 -> 1 -> null
# Output: 1 -> 2 -> 3 -> 4 -> null
# Requirements:
# ● Method 1: Achieve O(N) time complexity, where N is the length of the list.
# ● Method 2: Achieve O(1) extra space complexity.

class listNode:
    def __init__(self, val=0, next = None):
        self.val = val 
        self.next = next

class linkedList:
    def __init__(self):
        self.dummyHead = listNode() 
        self.size = 0 
    def addAtTail(self, val):
        new = listNode(val)
        current = self.dummyHead
        while current.next != None:
            current = current.next
        new.next = None 
        current.next = new
        self.size += 1

# Method 1:
def removeDuplicates1(head):
    '''
    Time complexity: O(N): The worst case is travese from the head to the tail.
    Space complexity: O(N): In the worst case, set seen will store all the different values, which at most have N.
    '''
    # 1. empty list
    if not head:
        return None
    
    # 2.
    seen = set()
    dummyHead = listNode(0) 
    dummyHead.next = head
    current = dummyHead
    while current and current.next:
        if current.next.val in seen: 
            current.next = current.next.next
        else:
            seen.add(current.next.val)
            current = current.next 
    
    return dummyHead.next


# Method 2:
def removeDuplicates2(head):
    '''
    Time complexity: O(N**2): The worst case is each node have to scan the nodes after itself.
    Space complexity: O(1): The extra variables are pointers, which amount will not grow with N.
    '''
    # 1. empty list
    if not head:
        return None

    # 2. 
    dummyHead = listNode(0)
    dummyHead.next = head

    current = head
    while current:
        pointer = current
        while pointer.next:
            if pointer.next.val == current.val:
                pointer.next = pointer.next.next  # delete duplicate node
            else:
                pointer = pointer.next
        current = current.next

    return dummyHead.next


    
def printList(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("null")


# ---Problem 2: Longest Subarray with Sum Equal to K---
# Description:
# Given an unsorted array arr consisting of positive integers, and a positive integer k, find the length of the longest subarray whose elements sum up to exactly k.
# Example:
# Input: arr = [1, 2, 1, 1, 1], k = 3
# Output: 3
# Explanation: The longest subarray with sum = 3 is [1, 1, 1], so the answer is 3.


def longestSubarray(arr, k):
    left = 0
    right = 0
    currentSum = 0
    maxLen = 0

    while right < len(arr):
        currentSum += arr[right]
        while currentSum > k and left <= right:
            currentSum -= arr[left]
            left += 1
        if currentSum == k:
            maxLen = max(maxLen, right - left + 1)
        right += 1

    return maxLen




if __name__ == '__main__':
    # Question 1
    # build a linked list
    nums = [1, 2, 3, 3, 4, 4, 2, 1, 1]
    ll = linkedList()
    for x in nums:
        ll.addAtTail(x)
    head1 = ll.dummyHead.next
    print(f"【Question 1】: \nThe original linked list is:")
    printList(head1)

    head2 = removeDuplicates1(head1)
    head3 = removeDuplicates1(head1)

    print("After removing duplicates: \n[Method 1] result:")
    printList(head2)
    print("[Method 2] result:")
    printList(head3)

    print("=" * 50)
    
    # Question 2
    print("【Question 2】:")
    print("Test Case 1:")
    arr = [1, 2, 1, 1, 1]
    k = 3
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 2: Empty array")
    arr = []
    k = 3
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 3: Whole array")
    arr = [1, 1, 1, 1]
    k = 4
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 4: Only one element equals k")
    arr = [3, 1, 2, 1]
    k = 3
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 5: No such subarray")
    arr = [1, 2, 3]
    k = 7
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 6: The array has one element which equals k")
    arr = [5]
    k = 5
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)

    print("Test Case 7: The array has one element which not equals k")
    arr = [5]
    k = 3
    print("Input:", arr, "k =", k)
    print("Output:", longestSubarray(arr, k))
    print("-" * 50)








