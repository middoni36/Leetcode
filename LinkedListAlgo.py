class ListNode():
    def __init__(self):
        self.value=None
        self.next=None


class Solution():
    def __init__(self):
        self.head=ListNode()
        self.listofduplicates=[]
    def addnumtolist(self,num):
        if self.head.value==None:
            self.head.value=num

        else:
            b=self.head
            while b.next != None:
                  b=b.next
            a=ListNode()
            a.value=num
            b.next=a

    def deleteDuplicates(self):
         p=self.head
         while p.next :
                if p.next.value==2:
                    p.next=p.next.next
                else:
                    p=p.next
    def removeduplicandaddthemtolist(self):
        current=self.head
        previous=ListNode()
        while current.next :
            if current.value in self.listofduplicates:
                current=current.next
            else:
                self.listofduplicates.append(current.value)
                current=current.next
                if current.next.next==None:
                    previous = current


        if previous.value!=current.value:
            self.listofduplicates.append(current.value)















    def print_elemnts(self):
        b=self.head
        while b.next != None:
            print(b.value)
            b=b.next
        print(b.value)


a=Solution()
a.addnumtolist(2)
a.addnumtolist(2)
a.addnumtolist(3)
a.addnumtolist(3)
a.addnumtolist(3)
a.addnumtolist(4)
a.removeduplicandaddthemtolist()
print(a.listofduplicates)
a.deleteDuplicates()


a.print_elemnts()