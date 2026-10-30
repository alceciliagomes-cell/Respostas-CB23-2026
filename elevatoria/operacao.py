"""Ponto de operação da bomba e diagnóstico dos métodos de raiz (issue #8).

Este módulo junta peças que já existem na base:

- `CurvaCalibracao` (de `elevatoria/calibracao.py`, Marco 2): a curva da bomba, interpolada
  a partir do ensaio;
- `Tubulacao` (de `fornecido/hidraulica.py`, da equipe de hidráulica): a curva do sistema;
- `Bisseccao` e `Newton` (de `elevatoria/raizes.py`, escritos por um colega): os métodos de
  raiz, que devolvem um `ResultadoRaiz`.

As funções marcadas com `NotImplementedError` são a issue #8; as docstrings descrevem o
contrato. Não mude nomes nem assinaturas públicas: o `marco3.py` e os testes dependem deles.
Funções auxiliares privadas (`_nome`) são permitidas.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence

from elevatoria.calibracao import CurvaCalibracao
from elevatoria.raizes import MetodoRaiz, ResultadoRaiz
from fornecido.hidraulica import Tubulacao


@dataclass(frozen=True)
class PontoOperacao:
    """O ponto em que a bomba opera: vazão, altura e o resultado do método de raiz."""

    vazao: float              # L/s
    altura: float             # m
    resultado: ResultadoRaiz  # o que o resolvedor devolveu (iterações, histórico...)


def ponto_operacao(bomba: CurvaCalibracao, tubulacao: Tubulacao, resolvedor: MetodoRaiz,
                   a: float = 10.0, b: float = 100.0) -> PontoOperacao:
    if a >= b:
        raise ValueError(f"O intervalo deve ter a < b; recebi [{a}, {b}]")
    
    dom_min, dom_max = bomba.dominio
    if a < dom_min or b > dom_max:
        raise ValueError(f"Intervalo [{a}, {b}] fora do domínio da bomba [{dom_min}, {dom_max}]")
        
    def f(Q: float) -> float:
        return bomba(Q) - tubulacao.altura_sistema(Q)
        
    resultado = resolvedor.encontrar(f, a, b)
    if not resultado.convergiu:
        raise ValueError("O resolvedor não convergiu para o ponto de operação.")
        
    return PontoOperacao(
        vazao=resultado.raiz,
        altura=bomba(resultado.raiz),
        resultado=resultado
    )


def ordem_convergencia(historico: Sequence[float], raiz: float, piso: float = 1e-14) -> float:
    limite = piso * max(1.0, abs(raiz))
    erros = [abs(x - raiz) for x in historico if abs(x - raiz) > limite]
    
    if len(erros) < 3:
        raise ValueError("Menos de 3 erros acima do piso, impossível calcular a ordem.")
        
    e_km1 = erros[-3]
    e_k = erros[-2]
    e_kp1 = erros[-1]
    
    return math.log(e_kp1 / e_k) / math.log(e_k / e_km1)