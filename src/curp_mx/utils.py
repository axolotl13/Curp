import unicodedata

from .data import CONSONANTS, IGNORE_NAMES, PREPOSITIONS, VOWELS


def clean_text(text: str) -> str:
    """Normaliza un texto para su uso en el cálculo de CURP/RFC.

    Realiza las siguientes transformaciones:

    - Elimina espacios al inicio y al final.
    - Convierte el texto a mayúsculas.
    - Reemplaza temporalmente la Ñ por X.
    - Descompone los caracteres Unicode para separar letras y acentos.
    - Elimina las marcas diacríticas, como acentos y diéresis.
    - Restaura los caracteres de reemplazo cuando corresponde.
    - Conserva únicamente letras y espacios.

    Args:
    text: Texto original que se desea normalizar.

    Returns:
    El texto normalizado, sin acentos y con caracteres no válidos
    eliminados.

    """
    text = text.strip().upper().replace("Ñ", "\ufffd")
    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(c for c in normalized if unicodedata.category(c) != "Mn")
    without_accents = without_accents.replace("\ufffd", "Ñ")
    return "".join(c for c in without_accents if c.isalpha() or c == " ")


def clean_prepositions(text: str) -> list:
    """Elimina preposiciones y palabras ignoradas del texto.

    Primero normaliza el texto mediante clean_text y después
    elimina las palabras incluidas en PREPOSITIONS.

    Si todas las palabras son eliminadas, devuelve la lista original
    para evitar obtener una lista vacía.

    Args:
        text: Texto que contiene uno o más nombres o apellidos.

    Returns:
        Lista de palabras normalizadas sin las preposiciones ignoradas,
        o la lista original si todas fueron descartadas.

    """
    words = clean_text(text).split()
    return [w for w in words if w not in PREPOSITIONS] or words


def get_first_word_lastname(lastname: str) -> str:
    """Obtiene la primera palabra significativa de un apellido.

    Las preposiciones definidas en PREPOSITIONS son ignoradas.

    Args:
        lastname: Apellido completo.

    Returns:
        La primera palabra significativa del apellido o una cadena vacía
        si no contiene palabras.

    """
    words = clean_prepositions(lastname)
    return words[0] if words else ""


def get_first_word_firstname(first_name: str) -> str:
    """Obtiene el nombre que debe utilizarse para CURP.

    Si el primer nombre pertenece a IGNORE_NAMES y existe un segundo
    nombre, se utiliza el segundo. Esto permite ignorar nombres comunes
    definidos por las reglas del algoritmo.

    Args:
        first_name: Uno o más nombres.

    Returns:
        El nombre seleccionado para el cálculo o una cadena vacía si no
        se proporcionó ningún nombre.

    """
    words = clean_prepositions(first_name)
    if len(words) > 1 and words[0] in IGNORE_NAMES:
        return words[1]
    return words[0] if words else ""


def get_first_letter(word: str) -> str:
    """Obtiene la primera letra de una palabra.

    Args:
        word: Palabra de la que se desea obtener la primera letra.

    Returns:
        La primera letra de la palabra o "X" si está vacía.

    """
    return word[0] if word else "X"


def get_first_vowel(word: str):
    """Obtiene la primera vocal interna de una palabra.

    La búsqueda comienza después de la primera letra, por lo que la
    vocal inicial de la palabra no se considera.

    Args:
        word: Palabra en la que se buscará la vocal.

    Returns:
        La primera vocal encontrada después de la primera letra o
        "X" si no existe ninguna.

    """
    return next((vowel for vowel in word[1:] if vowel in VOWELS), "X")


def get_first_consonant(word: str) -> str:
    """Obtiene la primera consonante interna de una palabra.

    La búsqueda comienza después de la primera letra, por lo que la
    primera letra de la palabra no se considera.

    Args:
        word: Palabra en la que se buscará la consonante.

    Returns:
        La primera consonante encontrada después de la primera letra o
        ``"X"`` si no existe ninguna.

    """
    return next((consonant for consonant in word[1:] if consonant in CONSONANTS), "X")
