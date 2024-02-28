class node:
    def __init__(self):
        self.data = None
        self.next = None

class Solution:
    
    def createnode(self):
        self.header = node()
        self.header.data = -1
        self.header.next = None
        return self.header
    
    def isempty(self,top):
        if(top.next == None):
            return True
        return False
    
    def size(self,top):
        if self.isempty(top):
            raise Exception("Stack Underflow")
        else:
            temp = top
            s = 0
            while (temp.next != None):
                temp = temp.next
                s=s+1
            return s
        
    def peek(self,top):
        if self.isempty(top):
            raise Exception("Stack Underflow")
        else:
            return top.next.data
    
    def display(self,top):
        if self.isempty(top):
            raise Exception("Stack Underflow")
        else:
            temp=top
            s=0
            while(temp.next != None):
                temp = temp.next
                print("=>",temp.data,end=" ")
    
    def push(self,top,ele):
        temp = node()
        temp.data = ele
        temp.next = top.next
        top.next = temp

    def pop(self,top):
        if self.isempty(top):
            raise Exception("Stack Underflow")
        else:
            temp = top.next
            top.next = temp.next
            d = temp.data
            temp = None
            return d
        
S = Solution()
top = S.createnode()
while (True):
    print()
    print("Enter the choices:- \n1.Push \n2.Peek \n3.Pop \n4.Display \n5.Size \n6.Exit ")
    c = int(input("Enter the choices: "))
    if(c==1):
        ele = int(input("Enter the element: "))
        S.push(top,ele)
        S.display(top)
    elif(c==2):
        print("The top of the element is ",S.peek(top))
    elif(c==3):
        print("The pop out element is ",S.pop(top))
    elif(c==4):
        S.display(top)
    elif(c==5):
        print("Size of the Stack: ",S.size(top))
    elif(c==6):
        break