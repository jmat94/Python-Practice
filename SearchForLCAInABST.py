"""
Program to find the Lowest common ancestor in a Binary Search Tree


Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the 
lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant 
of itself).

The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root. 
Computation of lowest common ancestors may be useful, for instance, as part of a procedure for 
determining the distance between pairs of nodes in a tree: the distance from n1 to n2 can be 
computed as the distance from the root to n1, plus the distance from the root to n2, minus 
twice the distance from the root to their lowest common ancestor. (Source Wiki)


"""


# Node class
class Node:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None



def searchForLCAInABST(rootNode, childNode1, childNode2):

	"""
	Function find the LCA in a BST

	Parameters: 

		rootNode - Node
		childNode1 - Integer
		childNode2 - Integer

	Returns:

		lca value

	"""
	

	# Checks if rootNode is present or not
	if (rootNode == None):
		return None


	# If root value is greater than childNode1 and childNode, the lca is present in the left side
	if (rootNode.value > childNode1 and rootNode.value > childNode2):
		return searchForLCAInABST(rootNode.left, childNode1, childNode2)


	# If root value is less than childNode1 and childNode, the lca is present in the right side
	if (rootNode.value < childNode1 and root.value < childNode2):
		return searchForLCAInABST(rootNode.right, childNode1, childNode2)

	return rootNode


rootNode = Node(35)
rootNode.left = Node(10)
rootNode.right = Node(28)
rootNode.left.left = Node(6)
rootNode.left.right = Node(15)
rootNode.left.right.right = Node(20)

childNode1 = 2
childNode2 = 20

lca1 = searchForLCAInABST(rootNode, childNode1, childNode2)
print(f" The lca of {childNode1} and {childNode2} is {lca1.value}")



