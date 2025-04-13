class Hits:
    def __init__(self, logger, extractkeys_instance):
        """
        Inicializa una instancia de la clase Hits.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        """
        self.logger = logger
        self.extractkeys_instance = extractkeys_instance

    def get_hits(self, datos):
        """
        Calcula el numero de paginas basado en una lista de hits(resultado)
        -hits (list): lista de cadenas
        """
        hits = self.extractkeys_instance.extract_key_from_dict(
            datos, embeded_key=None, key="totalHits"
        )

        if (
            hits and hits[0].replace(",", "").isdigit()
        ):  # elimina comas y verifica si es un digito
            pages = int(hits[0].replace(",", "")) / 100
            pages = math.ceil(pages)  # redondear a entero superior
            self.logger.info(f"Total de páginas: {pages}")
            return pages
        return 0
