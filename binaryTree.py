
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.Tail = None

    def binarySearchTree(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(temp):
                if(newNode.data < temp.data and temp.prev == None):
                    temp.prev = newNode
                    break
                elif(newNode.data < temp.data and temp.prev != None):
                    temp = temp.prev
                elif(newNode.data > temp.data and temp.next == None):
                    temp.next = newNode
                    break
                else:
                    temp = temp.next       
    def inorderTraverse(self):
        stack = []
        current = self.head
        
        while(True):
            if(current is not None):
                stack.append(current)
                current = current.prev
            elif(current is None):
                current = stack.pop()
                print(current.data)
                current = current.next
            if(current == None and len(stack) == 0):
                break
    def preorderTraverse(self):
        stack = []
        current = self.head
        
        while(True):
            if(current is not None):
                stack.append(current)
                print(current.data)
                current = current.prev
            elif(current is None):
                current = stack.pop()
                current = current.next
            if(current == None and len(stack) == 0):
                break
    def postorderTraverse(self):
        root = self.head
        stack = []
        while(True):
            while(root is not None):
                stack.append(root)
                stack.append(root)
                root = root.prev
            if(len(stack) == 1):
               print(stack[-1].data)
               return
            root = stack.pop()
            
            if(root == stack[-1] or len(stack) == 0):
                root = root.next
            else:
                print(root.data)
                root = None
            # print(len(stack))

        
    def binaryTree(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
        else:
            temp = self.head
            while(True):
                if(temp.next == None and temp.prev == None):
                    print("Left and Right node free for ",temp.data)
                elif(temp.next != None and temp.prev == None):
                    print("right node not free and left node is free for ",temp.data)
                elif(temp.next == None and temp.prev != None):
                    print("right node free and left node not free for ",temp.data)
                elif(temp.next != None and temp.next != None):
                    print("Left and Right not node free for ",temp.data)
                    
                n = int(input("\n1.Enter 1 to insert node at left\n2.Enter 2 to insert node at right\n3.move to left\n4.move to right\n5.break\n"))
                if(temp.prev == None and n == 1):
                    temp.prev = newNode
                    print("Node inserted at left successfully")
                    break
                elif(temp.next == None and n == 2):
                    temp.next = newNode
                    print("Node inserted at right successfully")
                    break
                elif(n == 3):
                    if(temp.prev == None):
                        print("left value is None please enter value to insert or go to right\n")
                        continue
                    temp = temp.prev
                elif(n == 4):
                    if(temp.next == None):
                        print("right value is None please enter value to insert or go to left\n")
                        continue
                    temp = temp.next
                else:
                    print("Enter valid number\n")
                    
while(True):
    print("1.create the head\n2.insert the node\n3.Inorder\n4.preorder\n5.postorder\n6.binary tree insert\n")
    n = int(input("Enter the choice\n"))
    if(n == 1):
        List = LinkedList()
    elif(n == 2):
        data = int(input("Enter the data\n"))
        List.binarySearchTree(data)
    elif(n == 3):
        List.inorderTraverse()
    elif(n == 4):
        List.preorderTraverse()
    elif(n == 5):
        List.postorderTraverse()
    elif(n == 6):
        data = int(input("Enter the data\n"))
        List.binaryTree(data)
    else:
        break
        