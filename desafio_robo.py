lin = 4
col = 4
matriz = [ # o S indica a saída
    ['R', '#', '#', '#'],
    ['-', '-', '-', '#'],
    ['#', '#', '-', '#'],
    ['S', '-', '-', '#']
]

def imprimirMatriz():
    for i in range(0,lin):
        
        for j in range(0,col):    
            print(f"[{matriz[i][j]}]", end="")
        print("")    
    print("")
            

def busca(l, c):
    if (l >= lin or c >= col or l < 0 or c < 0 or #Posições inválidas
        matriz[l][c] == "*" or matriz[l][c] == "R" or matriz[l][c] == "#"):
        return 0
    
    if matriz[l][c] == 'S': # achou a saída
        matriz[l][c] = '*'
        return 1
    
    if matriz[l][c] != '#': #marca o caminho
        matriz[l][c] = '*'
        imprimirMatriz()    
    
    if(busca(l, c + 1) or busca(l + 1, c) or busca(l, c - 1) or busca(l -1, c)):
        return 1
        
        
if(busca(0, 1) or busca(1, 0)): # direita ou baixo
    print('Caminho encontrado!')
    imprimirMatriz()
else:
    print('Caminho não encontrado: ')
    imprimirMatriz()


