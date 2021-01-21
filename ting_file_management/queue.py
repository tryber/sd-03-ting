from deque import Deque


class Queue:
    def __init__(self):
        self._deque = Deque()

    def __len__(self):
        return len(self._deque)

    def enqueue(self, value):
        self._deque.push_back(value)

    def dequeue(self):
        return self._deque.pop_front()

    def search(self, index):
        """Aqui irá sua implementação"""
