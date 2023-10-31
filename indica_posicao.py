def indica_posicao(psort,pesp):
    lista = []
    if len(psort)!= len(pesp):
        return lista
    else:  
        for i in range(len(psort)):
            if psort[i] == pesp[i]:
                lista.append(0)
            elif pesp[i] in psort :
                lista.append(1)
            else: 
                lista.append(2)
    return lista

print(indica_posicao('bolem','Marco'))
