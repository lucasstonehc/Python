class Queue(object):

	def __init__(self, length):
		self.length = length
		self.vector = [0] * self.length
		self.head = 0
		self.tail = 0

	def insert(self, element):
		if self.isEmpty():
			self.vector[self.tail] = element
			self.tail += 1
		else:
			print("Queue is fully")

	def remove(self):
		x_head = 0
		if self.tail!= 0:
			x_head = self.vector[self.head]
			self.vector[self.head] = 0
			self.head+=1
		else:
			print("Queue is Empty")
		return x_head

	def isEmpty(self):
		if self.tail <= self.length - 1:
			return True
		else:
			return False

	def show(self):
		 print(self.vector)


class Stack(object):

	def __init__(self, length):
		self.queue_one = Queue(length)
		self.queue_two = Queue(length)
		

queue = Queue(10)

queue.insert(2)
queue.insert(3)
queue.insert(5)
queue.show()
queue.remove()
queue.show()




