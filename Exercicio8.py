'''
Implemente uma pilha utilizando a lista singularmente encadeada. As operações PUSH e POP devem rodar em complexidade temporal de O(1).
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


class Stack(object):

	def __init__(self):
		self.list = LinkedList()

	def push(self, element):
		self.list.insert(element)

	def pop(self):
		x = self.list.head
		while x != None:
			x = x.next
		print("Pop: ", x.key)
		self.list.tail = x
		print("Element, ", self.list.tail.key)
		self.list.tail.next = None
		
	
	def isEmpty(self):	
		return 0

	def show(self):
		self.list.show()


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(40)
stack.show()
stack.pop()
stack.push(50)
stack.show()
stack.pop()
stack.pop()
stack.pop()


