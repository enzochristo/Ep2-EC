import random
def inicializa(l):
    especuladas = []
    n = len(l[0])
    tentativas = n+1
    sorteada = random.choice(l)
    d = {'n':n ,'sorteada':sorteada, 'especuladas': especuladas, 'tentativas' : tentativas }
    return d