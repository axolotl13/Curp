from generator import Generator


def main():
    Generator("Alberto", "Ñando", "Rodríguez", 12, 2, 1979, "H", "Yucatan").printer()
    Generator(
        "María Luisa", "Pérez", "Hernandez", 28, 1, 1999, "Mujer", "Queretaro"
    ).printer()
    Generator(
        "Luis Enrique", "Romero", "Palazuelos", 30, 6, 1923, "Hombre", "Nuevo León"
    ).printer()
    Generator(
        "Juan Jose", "D/amico", "Alvares", 1, 12, 1980, "Hombre", "Sinaloa"
    ).printer()
    Generator("Rocio", "Riva Palacio", "Cruz", 3, 8, 2001, "M", "Oaxaca").printer()
    Generator(
        "Carlos", "MC Gregor", "López", 13, 6, 1923, "Hombre", "Estado de México"
    ).printer()
    Generator(
        "Ofelia", "Pedrero", "Dóminguez", 23, 10, 2010, "Mujer", "Veracruz"
    ).printer()
    Generator(
        "Andres", "Ich", "Rodríguez", 20, 9, 2000, "H", "Baja California"
    ).printer()
    Generator("Luis", "Perez", "", 6, 10, 1967, "H", "Chihuahua").printer()
    Generator("Alberto", "Oñate", "Rodríguez", 12, 1, 2017, "H", "Colima").printer()
    Generator("Leticia", "Luna", "", 16, 12, 2003, "M", "Guerrero").printer()
    Generator(
        "Maria de los Angeles",
        "Moreno",
        "Sanchez",
        19,
        8,
        1983,
        "M",
        "Baja California Sur",
    ).printer()


if __name__ == "__main__":
    main()
