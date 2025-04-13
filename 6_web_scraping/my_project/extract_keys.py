class ExtractKeys:
    def __init__(self, logger, data_instance):
        """
        Inicializa una instancia de la clase TransformLinks.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        """
        self.logger = logger
        self.data_instance = data_instance

    def extract_key_from_dict(self, source, embeded_key=None, key=None):
        """
        Extrae los valores proporcionados de un diccionario anidado.
        - source: La fuente de datos, que puede ser un diccionario o una lista de diccionarios.
        - embeded_key (opcional): Una clave  que se utiliza para extraer valores de un diccionario anidado.
        - key (opcional): Una clave que se utiliza para extraer valores del diccionario o lista de diccionarios.
        """
        if not source:  # sin datos que procesar
            self.logger.warning("No hay datos que procesar")
            return []
        if embeded_key:  # la funcion asume que source es una lista de diccionarios
            first_page = source[0]
            key_ = first_page.get(key, [])  # se obtiene el diccionario key

            if not isinstance(key_, list):  # Si no es una lista, convertirlo en lista
                key_ = [key_]

            results = [
                item.get(embeded_key)
                for item in key_
                if isinstance(item, dict) and embeded_key in item
            ]  # itera sobre key y extrae embeded_key
            return results + self.extract_key_from_dict(source[1:], embeded_key, key)

        else:  # si embede_key no se proporciona, solo se extrae key
            results = [
                item.get(key)
                for item in source
                if isinstance(item, dict) and key in item
            ]
            return results

    def extract_keys_for_link(self, link, embeded_key, key):
        """
        Extrae claves de datos obtenidos apartir de una lista de enlaces.
        - links (list): Enlaces (URLs) desde los cuales se obtendran los datos
        Returns:
        - lits: datos extraidos de los enlaces.
        """
        json_ = self.data_instance.get_data(
            link, headers_home
        )  # se llama a la funcion get_data
        if not json_:
            self.logger.warning(f"No se obtuvieron datos de {link}")
            return []
        self.logger.info(f"Datos obtenidos de {link}: {len(json_)} elementos")
        extracted_keys = self.extract_key_from_dict(
            source=json_, embeded_key=embeded_key, key=key
        )
        return extracted_keys
