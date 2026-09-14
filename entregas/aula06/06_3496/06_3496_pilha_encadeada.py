class _No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def push(self, item):
        novo_no = _No(item)
        novo_no.proximo = self._topo
        self._topo = novo_no
        self._tamanho += 1

    def pop(self):
        if self.esta_vazia():
            raise IndexError()
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self._tamanho -= 1
        return valor

    def topo(self):
        if self.esta_vazia():
            raise IndexError()
        return self._topo.valor

    def esta_vazia(self):
        return self._topo is None

    def __len__(self):
        return self._tamanho

    def __repr__(self):
        if self.esta_vazia():
            return "Pilha(Vazia)"
        resultado = "Pilha(Topo"
        atual = self._topo
        while atual:
            resultado += f" -> {repr(atual.valor)}"
            atual = atual.proximo
        resultado += ")"
        return resultado