class Resultados:
    def __init__(
        self,
        logger,
        startdata_instance,
        extractdata_instance,
        transformlink_instance,
        data_instance,
        hits_instance,
    ):
        """
        Inicializa una instancia de la clase Resultados.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        - startdata_instance: Una instancia de la clase StartData para obtener datos iniciales.
        - extractdata_instance: Una instancia de la clase ExtractData para extraer datos específicos.
        - transformlink_instance: Una instancia de la clase TransformLinks para generar enlaces.
        - data_instance: Una instancia de la clase Data para obtener datos.
        - hits_instance: Una instancia de la clase Hits para calcular el número de hits.
        """
        self.logger = logger
        self.startdata_instance = startdata_instance
        self.extractdata_instance = extractdata_instance
        self.transformlink_instance = transformlink_instance
        self.data_instance = data_instance
        self.hits_instance = hits_instance

    def greater_than_15(self, links):
        """
        Procesa enlaces cuando hay más de 15 páginas de resultados.

        Parámetros:
        - links: Lista de enlaces a procesar.
        - headers_home: Encabezados para la solicitud.

        Retorna:
        - Una lista de URLs correctas extraídas.
        """
        url_correcta_extract = []

        for link in links:
            self.logger.info(f"-Link en proceso {link}")
            datos = self.data_instance.get_data(link, headers_home)
            paginas_link = self.hits_instance.get_hits(datos)

            if paginas_link == 1:  # tipo de propiedad menos de 100 resultados
                self.logger.info(
                    f"- tipo de propiedad por estado (== 1 pagina) {paginas_link}"
                )
                url_correcta_extract.extend(
                    self.extractdata_instance.obtener_urlcorrectapropiedad(link)
                )
                self.extractdata_instance.obtener_id(link)

            if paginas_link > 1:  # por numero de pagina y estado
                paginated_links = self.transformlink_instance.get_link(
                    base_url=link, data=None, extra_pag=paginas_link, extra_path=None
                )
                self.logger.info(
                    f"- este es paginated tipo de propiedad por estado (> 1 pagina) {paginated_links}"
                )
                for link in paginated_links:
                    url_correcta_extract.extend(
                        self.extractdata_instance.obtener_urlcorrectapropiedad(link)
                    )
                    self.extractdata_instance.obtener_id(link)
        return url_correcta_extract

    def between_1_and_15(self, links):
        """
        Procesa enlaces cuando hay entre 1 y 15 páginas de resultados.

        Parámetros:
        - links: Lista de enlaces a procesar.

        Retorna:
        - Una lista de URLs correctas extraídas.
        """
        url_correcta_extract = []

        self.logger.info(f"- esta es 1 a 15: {links}")
        for link in links:
            url_correcta_extract.extend(
                self.extractdata_instance.obtener_urlcorrectapropiedad(link)
            )
            self.extractdata_instance.obtener_id(link)
        return url_correcta_extract

    def resultados(self, base_url, estado, tipo_propiedad):
        """
        Obtiene y procesa datos de propiedades desde una URL base, filtrados por estado y tipo de propiedad.

        Parámetros:
        - base_url: La URL base desde la cual se obtendrán los datos.
        - estado: El estado para el cual se desean obtener las propiedades.
        - tipo_propiedad: El tipo de propiedad que se desea filtrar.
        - headers_home: Encabezados para la solicitud.

        Retorna:
        - Una lista de URLs correctas extraídas.
        """
        paginas, urls = self.startdata_instance.start_data(
            base_url, data=[estado], headers_home=headers_home
        )

        url_correcta_extract = []

        if paginas > 15:
            links = self.transformlink_instance.get_link(
                base_url, data=[estado], extra_pag=None, extra_path=tipo_propiedad
            )
            url_correcta_extract.extend(self.greater_than_15(links))

        elif 1 < paginas <= 15:  # por numero de pagina y estado
            links = self.transformlink_instance.get_link(
                base_url, data=[estado], extra_pag=paginas, extra_path=None
            )
            url_correcta_extract.extend(self.between_1_and_15(links))

        elif paginas <= 1:
            self.logger.info(f"- solo un link: {urls}")
            url_correcta_extract.extend(
                self.extractdata_instance.obtener_urlcorrectapropiedad(urls)
            )
            self.extractdata_instance.obtener_id(urls)
        return url_correcta_extract
