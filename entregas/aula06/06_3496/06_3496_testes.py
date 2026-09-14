import unittest

PilhaEncadeada = __import__("06_3496_pilha_encadeada").PilhaEncadeada
FilaEncadeada = __import__("06_3496_fila_encadeada").FilaEncadeada

class Testes(unittest.TestCase):
    def test_pilha(self):
        p = PilhaEncadeada()
        self.assertRaises(IndexError, p.pop)
        self.assertRaises(IndexError, p.topo)
        
        # Testando tipos diferentes, None e repetidos num loop
        for item in [1, None, "A", "A"]:
            p.push(item)
            
        self.assertEqual(len(p), 4)
        self.assertEqual([p.pop() for _ in range(4)], ["A", "A", None, 1])
        self.assertEqual(len(p), 0)
        p.push(10)
        self.assertEqual(p.pop(), 10)

    def test_fila(self):
        f = FilaEncadeada()
        self.assertRaises(IndexError, f.desenfileirar)
        self.assertRaises(IndexError, f.frente)
        
        f.enfileirar(1)
        f.enfileirar(2)
        self.assertEqual(f.desenfileirar(), 1)
        f.enfileirar(3)
        self.assertEqual(len(f), 2)
        self.assertEqual([f.desenfileirar(), f.desenfileirar()], [2, 3])
        self.assertEqual(len(f), 0)   
        f.enfileirar(4)
        self.assertEqual(f.desenfileirar(), 4)

if __name__ == "__main__":
    unittest.main()