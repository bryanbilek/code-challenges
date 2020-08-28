# Write a function that receives as input the head node of a linked list and an integer k. Your function should remove the kth node from the end of the linked list and return the head node of the updated list.

# For example, if we have the following linked list:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null

# The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).

# After the function executes, the state of the linked list should be:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null

# If k is longer than the length of the linked list, the linked list should not be changed.

# Can you implement a solution that performs a single pass through the linked list and doesn't use any extra space?

# Note: When reading the tests, the linked list contents are enumerated in between square brackets; this does NOT mean the inputs are arrays.

# For example, a test input of head: [2, 4 ,6] indicates that the input is a singly-linked list
# (2) -> (4) -> (6) -> null whose head is the first element in the linked list.


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# understand: head is the first node in a ll. k is the number of nodes from reverse to remove a node
# plan: traverse through the ll & find the node, then set the pointer from the node before to the node after
def remove_kth_from_end(head, k):
    # edge case if k is 0, return the linked list as is
    if k == 0:
        return head
    # current node were on aka the head
    # counter for num of nodes we traverse through
    cur = head
    num_nodes = 0
    # while cur is not None aka the end of list, cur points to the next node, we add 1 to the count of num_nodes
    # when we reach the end of the loop(list), x is our index for the node we need removed by subtracting all the nodes by k
    while cur is not None:
        cur = cur.next
        num_nodes += 1
    x = num_nodes - k
    # edge case if k is greater than the number of nodes we traversed aka the linked list return the list unchanged
    if k > num_nodes:
        return head
    # create 2 pointers, official pointer starts at the head & prev is pointing 1 node behind
    prev = None
    pointer = head
    # we traverse through the list decrementing x by 1 to get to the node needing removal
    # to run the traversal, prev goes from None to head(pointer) & pointer(head) goes to pointer.next(head.next)
    while x != 0:
        prev = pointer
        pointer = pointer.next
        x -= 1
    # if prev is None, were removing 1st node in the list & returning head.next
    if prev is None:
        return head.next
    else:
        # otherwise & for most cases, we are setting the prev.next's pointer to the pointer.next's node to skip over the node
        # we want to remove
        prev.next = pointer.next
    # finally, return head which is the linked list
    return head
