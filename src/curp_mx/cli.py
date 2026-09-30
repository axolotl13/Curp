"""CLI: python -m curp_mx generar | validar"""

import argparse
import sys
from datetime import datetime

from .generator import PersonData, generate_curp


def generate_cmd(args):
    try:
        fecha = datetime.strptime(args.fecha_nacimiento, "%d/%m/%Y").date()
    except ValueError:
        print("Error: la fecha debe tener formato DD/MM/AAAA", file=sys.stderr)
        sys.exit(1)

    try:
        data = PersonData(
            first_name=args.nombre,
            first_surname=args.primer_apellido,
            second_surname=args.segundo_apellido or "",
            birth_date=fecha,
            sex=args.sexo,
            state=args.estado,
        )
        curp = generate_curp(data)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(curp)
    print(
        "\nNota: la posición 17 (homoclave) se generó como '0' por defecto. "
        "RENAPO puede asignar otro valor para evitar duplicados. Verifica "
        "siempre la CURP oficial en https://www.gob.mx/curp/",
        file=sys.stderr,
    )


def main():
    parser = argparse.ArgumentParser(description="Generador de CURP (México)")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    p_generate = subparsers.add_parser(
        "generar", help="Genera una CURP a partir de datos personales"
    )
    p_generate.add_argument("--nombre", required=True)
    p_generate.add_argument("--primer-apellido", required=True)
    p_generate.add_argument("--segundo-apellido", default="")
    p_generate.add_argument(
        "--fecha-nacimiento", required=True, help="Formato DD/MM/AAAA"
    )
    p_generate.add_argument("--sexo", required=True, choices=["H", "M"])
    p_generate.add_argument(
        "--estado", required=True, help="Clave de 2 letras, ej. JC, DF, NL"
    )
    p_generate.set_defaults(func=generate_cmd)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
