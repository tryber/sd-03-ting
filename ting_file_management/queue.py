class Queue:
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.data = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.data)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.data.insert.first(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.data.remove_first()

    def search(self, index):
        """Aqui irá sua implementação"""
        try:
            for i in index:
                return self[i]

        except EnvironmentError:
            if index != i:
                return "Index Invalido"
