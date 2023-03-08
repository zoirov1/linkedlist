class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedLinst:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def sum(self) -> int:
        ls = self.head
        sm = 0
        while ls:
            sm += ls.data
            ls = ls.next
        return sm

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def min(self) -> int:
        num = self.head
        mn = self.head.data
        while num:
            if mn > num.data:
                mn = num.data
            num = num.next
        return mn
    
    def max(self) -> int:
        num = self.head
        mx = self.head.data
        while num:
            if mx < num.data:
                mx = num.data
            num = num.next
        return mx

    def max_min(self) -> None:
        mn = self.min()
        mx = self.max()
        temp = self.head
        while temp:
            if temp.data == mn:
                temp.data = mx
            elif temp.data == mx:
                temp.data = mn
            temp = temp.next

    def insertInto(self, pre_node, new_data):
        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_node


       


        
        
#1
# llis = LinkedLinst()
# for i in range(int(input('>>> '))):
#     llis.append(i)
# print('sum of elements in linkedlist >>>',llis.sum())


# #2
# llis = LinkedLinst()
# llis.append(23)
# llis.append(98)
# llis.append(-12)
# print('min of elements in linked list >>>',llis.min())


# #3
# llis = LinkedLinst()
# for i in range(1,int(input('>>> '))):
#     llis.append(i)
# llis.max_min()
# llis.printList()
# Combinations Of string "GeEKS" OF SIZE 3.

#4
