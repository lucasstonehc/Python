'''
Uma pilha permite a inserção e remoção de elementos em apenas uma de suas pontas. 
Um fila permite a inserção em uma ponta, e a remoção em outra. Uma fila duplamente terminada (ou Deque) permite a inserção e remoção nas duas pontas.
Implemente uma fila duplamente terminada e assugere-se de fornecer quatro procedimentos com complexidade temporal de O(1)
para inserir e remover elementos das duas pontas da fila. Essa fila deve ser implementada utilizando um vetor de tamanho fixo.
'''
import math

class Queue(objetc):


	def __init__(self, length):
		self.vector = [] * self.length
		self.head = math.ceil(self.length/2)
		self.tail = math.ceil(self.length/2) 

	def insert_begin():
	def insert_end():
	def remove_begin():
	def remove_end():
