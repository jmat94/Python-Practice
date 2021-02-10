"""
Designing a stack using a singly linked list along with stack operations
"""


class Node:
	def __init__(self, value):
		
		self.value = value
		self.next = None


class StackUsingSinlgyLinkedList:

	def __init__(self):

		self.head = None


	def push(self, value):

		"""
		Function to add an element at the top of the stack

		Parameters:

				value - An integer

		"""

		if (self.head == None):

			self.head = Node(value)

		else:

			new_node = Node(value)

			new_node.next = self.head

			self.head = new_node


	def pop(self):

		"""
		Function to remove an element from the stack

		Returns:

				None or the value which is popped
		"""
		
		if (self.head == None):
			
			return None

		else:

			nodeToBePopped = self.head

			self.head = self.head.next

			nodeToBePopped.next = None

			return nodeToBePopped.value



	def peek(self):

		"""
		Function to see the element present at the top of the stack

		Returns: 

				None if no element is found

				A value if an element is present at the top
		"""

		if (self.head == None): 
			 
			return None

		else:
			
			return self.head.value


	
	def print_stack(self):

		"""
		Function to print the elements in a stack
		"""

		if(self.head == None):
			return None

		else:

			new_node = self.head

			while(new_node != None):

				print(new_node.value, end = " ")

				new_node = new_node.next

			return




ll1 = StackUsingSinlgyLinkedList()
ll2 = StackUsingSinlgyLinkedList()

# Pushing elements to the top of the stack
ll1.push(1)
ll1.push(2)
ll1.push(3)

# Checking the topmost element in the stack
ll1.peek()

# Removing the element present at the top of the stack
ll1.pop()

# Printing the elements of the stack
ll1.print_stack()



