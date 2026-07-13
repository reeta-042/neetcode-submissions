# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val > list2.val:
            tail = list2
            current1 = list2.next
            current2 = list1

        else:
            tail = list1
            current1 = list1.next
            current2 = list2

        head = tail


        while current1 != None and current2!= None:
            if current1.val > current2.val:
                tail.next = current2
                current2 = current2.next
            else:
                tail.next = current1
                current1 = current1.next
            tail = tail.next

        if current1 != None:
            tail.next = current1
        if current2 != None:
            tail.next = current2

        return head

        