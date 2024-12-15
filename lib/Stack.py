class Stack:

    def __init__(self, items=None, limit=100):
        """
        Initializes the stack with an optional list of initial items and an optional limit for the stack.
        """
        if items is None:
            items = []  # If no initial items are provided, use an empty list
        self.stack = items
        self.limit = limit

    def isEmpty(self):
        """
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def push(self, item):
        """
        Adds an item to the top of the stack.
        Raises an error if the stack is full.
        """
        if self.full():
            raise IndexError("Stack is full")
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        Raises an error if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Returns the item from the top of the stack without removing it.
        Raises an error if the stack is empty.
        """
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self):
        """
        Returns the number of items in the stack.
        """
        return len(self.stack)

    def full(self):
        """
        Returns True if the stack is full, False otherwise.
        If a limit is set, checks if the stack has reached that limit.
        """
        return len(self.stack) >= self.limit

    def search(self, target):
        """
        Searches for an item in the stack. Returns the distance (index from the top) of the target element.
        If the target is found at the top of the stack, it returns 0.
        If the target is not found, it returns -1.
        """
        try:
            index = self.stack.index(target)
            return len(self.stack) - 1 - index
        except ValueError:
            return -1
