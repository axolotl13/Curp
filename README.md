# CURP

INSTRUCTIVO NORMATIVO PARA LA ASIGNACIÓN DE LA CLAVE ÚNICA DE REGISTRO DE POBLACIÓN

## Descripción

La Clave Única de Registro de Población es un instrumento que permite registrar
en forma individual a todas las personas que residen en el territorio nacional,
así como a los mexicanos que radican en el extranjero.

### Criterios de excepción

- [x] Si la letra inicial de alguno de los apellidos o del nombre es **Ñ**, el sistema
      asignará una **"X"** en su lugar.

        Ejemplo: ALBERTO ÑANDO RODRIGUEZ        >       XARA

- [x] Cuando el nombre sea compuesto(formado por dos o más palabras), la clave se
      construye con la **letra inicial** de la primera palabra, siempre que no
      sea **MARIA**, MA., MA, o **JOSE**, J, J. en cuyo caso se utilizará la
      segunda palabra.

        Ejemplos: MARIA LUISA PEREZ HERNANDEZ   >       PEHL
        LUIS ENRIQUE ROMERO PALAZUELOS          >       ROPL

- [x] Si en los apellidos o en el nombre aparecieran caracteres especiales como
      diagonal (**/**), guión (**-**), o punto (**.**), se captura tal cual viene
      en el documento probatorio y la aplicación asignará una **"X"** en caso de
      que esa posición intervenga para la conformación de la clave.

        Ejemplo: JUAN JOSE D/AMICO ALVAREZ      >       DXAJ

- [x] Apellidos compuestos, formados por más de una palabra, la clave se
      conformará con la primera palabra del apellido.

        Ejemplo: ROCIO RIVA PALACIO CRUZ        >       RICR

- [x] Cuando alguno de los apellidos o nombre es compuesto y la primera palabra
      de esta composición es una preposición, conjunción, contracción **(DA, DAS,
      DE, DEL, DER, DI, DIE, DD, EL, LA, LOS, LAS, LE, LES, MAC, MC, VAN, VON, Y).**
      La aplicación elimina la primera palabra y utiliza la siguiente del
      apellido o nombre.

        Ejemplo: CARLOS MC GREGOR LOPEZ         >       GELC

- [x] Si de las cuatro letras resulta una palabra altisonante (Ver
      ANEXO 2). La segunda letra será sustituida por una “X”.

        Ejemplo: OFELIA PEDRERO DOMINGUEZ       >       PXDO

  -[x] Con dos apellidos, si el primer apellido no tiene vocal interna.
  Para la construcción de la CURP el sistema asignará una "X" en la
  segunda posición.

        Ejemplo: ANDRES ICH RODRÍGUEZ           >       IXRA

-[x] Con un apellido, si no existe segundo apellido. El sistema
asignará una “X” en la tercera posición.

        Ejemplo: LUIS PEREZ                     >       PEXL

### Instalar dependencias

```bash
pip install -r requirements.txt
```
Ejecutar **main**

```bash
python3 main.py
```
