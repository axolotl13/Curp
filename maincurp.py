from datetime import date
from unicodedata import normalize
from consonantes import iniciales, consonantex
from renapo import entidades, antisonantes, preposiciones
from digitoverificador import getValor


class generarCurp:
    def __init__(self, nombre, apellidopaterno, apellidomaterno, dia, mes, año, estado, sexo):
        self.nombre = nombre
        self.apellidopaterno = apellidopaterno
        self.apellidomaterno = apellidomaterno
        self.dia = dia
        self.mes = mes
        self.año = año
        self.estado = estado
        self.sexo = sexo

    # Reemplaza la consonante ñ por x, limpia las tildes y transforma los datos a mayusculas
    def limpiar(self):
        datos, lista_limpia = [self.nombre, self.apellidopaterno, self.apellidomaterno, self.estado, self.sexo], []
        for dato in datos:
            lista_limpia.append(normalize("NFKD", dato.upper().replace("Ñ", "X")).encode("ascii","ignore").decode("ascii"))
        return lista_limpia

    # Elimina preposiciones, descompone nombres y apellidos compuestos
    def datos(self):
        name = self.limpiar()[0]
        firstname = self.limpiar()[1]
        lastname = self.limpiar()[2]
        compuestos, normalizar, datos_limpios = [name, firstname, lastname], [], [[], [], []]
        for separar in compuestos:
            normalizar.append(separar.split())
        for filtrar in range(len(normalizar)):
            for eliminar in normalizar[filtrar]:
                if eliminar in preposiciones:
                    pass
                else:
                    datos_limpios[filtrar].append(eliminar)
        if len(datos_limpios[0]) > 1:
            if datos_limpios[0][0] in ["MARIA", "JOSE"]:
                datos_limpios[0] = [datos_limpios[0][1]]
            else:
                datos_limpios[0] = [datos_limpios[0][0]]
        else:
            pass
        if len(datos_limpios[1]) > 1:
            datos_limpios[1] = [datos_limpios[1][0]]
        else:
            pass
        return datos_limpios

    # Validar fecha
    def fecha(self):
        try:
            day = self.dia
            month = self.mes
            year = self.año
            dates = date(int(year), int(month), int(day))
            return dates.strftime("%y" + "%m" + "%d")
        except Exception as ex:
            return ex

    # Calcular Siglo
    def siglo(self):
        year = int(self.año)
        if year in range(1901, 2001):
            return "0"
        elif year in range(2001, 2101):
            return "1"
        else:
            return None

    # Comprueba si el sexo es valido
    def sex(self):
        sexo = self.limpiar()[4]
        if sexo in ["MUJER", "FEMENINO", "M"]:
            return "M"
        elif sexo in ["HOMBRE", "MASCULINO", "H"]:
            return "H"
        else:
            return None

    # Entidades segun Renapo
    def estados(self):
        return entidades.get(self.limpiar()[3])

    # Genera el curp
    def getCurp(self):
        nombre = self.datos()[0][0]
        primerapellido = self.datos()[1][0]
        segundoapellido = self.datos()[2][0]
        fecha = self.fecha()
        datos = [iniciales(primerapellido), segundoapellido[0], nombre[0]]
        datos = "".join(datos)
        if antisonantes.get(datos):
            datos = antisonantes.get(datos)
        else:
            pass
        curp = [datos, fecha, self.sex(), self.estados(), consonantex(primerapellido, segundoapellido, nombre), self.siglo(), "0"]
        return "".join(curp)

    # Calcula el ultimo digito
    def validar(self):
        return getValor(self.getCurp())

    # Imprimir
    def imprimir(self):
        print("""\
        + + + + + + + + + + + + + + + + + + + + + +
        +                                         +
        +           """ + self.validar() + """            +
        +                                         +
        + + + + + + + + + + + + + + + + + + + + + +
        """
        "\n\t\t      Nombre:", self.nombre,
        "\n\t\t  Apellido P:", self.apellidopaterno,
        "\n\t\t  Apellido M:", self.apellidomaterno,
        "\n\t\tFecha de Nac:", self.fecha(),
        "\n\t\t        Sexo:", self.sexo,
        "\n\t\t      Estado:", self.estado,
        "\n"
        )


curp1 = generarCurp("Alberto", "Ñando", "Rodriguez", "9", "8", "1999", "Baja California", "Hombre")
curp1.imprimir()

curp2 = generarCurp("Rocio", "Riva Palacio", "Cruz", "10", "9", "2001", "Tlaxcala", "Mujer")
curp2.imprimir()

curp3 = generarCurp("Carlos", "MC Gregor", "Lopez", "1", "11", "1967", "Zacatecas", "Hombre")
curp3.imprimir()

curp4 = generarCurp("Andres", "Ich", "Rodriguez", "25", "06", "2009", "Yucatan", "Hombre")
curp4.imprimir()

curp5 = generarCurp("Ofelia", "Pedrero", "Dominguez", "01", "01", "1981", "Nuevo Leon", "Mujer")
curp5.imprimir()
