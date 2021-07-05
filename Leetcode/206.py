# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if not head:
#             return
#         if not head.next:
#             return head
#         sec = head.next
#         head.next = None
#
#         def rev(node1, node2):
#             if node2.next:
#                 node3 = node2.next
#                 if node3.next:
#                     node4 = node3.next
#                 else:
#                     node4 = None
#             else:
#                 node3 = None
#                 node4 = None
#             node2.next = node1
#             if node3:
#                 node3.next = node2
#             else:
#                 return node2
#             if node4:
#                 return rev(node3, node4)
#             else:
#                 node3.next = node2
#                 return node3
#
#         return rev(head, sec)
class Solution(object):
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        temp1 = head
        temp2 = head.next
        head.next = None
        while temp2.next:
            temp3 = temp2.next
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
        return temp2
