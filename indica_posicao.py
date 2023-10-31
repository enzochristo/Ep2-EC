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

print(indica_posicao('Beatriz','Beatriz'))
