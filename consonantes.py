vocales = ['A', 'E', 'I' ,'O' ,'U']

def iniciales(firstname):
    apellido = firstname
    iniciales, consonante, x,  = [], [], 0
    for i in range(len(apellido)):
        if i < 1:
            iniciales.append(apellido[i])
        if i >= 1:
            consonante.append(apellido[i])
    for i in consonante:
        if i in vocales:
            if x == 0:
                iniciales.append(i)
                x = x + 1
    if len(iniciales) <= 1:
        iniciales.append("X")
    return "".join(iniciales)

def consonantex(firstname, lastname, name):
    datos = [firstname, lastname, name]
    csc, abj = [[], [], []], []
    for i in range(len(datos)):
        for j in range(len(datos[i])):
            if j >= 1:
                if datos[i][j] not in vocales:
                    csc[i].append(datos[i][j])
    for i in range(len(datos)):
        abj.append(csc[i][0])
    return "".join(abj)

