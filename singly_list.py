# headList = LinkedList()

# headList.head = Node(1)

# headList.head.next = Node(2)

# headList.head.next.next = Node(3)

# temp = headList.head

# while(temp != None):
#     print(temp.data)
#     temp = temp.next


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.Tail = None

    def insertFirst(self,data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            self.Tail = newNode
            return
        newNode.next = self.head
        self.head = newNode
    
    def insertLast(self,data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            self.Tail = newNode
            return
        self.Tail.next = newNode
        self.Tail = newNode
    
    def deleteFirst(self):
        self.head = self.head.next
    
    def deleteLast(self):
        temp = self.head
        while(temp.next.next != None):
            temp = temp.next
        Tail = temp
        temp.next = None
    
    def insertAtGivenPosition(self, newNode, pos):
        if(self.head == None):
            self.insertFirst(data)
            return
        temp = self.head
        temp1 = None
        while(pos>0):
            temp1 = temp
            temp = temp.next
            pos = pos - 1
        temp1.next = newNode
        newNode.next = temp

    def deleteAtGivenPostion(self, pos):
        if(self.head == None):
            print("List is empty")
            return
        temp = self.head
        temp1 = None
        while(pos>0):
            temp1 = temp
            temp = temp.next
            pos = pos - 1
        temp1.next = temp.next
    
    def findMiddle(self):
        temp = self.head
        temp1 = self.head
        while(temp1.next):
            temp1 = temp1.next
            if(temp1.next != None):
                temp = temp.next
                temp1 = temp1.next
        print(temp.data)
    def findElement(self, data1):
        temp = self.head
        temp1 = None
        while(temp != None):
            temp1 = temp
            temp = temp.next
            if(temp.data == data1):
                # print(temp1.data,temp.data)
                return temp1,temp
                
    def swapNode(self, data1, data2):
        temp = self.head
        temp1 = self.head
        temp2 = None
        temp3 = None
        temp4 = None
        if(temp.data == data1):
            temp2, temp3 = self.findElement(data2)
            print(temp2.data,temp3.data)
            self.head = temp3
            temp4 = temp3.next
            self.head.next = temp.next
            temp2.next = temp
            temp.next = temp4
            print("erwe")
            return
        elif(temp1.data == data2):
            temp2, temp3 = self.findElement(data1)
            self.head = temp3
            temp4 = temp3.next
            self.head.next = temp1.next
            temp2.next = temp1
            temp1.next = temp4
            return

        temp2,temp = self.findElement(data1) 

        temp3, temp1 = self.findElement(data2)
        if(temp.next == temp1):
            temp2.next = temp1
            temp4 = temp1.next
            temp1.next = temp
            temp.next = temp4
            return
        temp2.next = temp1
        temp4 = temp1.next
        temp1.next = temp.next
        temp3.next = temp
        temp.next = temp4

    def reverseList(self, data):
        current = self.head
        prev = None
        newNode = self.head
        while(newNode):
            newNode = newNode.next
            current.next = prev
            prev = current
            current = newNode
        self.head = prev

    def reverseListBySize(self, size):
        current = self.head
        prev = None
        newNode = self.head
        newNode1 = self.head
        flag = 0
        while(newNode):
            size1 = size*2-1
            newNode1 = newNode
            while(newNode1.next and size1 != 0):
                temp = newNode1
                newNode1 = newNode1.next
                size1 = size1 - 1

            if(size1 >= size):
                prev = None
            else:
                prev = newNode1
            size1 = size
            # print(prev)
            while(newNode and size1 != 0):
                size1 = size1 - 1
                newNode = newNode.next
                current.next = prev
                prev = current
                print(current.data)
                print(prev.data)
                current = newNode

            print("        ")
            if(flag == 0):
                self.head = prev
                flag = 1

while(True):
    n = int(input("1.create a head\n2.display\n3.insert at First\n4.insert at Last\n5.delete at First\n6.delete at Last\n7.insert at the given position\n8.delete at the given position\n9.find the Middle Node\n10.swap the node\n15.exit\n"))    
    print("-----------------------------")
    
    if(n == 1):
        List = LinkedList()
        print("head created successfully")
    elif(n == 2):
        temp = List.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.next
    elif(n == 3):
        data = int(input("Enter the data\n"))
        List.insertFirst(data)
    elif(n == 4):
        data = int(input("Enter the data"))
        List.insertLast(data)
    elif(n == 5):
        List.deleteFirst()
    elif(n == 6):
        List.deleteLast()
    elif(n == 7):
        data = int(input("Enter the data\n"))
        newNode = Node(data)
        pos = int(input("Enter the position\n"))
        List.insertAtGivenPosition(newNode, pos)
    elif(n == 8):
        pos = int(input("Enter the position\n"))
        List.deleteAtGivenPostion(pos)
    elif(n == 9):
        List.findMiddle()
    elif(n == 10):
        List.swapNode(2,3)
    elif(n == 11):
        data = int(input("Enter the number\n"))
        List.reverseList(data)
    elif(n == 12):
        data = int(input("Enter the number\n"))
        List.reverseListBySize(data)
    else:
        break
    print("\n-----------------------------")
