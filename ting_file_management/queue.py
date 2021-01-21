class Queue:

    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__data = ()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__data.insert(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.__data.pop()

    def search(self, index):
        """Aqui irá sua implementação"""

        try:
            if index <= 0 or len(self) <= -1:
                return None
        except IndexError:
            return "indice invalido"
        else:
            for i in index:
                return index[i]
