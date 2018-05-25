'''
Nas notas de aula sobre Listas, apresenta-se uma lista duplamente encadeada. Para este exercício,
implemente uma lista singularmente encadeada não-ordenada.
'''
class Node(object):

	def __init__(self):
		self.key = None
		self.next = None


	def setKey(self, key):
		self.key = key

	def getKey(self):
		return self.key


class LinkedList(object):

	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, element):
		node = Node()
		node.setKey(element)

		if self.isEmpty():
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def remove(self):

		if not self.isEmpty():
			self.aux = self.head.key
			self.head = self.head.next
		else: 
			print("List is empty")
		print("Elemento removido", self.aux)

	def isEmpty(self):
		if self.tail == None and self.head == None:
			return True
		else:
			return False
	
	def show(self):
		self.aux = self.head
		while self.aux != None:
			print(self.aux.key)
			self.aux = self.aux.next


mylist = LinkedList()
mylist.insert(10)
mylist.insert(30)
mylist.insert(40)
mylist.insert(50)
mylist.show()
mylist.remove()
mylist.show()


