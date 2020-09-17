abecedario = '0123456789ABCDEFGHIJKLMN~OPQRSTUVWXYZ'
lista = list(abecedario)


def getValor(xur):
    curp = list(xur)
    curp.reverse()
    caracteres, resultado, suma = [], 0, 0
    for valor in curp:
        for item in range(len(lista)):
            if valor == lista[item]:
                caracteres.append(item)
    for i in range(len(curp)):
        resultado = (i + 1) * caracteres[i]
        #print(curp[i], "=", i + 1 , "x", valor[i], "=", resultado)
        suma = suma + resultado
    resultado = ((suma%10)-10)*-1
    if resultado == 10:
        resultado = 0
    else:
        pass
    curp.reverse()
    curp.pop(-1)
    curp.append(str(resultado))
    return "".join(curp)

