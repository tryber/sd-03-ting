from collections.abc import Iterator


class QueueIterator(Iterator):
    def __init__(self, iterable):
        self.iterable = iterable
        self.position = iterable.head

    def __next__(self):
        if self.position:
            result = self.position
            self.position = self.position.next
            return result
        else:
            raise StopIteration
