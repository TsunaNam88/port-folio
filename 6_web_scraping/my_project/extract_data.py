class ExtractData:
    def __init__(self, logger, extractkeys_instance):
        """
        Inicializa una instancia de la clase ExctractData.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        - extractkey_instance: Una instancia de la clase ExtractKeys para extraer claves específicas de los datos.
        """
        self.logger = logger
        self.extractkeys_instance = extractkeys_instance

    def obtener_id(self, link):
        id = []
        id.extend(
            self.extractkeys_instance.extract_keys_for_link(
                link, embeded_key="idOriginal", key="results"
            )
        )
        self.logger.info(f"Total de id: {len(id)}")
        return id

    def obtener_urlcorrectapropiedad(self, links):
        url_correcta_extract = []

        # Asegurar que links sea una lista
        if not isinstance(links, list):
            links = [links]  # Convertir en lista si es un solo elemento

        url_correcta_extract.extend(
            self.extractkeys_instance.extract_keys_for_link(
                links, embeded_key="urlCorrectaPropiedad", key="results"
            )
        )
        self.logger.info(
            f"URLs extraídas hasta ahora: {len(url_correcta_extract)} elementos"
        )
        return url_correcta_extract
