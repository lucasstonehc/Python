'''
Implemente uma lista encadeada circular com sentinela
'''

class Node(object):

	def __init__(self):
		self.key = None
		self.prev = None
		self.next = None


class LinkedList(object):

	def __init__(self):
		self.setinel = Node()
		self.head = self.setinel	
		self.tail = self.setinel

	def isEmpty(self):
		if self.head.next == None and self.tail.prev == None:
			return True
		else:
			return False

	def insert(self, element):
		node = Node()
		node.key = element

		if self.isEmpty():
			self.tail.next = node
			self.tail = node
			self.tail.prev = self.setinel
			self.tail.next = self.setinel
			self.head.prev = node
		else:
			self.tail.next = node
			self.tail.next.prev = self.tail
			self.tail = node
			self.head.prev = node
			self.tail.next = self.setinel

	def remove(self, key):

		return 0

	def show(self):
		aux = self.setinel.next
		while aux != self.setinel:
			print(aux.key)
			aux = aux.next	

	def find(self, key):
		aux = self.setinel.next
		find = False
		while aux != self.setinel:
			if aux.key == key:
				find = True
				break
			aux = aux.next	
		if find:
			return print(aux.key)
		else:
			return print("Element not found")

li = LinkedList()
li.insert(10)
li.insert(20)
li.insert(40)
li.insert(50)
li.insert(60)
li.insert(70)

li.show()

li.find(400)




