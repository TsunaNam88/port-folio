import json


class ReadData:
    """
    Clase para leer datos de un archivo Json
    """

    def __init__(self, filename, logger):
        """
        Metodo que inicializa la clase
        """
        self.filename = filename
        self.logger = logger

    def read_json(self):
        """
        Metodo que transforma y lee el archivo json
        """

        with open(self.filename, "r", encoding="utf-8") as f:
            employees = [json.loads(line) for line in f]
            self.logger.info(f"Datos obtenidos de {self.filename}")
        return employees
