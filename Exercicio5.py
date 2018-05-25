class Stack(object):
    def __init__(self, length):
        self.length = length
        self.vector = [None] * self.length
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1
    
    def isFully(self):
        return self.top == self.length-1
    
    def push(self, element):
        if not self.isFully():
            self.top += 1
            self.vector[self.top] = element
        else:
            raise Exception('stack is fully')
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.vector[self.top+1]
        else:
            raise Exception('stack is empty')


class Queue(object):

    def __init__(self, lenght):
        self.stack_one = Stack(lenght)
        self.stack_two = Stack(lenght)

    def insert(self, element):
        self.stack_one.push(element)

    def remove(self):
        while self.stack_one.top != -1:
            self.stack_two.push(self.stack_one.pop())

        aux  = self.stack_two.pop()
        print(aux)

        while self.stack_two.top != -1:
            self.stack_one.push(self.stack_two.pop())

        return aux


q = Queue(4)
q.insert(0)
q.insert(0)
q.insert(0)
q.insert(0)

q.remove()
q.remove()
q.remove()
q.remove()




