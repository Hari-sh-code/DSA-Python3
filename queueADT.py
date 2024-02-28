class Node:
    def __init__(self,data=0):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = Node()

    def isempty(self): 
        if self.front.next == None: 
            return True 
        return False

    def enqueue(self, ele): 
        temp = Node()
        temp.data = ele 
        temp.next = self.rear.next 
        self.rear.next = temp 
        self.rear = temp 

    def dequeue(self): 
        if self.front.next == None: 
            print("The queue is empty") 
        else: 
            temp = self.front.next 
            self.front.next = temp.next 
            d = temp.data 
            temp = None 
            return d 

    def display(self): 
        temp = self.front 
        if temp.next == None: 
            print("Empty List") 
        else: 
            print() 
            while(temp.next!=None): 
                temp = temp.next 
                print("->",temp.data,end="") 

    def size(self): 
        temp = self.front 
        s=0 
        if temp.next == None: 
            return 0 
        else: 
            while(temp.next!=None): 
                temp = temp.next 
                s = s+1 
            return s 

    def get_front(self): 
        if not self.isempty(): 
            return self.front.next.data 
        raise Exception("Queue empty") 

S = Queue()

while (True):
    print()
    print("Enter the choices:- \n1.Enqueue \n2.Front \n3.Dequeue \n4.Display \n5.Size \n6.Exit ")
    c = int(input("Enter the choices: "))
    if(c==1):
        ele = int(input("Enter the element: "))
        S.enqueue(ele)
        S.display()
    elif(c==2):
        print("The front of the queue is ",S.get_front())
    elif(c==3):
        print("The dequeued element is ",S.dequeue())
    elif(c==4):
        S.display()
    elif(c==5):
        print("Size of the Queue: ",S.size())
    elif(c==6):
        break