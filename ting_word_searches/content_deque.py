class Deque:
    FIRST_ELEMENT = 0

    def __init__(self, value=[], max_size=10):
        self._data = [*value]
        self._max_size = max_size

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return "Deque(" + ", ".join(str(x) for x in self._data) + ")"

    def __check_deck_length_push(self):
        if len(self._data) + 1 > self._max_size:
            print(f'size: {len(self._data)}')
            print(f'maxsize: {self._max_size}')
            raise Exception('Overflow')

    def __check_deck_length_pop(self):
        if len(self._data) - 1 < 0:
            print(f'size: {len(self._data)}')
            raise Exception('No data')

    def push_front(self, value):
        self.__check_deck_length_push()
        self._data.insert(self.FIRST_ELEMENT, value)

    def push_back(self, value):
        self.__check_deck_length_push()
        self._data.append(value)

    def pop_front(self):
        self.__check_deck_length_pop()
        return self._data.pop(self.FIRST_ELEMENT)

    def pop_back(self):
        self.__check_deck_length_pop()
        return self._data.pop()

    def peek_front(self):
        if self._data:
            return self._data[self.FIRST_ELEMENT]
        return None

    def peek_back(self):
        if self._data:
            return self._data[len(self)-1]
        return None

    def clear(self):
        if(len(self._data > 0)):
            self._data.clear()

    def exists(self, value):
        if value in self._data:
            return True
        return False

    def peek(self, position, order=""):
        if not order or order == "front":
            return self._data[position]
        position = (position * -1) - 1
        return self._data[position]
