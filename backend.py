
import random
import Palavras
palavras_port = Palavras.PALAVRAS


def filtra(l,n):
    lista = []
    for i in range(len(l)):
      if len(l[i]) == n:
         menor = l[i].lower()
         if menor not in lista:
            lista.append(menor)
    return lista


def inicializa(l):
    especuladas = []
    n = len(l[0])
    tentativas = n+1
    sorteada = random.choice(l)
    d = {'n':n ,'sorteada':sorteada, 'especuladas': especuladas, 'tentativas' : tentativas }
    return d

def indica_posicao(psort,pesp):
    lista = []
    if len(psort)!= len(pesp):
        return lista
    else:  
        for i in range(len(psort)):
            menor_esp = pesp.lower()
            menor_sort = psort.lower()
            if menor_sort[i] == menor_esp[i]:
                lista.append(0)
            elif menor_esp[i] in menor_sort :
                lista.append(1)
            else: 
                lista.append(2)
    return lista

def coloracao(ln,pe):
    lista = []
    for i in range(5):
        if ln[i] == 0:
            letra_v = '\033[92m' + pe[i] + '\033[0m' # cor verde
            lista.append(letra_v)
        elif ln[i] == 1:
            letra_a= "\033[93m" + pe[i] + '\033[0m'#cor amarela
            lista.append(letra_a)
        else:
            letra_r =  '\033[91m' + pe[i] + '\033[0m' #cor vermelha
            lista.append(letra_r)

    return lista

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


palavras_filtradas = filtra(palavras_port,5)
d_sorteada = inicializa(palavras_filtradas)
palavra_sorteada = d_sorteada['sorteada']
#cor = coloracao(lista_numeros,palavra_escolhida)


def ajuda(pf):
    lista_aux = []
    help = ''
    pf = palavras_filtradas
    x = 0
    while x < 11 :
        w = random.randint(10,5000)
        lista_aux.append(pf[w])
        x+=1
        if x == 10:
            help = ', '.join(lista_aux)
            help = help[:-1]
            return help


        


    




        


