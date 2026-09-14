import random

def criar_labirinto():
    lab = []
    for i in range(11):
        linha = []
        for j in range(11):
            linha.append(1)
        lab.append(linha)   
    pilha = [(1, 1)]
    lab[1][1] = 0
    
    while len(pilha) > 0:
        cx, cy = pilha[-1]
        vizinhos = []      
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx = cx + dx
            ny = cy + dy
            if 1 <= nx < 10 and 1 <= ny < 10 and lab[nx][ny] == 1:
                vizinhos.append((nx, ny, dx, dy))
        
        if len(vizinhos) > 0:
            nx, ny, dx, dy = random.choice(vizinhos)
            lab[cx + dx // 2][cy + dy // 2] = 0
            lab[nx][ny] = 0
            pilha.append((nx, ny))
        else:
            pilha.pop()
            
    lab[9][9] = 'Q'
    return lab

def resolver_labirinto(lab):
    pilha = [((1, 1), [(1, 1)])]
    visitados = [(1, 1)]
    
    while len(pilha) > 0:
        pos, caminho = pilha.pop()
        x, y = pos
        
        if lab[x][y] == 'Q':
            return caminho
            
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (nx, ny) not in visitados and lab[nx][ny] != 1:
                visitados.append((nx, ny))
                pilha.append(((nx, ny), caminho + [(nx, ny)]))
    return []

def exibir_labirinto(lab, caminho):
    for i in range(11):
        linha_str = ""
        for j in range(11):
            if (i, j) == (1, 1):
                linha_str += "I "
            elif lab[i][j] == 'Q':
                linha_str += "Q "
            elif (i, j) in caminho:
                linha_str += ". "
            elif lab[i][j] == 1:
                linha_str += "# "
            else:
                linha_str += "  "
        print(linha_str)

if __name__ == "__main__":
    lab = criar_labirinto()
    caminho = resolver_labirinto(lab)
    exibir_labirinto(lab, caminho)
