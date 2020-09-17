# Curp
### Generador de CURP mexicano en Python

Si la letra inicial de alguno de los apellidos o del nombre es **Ñ**, el sistema asignará una **"X"** en su lugar.

```
Ejemplo: ALBERTO ÑANDO RODRIGUEZ  > XARA
```

Cuando el nombre sea compuesto, la clave se construye con la **letra inicial** de la primera palabra, siempre que no sea **MARIA**, MA., MA, o **JOSE**, J, J. en
cuyo caso se utilizará la segunda palabra.

```
Ejemplos: MARIA LUISA PEREZ HERNANDEZ > PEHL
LUIS ENRIQUE ROMERO PALAZUELOS > ROPL
```

*Apellidos compuestos*, formados por más de una palabra, la clave se conformará con la primera palabra del apellido.

```
Ejemplo: ROCIO RIVA PALACIO CRUZ > RICR
```

Cuando alguno de los apellidos o nombre es compuesto y la primera palabra de esta composición es una *preposición*, *conjunción*, *contracción*. La aplicación elimina la primera palabra y utiliza la siguiente del apellido o nombre.

```
Ejemplo: CARLOS MC GREGOR LOPEZ > GELC
```

Si de las cuatro letras resulta una *palabra altisonante*. La segunda letra será sustituida por una **“X”**.

```
Ejemplo: OFELIA PEDRERO DOMINGUEZ > PXDO
```

Con dos apellidos, si el primer apellido no tiene *vocal interna*. Para la construcción de la CURP el sistema asignará una **"X"** en la segunda posición.

```
Ejemplo: ANDRES ICH RODRÍGUEZ > IXRA
```

Con un apellido, si no existe segundo apellido. El sistema asignará una **“X”** en la tercera posición.
**<u>Marcara error, es facíl solucionarlo, en algun futuro se hará si es que tengo tiempo</u>**

Cuando la primera consonante interna es la letra **Ñ**. El sistema asignará una **“X”**.

```
Ejemplo: ALBERTO OÑATE RODRIGUEZ > XDL
```

Cuando no existen consonantes internas en nombre o apellido.  El sistema asignará una **“X”** en la posición correspondiente.
<u>**Marcara error, igual, la solución es facíl pero ahora no tengo tiempo**</u>

Con un sólo apellido.
<u>**Marcara error, igual, la solución es facíl pero ahora no tengo tiempo**</u>

Cuando el nombre sea compuesto (formado por dos o más palabras), la clave se construye con la primera consonante interna del primer nombre, siempre y cuando no sea María o José, en cuyo caso se utilizará el segundo nombre.

```
Ejemplo: MA. DE LOS ANGELES MORENO SANCHEZ > RNN
```


