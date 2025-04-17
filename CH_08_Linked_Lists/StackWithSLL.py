class LinkedStack:
    """LIFO Stack implementation using a Singly Linked List for storage"""
    #-------------------nested Node_ Class---------------------------------
    class Node_:
        """Lightweight, nonpublic class for storing a singly linked node."""
        #streamline memory usage
        __slots__ = '_element', '_next' 
        
        def __init__(self, element, next):
            #reference to user's element
            self._element = element
            #reference to next node
            self._next = next
        
        #---------------------------------STACK Methods-------------------------------------------
        def __init__(self):
            """Create empty stack"""
            #reference to head node
            self._head = None
            #number of stack elements
            self._size = 0
            
        def __len__(self):
            """Return the number of elements in the stack"""
            return self._size
        
        def is_empty(self):
            """Return True if the stack is empty"""
            return self._size == 0
        
        def push(self, e):
            """Add element e to the top of the stack"""
            #create and link a new node
            self._head = self._Node(e, self._head)
            self._size += 1
            
        def top(self):
            """Return (but not remove) the element at the top of stack.
            Raise Empty exception if the stack is empty
            """
            if self.is_empty():
                raise Empty('Stack is empty')
            #top of stack is at head of list
            return self._head._element
        
        def pop(self):
            """Remove and return the element at the top of the Stack (i.e. LIFO)
            Raise Empty Exception if the stack is empty
            """
            if self.is_empty():
                raise Empty('Stack is Empty')
            answer = self._head._element
            #bypass the former top node
            self._head = self._head._next
            self._size -= 1
            return answer
        
            
            