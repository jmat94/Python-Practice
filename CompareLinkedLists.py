"""
Program to compare two linked lists
"""


# Node class
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None



class LinkedList:
	def __init__(self):
		self.head = None



	def push(self, value):

		"""
			Function to add an element to the end of a linked list

			Parameters: 

					value - An Integer

		"""

		new_node = Node(value)

		new_node.next = self.head

		self.head = new_node



	def checkIfIdentical(self, secondList):

		"""
			Function to check if two linked lists are identical

			Parameters: 
					secondList: A Linked List

			Returns: Boolean value

		"""
		
		firstLinkedList = self.head
		secondLinkedList = secondList.head

		while(firstLinkedList != None and secondLinkedList != None):
			if (firstLinkedList.value != secondLinkedList.value):
				return False


			firstLinkedList = firstLinkedList.next
			secondLinkedList = secondLinkedList.next

		return (firstLinkedList == None and secondLinkedList == None)


	def print_list(self):

		"""
			Function to print the elements in a linked list
		"""

		new_node = self.head

		while(new_node != None):
			print(new_node.value)
			new_node = new_node.next


firstLinkedList = LinkedList()
secondLinkedList = LinkedList()

firstLinkedList.push(1)
firstLinkedList.push(2)
firstLinkedList.push(3)


secondLinkedList.push(1)
secondLinkedList.push(2)
secondLinkedList.push(3)




if(firstLinkedList.checkIfIdentical(secondLinkedList) == True):
	print("The two linked lists are identical")
else:
	print("The two linked lists are not identical")



