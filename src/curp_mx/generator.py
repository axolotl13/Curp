"""Generación de la CURP (persona física) a partir de datos personales.

Implementa el algoritmo público de RENAPO: prefijo de 4 letras (Reglas 1-9
del Instructivo Normativo), fecha, sexo, entidad, consonantes internas,
diferenciador de homonimia y dígito verificador.
"""

from dataclasses import dataclass
from datetime import date

from .data import ALPHABET_MX, INAPPROPRIATE_WORDS, STATES
from .utils import (
    get_first_consonant,
    get_first_letter,
    get_first_vowel,
    get_first_word_firstname,
    get_first_word_lastname,
)


@dataclass
class PersonData:
    """Datos personales necesarios para generar una CURP.

    Attributes:
        first_name: Nombre(s) de pila.
        first_surname: Apellido paterno. Puede ir vacío si la persona solo
            tiene un apellido (entonces debe venir en `second_surname`).
        second_surname: Apellido materno. Puede ir vacío bajo la misma
            condición anterior.
        birth_date: Fecha de nacimiento.
        sex: "H" (hombre) o "M" (mujer). No distingue mayúsculas/minúsculas
            ni espacios sobrantes; se normaliza en `__post_init__`.
        state: Clave de 2 letras de la entidad de nacimiento (ej. "JC" para
            Jalisco). Debe existir en el catálogo `STATES`.

    Raises:
        ValueError: si `sex` no es "H"/"M", si `state` no está en `STATES`,
            si `first_name` está vacío, o si no se proporcionó ningún
            apellido.

    """

    first_name: str
    first_surname: str
    second_surname: str
    birth_date: date
    sex: str
    state: str

    def __post_init__(self):
        # Normaliza antes de validar, así "h ", "jc" también son válidos.
        self.sex = self.sex.strip().upper()
        self.state = self.state.strip().upper()
        if self.sex not in {"H", "M"}:
            raise ValueError("Sexo debe ser H o M")
        if self.state not in STATES:
            raise ValueError("Estado inválido")
        if not self.first_name:
            raise ValueError("Nombre vacío")
        if not (self.first_surname or self.second_surname):
            raise ValueError("Se requiere al menos un apellido")


def _clean_fields(data: PersonData) -> tuple[str, str, str]:
    """Extrae la palabra relevante de cada campo, ya limpia de partículas.

    Por ejemplo, de un apellido compuesto como "De la Cruz" se queda solo
    con "CRUZ" (las partículas como "DE"/"LA" no cuentan para el algoritmo).

    Returns:
        Tupla (apellido_paterno, apellido_materno, nombre), cada uno como
        una sola palabra en mayúsculas sin acentos. Cualquiera de los dos
        apellidos puede venir como cadena vacía si la persona solo tiene
        uno (`PersonData` ya garantiza que no sea imposible, ver arriba).

    """
    return (
        get_first_word_lastname(data.first_surname),
        get_first_word_lastname(data.second_surname),
        get_first_word_firstname(data.first_name),
    )


def _build_curp_prefix(first_surname: str, second_surname: str, first_name: str) -> str:
    """Construye las primeras 4 posiciones de la CURP (Regla 1).

    Formato: inicial + primera vocal interna del apellido paterno, inicial
    del apellido materno, inicial del nombre. Si falta un apellido, esa
    posición se rellena con "X" en vez de intentar sacarla de otro campo.

    Args:
        first_surname: Apellido paterno ya limpio (puede ser "").
        second_surname: Apellido materno ya limpio (puede ser "").
        first_name: Nombre ya limpio (nunca vacío, `PersonData` lo exige).

    Returns:
        Las 4 letras, con la segunda sustituida por "X" si el resultado
        forma una palabra de la lista `INAPPROPRIATE_WORDS` (Regla 9).

    """
    l1 = get_first_letter(first_surname) if first_surname else "X"
    l2 = get_first_vowel(first_surname) if first_surname else "X"
    l3 = get_first_letter(second_surname) if second_surname else "X"
    l4 = get_first_letter(first_name)

    prefix = f"{l1}{l2}{l3}{l4}"

    return prefix[0] + "X" + prefix[2:] if prefix in INAPPROPRIATE_WORDS else prefix


def _date(birth_date: date) -> str:
    """Posiciones 5-10: fecha de nacimiento en formato AAMMDD."""
    return birth_date.strftime("%y%m%d")


def _internal_consonants(
    first_surname: str, second_surname: str, first_name: str
) -> str:
    """Posiciones 14-16: primera consonante interna de cada campo.

    "Interna" significa a partir de la segunda letra de la palabra (la
    primera letra ya se usó en `_build_curp_prefix`). Si una palabra no
    tiene ninguna consonante después de la primera letra, se usa "X"
    """
    return (
        get_first_consonant(first_surname)
        + get_first_consonant(second_surname)
        + get_first_consonant(first_name)
    )


def calculate_check_digit(curp_17: str) -> str:
    """Posición 18: dígito verificador, calculado sobre las primeras 17.

    Cada carácter se multiplica por un peso DESCENDENTE (18 para el primer
    carácter, 2 para el decimoséptimo), se suma todo, y el dígito es
    `(10 - suma % 10) % 10`.

    Args:
        curp_17: Las primeras 17 posiciones de la CURP (sin el propio
            dígito verificador).

    Returns:
        Un solo carácter ("0" a "9").

    Raises:
        ValueError: si `curp_17` no mide exactamente 17 caracteres.

    """
    if len(curp_17) != 17:
        raise ValueError(
            "Se requieren exactamente 17 caracteres para calcular el dígito verificador"
        )

    values = {c: i for i, c in enumerate(ALPHABET_MX)}
    total = sum(values[char] * (18 - i) for i, char in enumerate(curp_17))

    return str((10 - (total % 10)) % 10)


def _homoclave(year: int) -> str:
    """Posición 17: diferenciador de homonimia.

    RENAPO es la única autoridad que asigna el valor real de esta posición
    (lo usa para distinguir personas que de otro modo tendrían la misma
    CURP hasta la posición 16). Como no hay forma de calcularlo fuera de
    su sistema, aquí se usa un valor por defecto que sigue al menos la
    convención de RENAPO de usar letra para nacidos en el siglo XXI y
    dígito para el siglo XX: "A" si el año es 2000 o posterior, "0" en
    caso contrario. La CURP resultante es válida en formato y dígito
    verificador, pero esta posición puede no coincidir con la oficial.

    Args:
        year: Año de nacimiento (4 dígitos).

    Returns:
        "A" o "0", según el siglo.

    Raises:
        ValueError: si `year` no está entre 1900 y 2099.

    """
    if not 1900 <= year <= 2099:
        raise ValueError("Año fuera del rango soportado")

    return "A" if year >= 2000 else "0"


def generate_curp(data: PersonData) -> str:
    """Genera la CURP completa (18 caracteres) de una persona física.

    Args:
        data: Datos personales ya validados (ver `PersonData`).

    Returns:
        La CURP completa: prefijo de 4 letras + fecha + sexo + entidad +
        consonantes internas + diferenciador de homonimia + dígito
        verificador.

    """
    first_surname, second_surname, first_name = _clean_fields(data)
    curp17 = (
        f"{_build_curp_prefix(first_surname, second_surname, first_name)}"
        f"{_date(data.birth_date)}"
        f"{data.sex}"
        f"{data.state}"
        f"{_internal_consonants(first_surname, second_surname, first_name)}"
        f"{_homoclave(data.birth_date.year)}"
    )

    return curp17 + calculate_check_digit(curp17)
