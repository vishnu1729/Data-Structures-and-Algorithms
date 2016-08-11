"""definition of linked list implementation of s stack ADT
the different memeber functions are described beside in the comments
the class LinkedStack uses a private nested class Node that holds the units of the LinkedList"""
"""Author: Vishnu Muralidharan"""
class LinkedStack:
#non-public nested class Node
    class _Node:
        def __init__(self,element,next): #constructor to initialize element and next pointer
            self._element = element
            self._next = next

    def __init__(self):     #consturctor to LinkedStack class
        #initialize empty stack
        self._head = None
        self._size = 0

    def __len__(self):      #length of the stack
        return self._size

    def isempty(self):      #function to check if the stack is empty
        return self._size == 0

    def push(self,e):       #push is similar inserting node at the beginnign of the list
        #the new element is set to head of the list
        #the new head node's element is set to e and the new head's next filed points to the previous head
        self._head = self._Node(e,self._head)   
        self._size += 1

    def top(self):
        if isempty():
            print("The stack is empty")
        #return top element of stack
        return self._head._element

    def pop(self):      #pop is similar to removing elemennet from head of linked list
        if isempty():
            print("Stack is empty")
        answer = self._head._element
        self._head = self._head._next   #set the head node to the next node after old head node
        self._size -= 1
        return answer
    
