""" Copyright (c) 2023 Geovanni Santamaria. All Rights Reserved. 
Generate CURP following the Normative Instruction of 2006 provided by the Ministry 
of the Interior of the United Mexican States.
"""

from datetime import date, datetime

from unidecode import unidecode
from utils import entities, prepositions, profanities


class YearError(Exception):
    """
    This class throws an exception.

    Args:
        Exception (str): Show a message.
    """

    def __init__(self, message="The year cannot be greater than the current date."):
        super().__init__(message)


class LengthError(Exception):
    """
    This class throws an exception.

    Args:
        Exception (str): Show a message.
    """

    def __init__(self, message="The length does not comply with the established."):
        super().__init__(message)


def special_character(func):
    """
    This decorator replaces the value of the found function that matches the set.

    Args:
        func (function): Takes a function and its arguments.
    """

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        _special_character = set("ñ/-.")
        _special_character = "".join(
            "x" if letter in _special_character else letter for letter in result
        )
        return _special_character

    return wrapper


class Generator:
    """
    This class generates a Mexican CURP.

    Attributes:
        name (str): Person's first name.
        lastname (str): Person's paternal surname.
        mlastname (str): Person's maternal surname.
        day (int): Person's day of birth.
        month (int): Person's month of birth.
        year (int): Person's year of birth.
        gender (str): Person's gender.
        state (str): State where the person was born.
    """

    def __init__(
        self,
        name: str,
        lastname: str,
        mlastname: str,
        day: int,
        month: int,
        year: int,
        gender: str,
        state: str,
    ) -> None:
        self.name = name
        self.lastname = lastname
        self.mlastname = mlastname
        self.day = day
        self.month = month
        self.gender = gender
        self.year = year
        self.state = state

    def _clean_data(self, value) -> str:
        """
        Filters prepositions, conjunctions found in the first names and surnames.

        Args:
            value (str): Splits a string into a list.
        Returns:
            str: A string that has been filtered.
        """
        cleaned = filter(lambda value: not (value in prepositions.prep), value.split())
        return " ".join(list(cleaned))

    def _data(self) -> dict:
        """
        Create a dictionary with lowercase values and call a function to filter.

        Returns:
            dict: A filtered dictionary.
        """
        data = {
            "name": self.name,
            "lastname": self.lastname,
            "mlastname": self.mlastname,
            "gender": self.gender,
        }
        data = {key: self._clean_data(value.lower()) for key, value in data.items()}
        data |= {"state": self.state.lower()}
        return data

    def _filter_len(self, value) -> str:
        """
        Take the first value from the list if the value is found in the set
        and the length is greater than 1.

        Args:
            value (str): Split a string into a list.

        Returns:
            str: First string in a list depending on its length.
        """
        if len(result := value.split()) > 1:
            result = [
                result[1] if unidecode(result[0]) in ("maria", "jose") else result[0]
            ]

        return "".join(result)

    def _first_letter(self, letter) -> str:
        """
        Take the first character of the string; if none is found, return "x".

        Args:
            letter (str): A string.

        Returns:
            str: First character of a string.
        """
        return letter[0] if letter else "x"

    def _filter_vowels(self, value, is_vowel=False) -> str:
        """
        If the letter is a vowel, filter the vowels; otherwise, filter everything
        that is not a vowel.

        Args:
            value (str): Removes the first character from the string.
            is_vowel (bool, optional): Check if it is vowel. Defaults to False.

        Returns:
            str: First letter it finds.
        """
        value = value[1:]
        vowels = set("aáeéiíoóuúü-/.")
        if is_vowel:
            # vowels = vowels.union("-", "/", ".")
            search = filter(lambda letter: letter in vowels, value)
        else:
            search = filter(lambda letter: not (letter in vowels), value)
        return next(search, "x")

    @special_character
    def _lastname(self, consonant=False) -> str:
        """
        If it's not a consonant, it returns the first letter and filters the first vowel
        found; otherwise, it filters the first letter that is not found in the vowels.

        Args:
            consonant (bool, optional): Check if it is a consonant. Defaults to False.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: One or another string depending on a condition.
        """
        lastname = self._data()["lastname"]
        lastname = self._filter_len(lastname)
        if not lastname:
            raise LengthError()

        return (
            self._first_letter(lastname) + self._filter_vowels(lastname, True)
            if not consonant
            else self._filter_vowels(lastname)
        )

    @special_character
    def _mlastname(self, consonant=False) -> str:
        """
        If it's not a consonant, it filters the first vowel it finds; otherwise,
        it returns the first letter.

        Args:
            consonant (bool, optional): Check if it is a consonant. Defaults to False.

        Returns:
            str: One or another string depending on a condition.
        """
        mlastname = self._data()["mlastname"]

        return (
            self._first_letter(mlastname)
            if not consonant
            else self._filter_vowels(mlastname)
        )

    @special_character
    def _name(self, consonant=False) -> str:
        """
        If it's not a consonant, it filters the first vowel it finds; otherwise,
        it returns the first letter.

        Args:
            consonant (bool, optional): _description_. Defaults to False.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: One or another string depending on a condition.
        """
        name = self._data()["name"]
        name = self._filter_len(name)
        if not name:
            raise LengthError()

        return self._first_letter(name) if not consonant else self._filter_vowels(name)

    def _group_a(self) -> str:
        """
        Filters and replaces the dissonant words that are generated when you
        concatenate the surnames and the person's name.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: First the value that was found.
        """
        group_values = unidecode(self._lastname() + self._mlastname() + self._name())
        if len(group_values) != 4:
            raise LengthError()

        if group_values in profanities.words.keys():
            group_values = next(
                v for k, v in profanities.words.items() if k == group_values
            )

        return group_values

    def _birthdate(self) -> str:
        """
        Check if the year is greater than the current date.

        Raises:
            YearError: Year greater than the current date.

        Returns:
            str: Datetime a string.
        """
        birth = date(self.year, self.month, self.day)
        if (birthdate := birth) > datetime.date(datetime.now()):
            raise YearError()

        return birthdate.strftime("%y" + "%m" + "%d")

    def _gender(self) -> str:
        """
        Check if the gender is in one set or another.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: One or another string depending on a condition.
        """
        if (gender := self._data()["gender"]) in ("mujer", "m", "femenino", "f"):
            gender = "m"
        elif gender in ("hombre", "h", "masculino"):
            gender = "h"
        else:
            raise LengthError()

        return gender

    def _entities(self) -> str:
        """
        Filter the Mexican federal entities.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: Value that matches in the dictionary.
        """
        if (state := unidecode(self._data()["state"])) in entities.renapo.keys():
            state = next(v for k, v in entities.renapo.items() if k == state)
        else:
            raise LengthError()

        return state

    def _group_b(self) -> str:
        """
        A string with the first consonants found, excluding the first letter.

        Raises:
            LengthError: If the length does not meet the established criteria.

        Returns:
            str: A string of the first consonants.
        """
        fln = self._lastname(True) + self._mlastname(True) + self._name(True)
        if len(fln) != 3:
            raise LengthError()

        return fln

    def _century(self) -> str:
        """
        Check the 21st century.

        Returns:
            str: Zero if not within range
        """
        return "1" if self.year in range(2001, 2100) else "0"

    def _group_all(self) -> str:
        """
        Concatenate the values of the functions.

        Returns:
            str: A string with the values of the functions.
        """
        return (
            self._group_a()
            + self._birthdate()
            + self._gender()
            + self._entities()
            + self._group_b()
            + self._century()
        )

    def _verification_digit(self):
        """
        Calculates the verification digit.

        Returns:
            str: Concatenate CURP and the verification digit.
        """
        abc = "0123456789abcdefghijklmn~opqrstuvwxyz"
        curp = self._group_all()
        xurp = [abc.find(value) for value in reversed(curp + "0")]
        suma = ((sum((n + 1) * xurp[n] for n, _ in enumerate(curp)) % 10) - 10) * -1
        result = suma if suma != 10 else 0
        return curp + str(result)

    def printer(self):
        print(
            f"""\n
+ + + + + + + + + + + + + + + + + +
+       {self._verification_digit().upper()}        +
+ + + + + + + + + + + + + + + + + +
          Name:{self.name}
      Lastname:{self.lastname}
      Lastname:{self.mlastname}
     Birthdate:{self._birthdate()}
        Gender:{self.gender}
         State:{self.state}
+ + + + + + + + + + + + + + + + + +"""
        )
