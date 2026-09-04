PilhaEncadeada = __import__("06_3496_pilha_encadeada").PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self.pilha_entrada = PilhaEncadeada()
        self.pilha_saida = PilhaEncadeada()

    def _transferir(self):
        if self.pilha_saida.esta_vazia():
            while not self.pilha_entrada.esta_vazia():
                self.pilha_saida.push(self.pilha_entrada.pop())

    def enfileirar(self, item):
        self.pilha_entrada.push(item)

    def desenfileirar(self):
        if self.esta_vazia():
            raise IndexError()
        self._transferir()
        return self.pilha_saida.pop()

    def frente(self):
        if self.esta_vazia():
            raise IndexError()
        self._transferir()
        return self.pilha_saida.topo()

    def esta_vazia(self):
        return self.pilha_entrada.esta_vazia() and self.pilha_saida.esta_vazia()

    def __len__(self):
        return len(self.pilha_entrada) + len(self.pilha_saida)

    def __repr__(self):
        if self.esta_vazia():
            return "Fila(Vazia)"
        elementos = []
        temp = []
        while not self.esta_vazia():
            item = self.desenfileirar()
            elementos.append(repr(item))
            temp.append(item)
        for item in temp:
            self.enfileirar(item)
        return "Fila(Frente -> " + " -> ".join(elementos) + ")"