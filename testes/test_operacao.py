"""Seus testes do Marco 3 (veja a seção 5 do ENUNCIADO_MARCO3.md).

Regras: pelo menos 4 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou math.isclose, a não
ser que a igualdade exata seja justamente o que você quer testar.
"""
import unittest
import math

from elevatoria.raizes import Bisseccao, Newton
from elevatoria.operacao import ordem_convergencia, ponto_operacao


class TestBisseccaoExemplo(unittest.TestCase):
    """Exemplo do formato. `Bisseccao` é código existente da base."""

    def test_raiz_na_ponta(self):
        """Se f(a) já é zero, a bissecção devolve a sem iterar."""
        resultado = Bisseccao().encontrar(lambda x: x - 1.0, 1.0, 3.0)
        self.assertEqual((resultado.raiz, resultado.iteracoes), (1.0, 0))


class TestRegressaoNewton(unittest.TestCase):
    """Testes de regressão para a issue #9."""

    def test_newton_iteracoes_rapidas(self):
        """Newton deve resolver f(x) = x**2 - 4 em poucas iterações (<= 7) com convergência rápida."""
        resultado = Newton().encontrar(lambda x: x**2 - 4.0, 1.0, 5.0)
        self.assertLessEqual(resultado.iteracoes, 7)

    def test_newton_convergencia_quadratica(self):
        """A ordem de convergência do Newton deve ser próxima de 2 (quadrática)."""
        resultado = Newton().encontrar(lambda x: x**2 - 4.0, 1.0, 5.0)
        p = ordem_convergencia(resultado.historico, resultado.raiz)
        self.assertGreater(p, 1.8)


class TestContratoOperacao(unittest.TestCase):
    """Testes de contrato para as funções da issue #8."""

    def test_ordem_convergencia_poucos_erros(self):
        """Levanta ValueError se houver menos de 3 erros significativos acima do piso."""
        historico = [2.5, 2.00000000000001, 2.0]
        with self.assertRaises(ValueError):
            ordem_convergencia(historico, raiz=2.0)

    def test_ponto_operacao_intervalo_invalido(self):
        """Levanta ValueError imediatamente se a >= b."""
        with self.assertRaises(ValueError):
            ponto_operacao(None, None, None, a=100.0, b=10.0)


if __name__ == "__main__":
    unittest.main()