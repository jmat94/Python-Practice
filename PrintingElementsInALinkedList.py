"""
Python program to print elements in a linked list

"""


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class SinglyLinkedList:
	
	def __init__(self):

		self.head = None

	
	def push(self, value):

		"""
		Function to add elements to the top of a linked list

		Paramaters:

			value - int

		"""

		if(self.head == None):

			self.head = Node(value)

		else:
			
			new_node = Node(value)

			new_node.next = self.head

			self.head = new_node

	
	def printElements(self):

		"""
		
		Function to print the elements in a linked list

		"""

		if (self.head == None):
			return None

		new_node = self.head

		while(new_node != None):

			print(new_node.value)

			new_node = new_node.next



linkedList = SinglyLinkedList()
linkedList.push(1)
linkedList.push(2)
linkedList.push(3)

linkedList.printElements()








