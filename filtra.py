def filtra(l,n):
    lista = []
    for i in range(len(l)):
      if len(l[i]) == n:
         menor = l[i].lower()
         if menor not in lista:
            lista.append(menor)
    return lista

print(filtra(['Texto', 'Apelo', 'historia', 'ruina', 'caMelO', 'rUiNa'],5))