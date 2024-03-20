from logging import error as lerror

from generator import Generator

if __name__ == "__main__":
    try:
        options = (
            'Name(s): "José María": ',
            "First surname: ",
            "Second surname: ",
            "Birth day: ",
            "Birth month: ",
            "Birt year: ",
            "Gender: ",
            "State: ",
        )
        data = tuple(map(input, options))
        Generator(
            data[0],
            data[1],
            data[2],
            int(data[3]),
            int(data[4]),
            int(data[5]),
            data[6],
            data[7],
        ).printer()
    except KeyboardInterrupt as e:
        lerror(f"Error: Se interrumpio la ejecución {e}")
    except Exception as e:
        lerror(f"Error: Se produjo una falla - {e}")
