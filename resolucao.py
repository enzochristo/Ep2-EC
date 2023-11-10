from backend import palavras_filtradas,palavra_sorteada,coloracao,indica_posicao,d_sorteada,ajuda,inicializa
import time
print(' ============================='
'\n|                            |'
'\n| Bem-vindo ao Insper Termo  |'
'\n|                            |'
'\n===== Design de Software =====')
print('Comandos: \n .Para sair do jogo digite "desisto" ou algo que remeta a sair do jogo(Ex:''nao'',''sair'',''cansei'',''acabou'')\n .Para afirmar algo durante a jogatina, digite algo que remeta ao afirmativo(Ex:''sim'',''positivo'',''ss'',''s'')')
print('Regras:'
'\n- Você tem \033[94m6\033[0m tentativas para acertar uma palavra aleatória de 5 letras.'
'\n- A cada tentativa, a palavra testada terá suas letras coloridas conforme:'
'\n. \033[92mVerde\033[0m: a letra está na posição correta;'
'\n. \033[93mAmarelo\033[0m: a palavra tem a letra, mas está na posição errada;'
'\n. \033[91mVermelho\033[0m: a palavra não tem a letra.'
'\n- Os acentos são ignorados;'
'\n- Não se preocupe com espaços logo antes das palavras(Ex: amora(com espaço antes do ''a''), Ex2:amora(sem espaço antes do ''a''))'
'\n- Não se preocupe com letras maiúsculas'
'\n- As palavras podem possuir letras repetidas.'
f'\nCaso esteja sem ideias para palavras de 5 letras, aparecerá uma lista com dez palavras aleatorias que se renovarão a cada rodada em cima do termo \033[94m;)\033[0m')

lista_s = ['s','sss','certeza','com certeza','ss','sssssss','ssss','sim', 'positivo','simm','siiim','siim']
w = 0
i = 0
continuar = True
lpc = [' ']*30
d_tentativas = {1 : '\033[94mprimeira\033[0m' , 2: '\033[92msegunda\033[0m', 3: '\033[92mterceira\033[0m', 4: '\033[93mquarta\033[0m', 5: '\033[93mquinta\033[0m', 6: '\033[91msexta\033[0m'}

while continuar:
    lista_ajuda = ajuda(palavras_filtradas)
    tentativas = d_sorteada['tentativas']
    especulada = d_sorteada['especuladas']
    if palavra_sorteada != '':
        if w == 0 :
            print('\n\nEstou sorteando uma palavra...')
            time.sleep(1)
            print('Já tenho uma palavra! Adivinhe-a, você consegue!')
        w = 1
    if tentativas > 1 :
        time.sleep(.5)
        print(f'Você tem {tentativas} tentativas')
    if tentativas  == 1:
        time.sleep(.5) 
        print((f'Você tem {tentativas} tentativa'))

    palavra_escolhida = input('Qual seu palpite ?').strip().lower()

    if palavra_escolhida in ['desisto','nao','cansei','parar','quit','sair','desistir']:
        final = input('Tem certeza que deseja sair? ').strip().lower()
        if final in lista_s:
            print(f'Que pena! a palavra sorteada era "{palavra_sorteada}"')
            w = 0
            i = 0
            continuar = input('Gostaria de jogar outra vez ? ') in lista_s
            if continuar:
                d_sorteada = inicializa(palavras_filtradas)
                palavra_sorteada = d_sorteada['sorteada']
                lpc = ['  '] * 30
                lista_ajuda = ajuda(palavras_filtradas)
                continuar
            else:
                time.sleep(.3)
                print('Até a proxima \033[94m:)\033[0m')
                break

    elif len(palavra_escolhida) != 5:
        print('Apenas palavras com 5 letras')

    elif palavra_escolhida not in palavras_filtradas:
        print('Palavra desconhecida')

    elif palavra_escolhida in especulada:
        print('Palavra já testada!')

    else:
        lista_de_numeros = indica_posicao(palavra_sorteada,palavra_escolhida)
        cor = coloracao(lista_de_numeros,palavra_escolhida)
        d_sorteada['tentativas'] -= 1
        tentativas = d_sorteada['tentativas']
        especulada.append(palavra_escolhida)
        for j in range(len(cor)):
            lpc.insert(i,cor[j])
            i += 1    
        print('\033[94mINSPER:: TERMO\033[0m ')
        print(f'Caso precise de ideias aqui estão algumas: {lista_ajuda}'' \033[94m;)\033[0m')
        print(
        '\t --- --- --- --- ---' 
        f'\n\t| {lpc[0]} | {lpc[1]} | {lpc[2]} | {lpc[3]} | {lpc[4]} |'
        '\n\t --- --- --- --- ---'
        f'\n\t| {lpc[5]} | {lpc[6]} | {lpc[7]} | {lpc[8]} | {lpc[9]} |'
        '\n\t --- --- --- --- ---'
        f'\n\t| {lpc[10]} | {lpc[11]} | {lpc[12]} | {lpc[13]} | {lpc[14]} |'
        '\n\t --- --- --- --- --- '
        f'\n\t| {lpc[15]} | {lpc[16]} | {lpc[17]} | {lpc[18]} | {lpc[19]} |'
       '\n\t --- --- --- --- --- '
        f'\n\t| {lpc[20]} | {lpc[21]} | {lpc[22]} | {lpc[23]} | {lpc[24]} |'
       '\n\t --- --- --- --- --- '
        f'\n\t| {lpc[25]} | {lpc[26]} | {lpc[27]} | {lpc[28]} | {lpc[29]} |'
        '\n\t --- --- --- --- --- ')

        if palavra_escolhida == palavra_sorteada:
            w = 0
            i = 0
            tent_acert = 6 - tentativas
            print(f'Uau!! Você acertou! Parabens!! \nVocê acertou na {d_tentativas[tent_acert]} tentativa ')
            time.sleep(.1)
            continuar = input('Gostaria de jogar novamente ? ').strip().lower() in lista_s
            if continuar:
                d_sorteada = inicializa(palavras_filtradas)
                palavra_sorteada = d_sorteada['sorteada']
                lpc = [''] * 30
                lista_ajuda = ajuda(palavras_filtradas)
                continuar
            else:
                print('Até a proxima \033[94m:)\033[0m')
                continuar = False
        elif tentativas == 0:
            w = 0
            i = 0
            print(f'Não foi dessa vez, sinto muito :(\nMas por curiosidade, a palavra sorteada era "{palavra_sorteada}"')
            continuar = input('Gostaria de jogar outra vez ? ').strip().lower() in lista_s
            if continuar:
                d_sorteada = inicializa(palavras_filtradas)
                palavra_sorteada = d_sorteada['sorteada']
                lpc = ['']*30
                lista_ajuda = ajuda(palavras_filtradas)
                continuar
            else:
                print('Até a proxima \033[94m:]\033[0m')
                continuar = False
                
        

        
