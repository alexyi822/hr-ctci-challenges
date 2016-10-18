"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    tortoise = head
    hare = head
    
    while tortoise is not None and tortoise.next is not None:
        tortoise = tortoise.next
        hare = hare.next.next
        
        if tortoise == hare:
            return True
        
    return False