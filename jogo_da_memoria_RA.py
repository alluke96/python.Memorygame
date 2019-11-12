#Isabela Montingelli
#Victor Lamers
#Allyson Dunke
#Matheus Heisler
#Lucas Schermak

import random #usado para o Shuffle
#import Jesus as Cristo #sem ele nao seria possivel
import time #usado para dar uma pausa para ver a resposta por determinado tempo

def limpaTela(): #pula 100 linhas
    print('\n'*100)

def chutes(): #escolha das cartas
        print("========PRIMEIRA CARTA========")
        a = int(input('Digite o numero da linha: ')) - 1 # -1 para tornar o jogo mais amigavel ao usuario, começando do 1 ao inves do 0
        b = int(input('Digite o numero da coluna: ')) - 1
        mostra_board((a, b))
        print("========SEGUNDA CARTA========")
        x = int(input('Digite o numero da linha: ')) - 1
        y = int(input('Digite o numero da coluna: ')) - 1
        mostra_board((a, b),(x, y))
        if segredo[a][b] == segredo[x][y]: #descobre se acertou
            print('Acertou!')
            time.sleep(2) #aguarda 2 segundos antes de continuar
            print('\n' *2)
            board[a][b] = segredo[a][b] #continua exibindo as cartas acertadas
            board[x][y] = segredo[x][y]
        else: #se nao acertou, errou
            print('Errou!')
            time.sleep(2)
            limpaTela()
        if any('▓' in l for l in board): #procura em toda a board(matriz) se há ▓
            return True #encerra o jogo

def mostra_board(*tiles): #desempacota os tiles (funcao especifica do python)
    for linha in range(len(segredo)):
        for coluna in range(len(segredo[linha])):
            if (linha, coluna) in tiles:
                print(segredo[linha][coluna], end='')
            else:
                print(board[linha][coluna], end='')
        print()

# ganhou = False
dif = int(input("Digite a dificuldade desejada (1 - Facil / 2 - Medio / 3 - Dificil): ")) #escolha de dificuldade
if dif == 1:
    segredo = list('֍֍ֆֆՋՋ֏֏')
    random.shuffle(segredo) #escolhe aleatoriamente entre os pares do segredo
    board = [list('▓'*2) for i in range(4)] #4 col 2 lin
    segredo = [segredo[:2],
         segredo[2:4],
         segredo[4:6],
         segredo[6:]]
elif dif == 2:
    segredo = list('֍֍ֆֆῼῼᴪᴪ‡‡☻☻☼☼ꞶꞶ')
    random.shuffle(segredo) #escolhe aleatoriamente entre os pares do segredo
    board = [list('▓'*4) for i in range(4)] #4 col 4 lin
    segredo = [segredo[:4],
         segredo[4:8],
         segredo[8:12],
         segredo[12:]]
elif dif == 3:
    segredo = list('֍֍ֆֆՋՋ֏֏ևևᴥᴥῼῼᴪᴪ‡‡☻☻☼☼ꞶꞶᴫᴫὠὠᴧᴧ')
    random.shuffle(segredo) #escolhe aleatoriamente entre os pares do segredo
    board = [list('▓'*6) for i in range(5)] #6 col 5 lin
    segredo = [segredo[:6],
         segredo[6:12],
         segredo[12:18],
         segredo[18: 24],
         segredo[24:]]
else:
    exit("Dificuldade inválida")

mostra_board()

while chutes(): #enquanto o jogador nao ganhar, ele continua tentando
    pass #controle de fluxo (tapa buraco)

exit("PARABANHOS ☻☻☻☻!") #fim de jogo (vitoria)
