class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        

# def insert_new(head , data ):
#     new_node = Node(data)
#     new_node.next= head
#     return new_node

# def insert_last(head, data ):
#     temp = head
#     while temp.next :
#             temp = temp.next
#     temp.next = Node(data)
#     return head
 
def insert_middile(head ,data , pos):
    temp = head
    for i in range (pos - 1):
        temp = temp.next

    new_node = Node(data)
    new_node.next = temp.next
    temp.next = new_node
    return head     


head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

head.next = second
second.next = third
third.next = fourth

# head  = insert_new(head , 56)
# head  = insert_last(head , 56)
head = insert_middile(head, 45 , 3)

temp = head

while temp is not None:
     print(temp.data)
     temp = temp.next