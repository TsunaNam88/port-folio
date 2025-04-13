class StartData:
    def __init__(
        self,
        logger,
        transformlinks_instance,
        data_instance,
        hits_instance,
        extractkeys_instance,
    ):
        """
        Inicializa una instancia de la clase StartData.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        - transformlinks_instance: Una instancia de la clase TransformLinks para generar enlaces.
        - data_instance: Una instancia de la clase Data para obtener datos.
        - hits_instance: Una instancia de la clase Hits para calcular el número de hits.
        - extractkeys_instance: Una instancia de la clase ExtractKeys para extraer claves de los datos.
        """
        self.logger = logger
        self.transformlinks_instance = transformlinks_instance
        self.data_instance = data_instance
        self.hits_instance = hits_instance
        self.extractkeys_instance = extractkeys_instance

    def start_data(self, base_url, data, headers_home):
        urls = self.transformlinks_instance.get_link(base_url, data)

        json_ = self.data_instance.get_data(urls, headers_home)
        if not json_:
            self.logger.error(f"No se obtuvieron datos JSON de: {len(urls)}")
            raise ValueError("No se obtuvieron datos JSON ")
        hits = self.hits_instance.get_hits(json_)
        if not hits:
            self.logger.error("No se obtuvieron hits")
            raise ValueError("No se obtuvieron hits")

        return hits, urls
