# Convert Binary Number in a Linked List to Integer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        vals = []
        vals.append(head.val)
        while(head.next != None):
            head = head.next
            vals.append(head.val)
        # print(vals)
        # print(len(vals))
        res = 0
        power = range(len(vals)-1, -1, -1)
        for i in range(len(vals)):
            # print(i)
            # print('temp =' + str(vals[i]*pow(2,power[i])))
            res += vals[i]*pow(2,power[i])
            # print('res = ' + str(res))
        return(res)
        