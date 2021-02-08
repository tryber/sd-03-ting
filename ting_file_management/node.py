class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        self.prev = None
        self.value = None
        self.next = None

    def __str__(self):
        return str(f"{self.value=} {self.next=}")

    def copy(self):
        return self.value
      