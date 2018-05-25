'''
Similarmente à pilha, uma Fila é um conjunto dinâmico de dados em que a operação REMOVER remove sempre o elemento que está na fila há mais tempo; 
ou seja, a Fila implementa a política FIFO (First In, First Out). Uma fila possui uma cabeça e uma cauda. Quando um elemento é enfileirado, 
ele se posiciona na cauda da fila. O elemento desenfileirado é sempre aquele que está na cabeça da fila.
Implemente uma fila em um vetor de tamanho fixo. Note que, em um vetor de n elementos, você pode guardar no máximo n-1 elementos na fila. 
Sua implementação também deve impedir que aconteça estouro positivo ou negativo na fila.

IFMG-SABARÁ
AEDSIII
Lucas Santos Pimenta Junior
'''

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


queue = Queue(10)

queue.insert(2)
queue.insert(3)
queue.insert(5)
queue.show()
queue.remove()
queue.show()




