# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def getSum(linkedList):
            count = 0
            total = 0
            current = linkedList

            #we use val to get the value at current pointer then multiply it to 10 raise to depending on its place value 
            while current:
                total += current.val * (10 ** count)
                count += 1
                current = current.next
            
            return total
        
        finalTotal = getSum(l1) + getSum(l2)
        #yey were done we did get the sum of the linked list now we need to code it back into a linked list in reverse

        #we convert the int to a string to iterate each number
        stringT = str(finalTotal)
        lenString = len(stringT) - 1
        
        #here we created the node and assigned the value of last number in the stringT as desired.
        dummy_head = ListNode(int(stringT[lenString]))
        current = dummy_head

        #i did not use for i in range instead while loop so we can reverse the iteration. I started with maximum value which is the len of the String but we did use the last value earlier so we prioritize subtracting one then add the succeeding node and value to the list and move the pointer
        while lenString > 0:
            lenString -= 1
            new_node = ListNode(int(stringT[lenString]))
            current.next = new_node
            current = current.next
        
        return dummy_head
        
