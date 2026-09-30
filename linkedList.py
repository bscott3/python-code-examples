class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def AtStart(self, data):
        print(f"Adding {data} to the start of the list")
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode

    def Inbetween(self,middle_node, newdata):
        if middle_node is None:
            print("The given node is not present in the list")
            return
        print(f"Inserting {newdata} after {middle_node.data}")
        NewNode = Node(newdata)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def AtEnd(self, data):
        print(f"Adding {data} to the end of the list")
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return 
        tail = self.head
        while(tail.next):
            tail=tail.next
        tail.next = NewNode

    def DeleteNode(self, key):
        print(f"Deleting Node with data {key}")
        Header = self.head
        if Header is not None:
            if Header.data == key:
                self.head = Header.next
                Header = None
                return
        if Header is None:
            print(f"Node with data {key} not found")
            return
        while Header.next is not None and Header.next.data != key:
            Header = Header.next
        if Header.next is None:
            print(f"Node with data {key} not found")
            return
        Header.next = Header.next.next

    def listprint(self):
        output = self.head
        while output is not None:
            print(output.data)
            output = output.next
    

list1 = SLL()
list1.head = Node('Mon')
e2 = Node('Tue')

list1.head.next = e2

# in singular linked list you can only traverse the list in the forward direction

list1.listprint()

# lets add thurs to the linked list by adding it 
list1.AtEnd('Thurs')
list1.listprint()

# lets add Sunday to the beginning of the linked list
list1.AtStart('Sun')
list1.listprint()

# lets insert Wednesday after Tuesday
list1.Inbetween(e2, 'Wed')
list1.listprint()

# lets delete a node with data 'Tue'
list1.DeleteNode('Tue')
list1.listprint()

print(list1)