class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front is None
    def enqueue(self,data):
        nn=node(data)
        if self.front is None:
            self.front=nn
            self.rear=nn
        else:
            self.rear.next=nn
            self.rear=nn
        print("value is entered")
    def dequeue(self):
        if self.is_empty():
            return "There are empty queue"
        delete_value=self.front
        self.front=self.front.next
        return delete_value.data
    def size(self):
        count=0
        cur=self.front
        while cur:
            count+=1
            cur=cur.next
        return count
    def peek(self):
        return self.front.data
    def display(self):
        if self.is_empty():
            return "Empty Queue"
        cur=self.front
        while cur is not None:
            print(cur.data)
            cur=cur.next
        print()
q=queue()
q.enqueue(25)
q.enqueue(36)
q.enqueue(39)
q.enqueue(45)
q.enqueue(91)
q.enqueue(37)
q.display()
print(q.size())
print(q.peek())
print(q.dequeue())

