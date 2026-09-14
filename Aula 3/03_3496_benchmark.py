import time  
import random
import sys
from AP_03_ordenacao import selection_sort, divide_and_conquer_sort, quick_sort
sys.setrecursionlimit(10000)

def caso_medio(n):
    lista = []
    for _ in range(n):
        sorteio = random.randint(1, 10000)
        lista.append(sorteio)
    return lista

def pior_caso(n):
    lista = list(range(n, 0, -1))
    return lista

def medir_tempo(ordenacao, n, repeticao, worst_case = False):
    tempos = []
    for _ in range(repeticao):
        if worst_case == True:
            teste = pior_caso(n)
        else:
            teste = caso_medio(n)

        inicio = time.perf_counter()
        ordenacao(teste)
        fim = time.perf_counter()
        tempo_gasto = fim - inicio
        tempos.append(tempo_gasto)

    media = sum(tempos) / repeticao
    return media

n = [100, 500, 1000, 5000]
repeticao = 50

algoritmos = [
    ("Selection Sort", selection_sort),
    ("Merge Sort", divide_and_conquer_sort),
    ("Quick Sort", quick_sort)
]

print("-" * 65)
print(f"{'Algoritmo':<18} | {'Cenário':<12} | {'N':<6} | {'Tempo Médio (s)'}")
print("-" * 65)

for nome_algoritmo, funcao_algoritmo in algoritmos:
    for k in n:
        tempo_medio = medir_tempo(funcao_algoritmo, k, repeticao, worst_case = False)
        print(f"{nome_algoritmo:<18} | {'Médio':<12} | {k:<6} | {tempo_medio:.6f}")
        
        tempo_pior = medir_tempo(funcao_algoritmo, k, repeticao, worst_case = True)
        print(f"{nome_algoritmo:<18} | {'Pior':<12} | {k:<6} | {tempo_pior:.6f}")

print("-" * 65)