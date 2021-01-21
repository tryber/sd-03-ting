class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__data = []

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        for i in value:
            self.__data.append(i)

    def dequeue(self):
        """Aqui irá sua implementação"""

    def search(self, index):
        """Aqui irá sua implementação"""
