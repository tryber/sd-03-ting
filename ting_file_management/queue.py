class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)
        return self.queue

    def dequeue(self):
        [first, *rest] = self.queue
        self.queue = rest
        return first

    def search(self, index):
        if index < 0 or index >= len(self.queue):
            raise IndexError('list index out of range')
        else:
            return self.queue[index]
