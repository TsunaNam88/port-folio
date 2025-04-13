class Data:
    def __init__(self, logger):
        """
        Inicializa una instancia de la clase Data.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        """

        self.logger = logger

    def get_data(self, source, headers_home):
        """
        Obtiene datos en formato JSON desde una URL o una lista de URLs.

        Parámetros:
        - source: Una cadena o lista que representa la URL o URLs.
        - headers_home: Encabezados para la solicitud.

        Retorna:
        - Una lista de resultados en formato JSON.
        """
        results_page = []
        urls = source if isinstance(source, list) else [source]

        for url in urls:
            self.logger.info(f"Solicitando datos de {url}")
            response = req.get_requests(url, headers_home)

            if response:
                json_response = response.json()
                results_page.append(json_response)
                self.logger.info(f"Datos obtenidos correctamente de {url}")
            else:
                self.logger.warning(
                    f"Error al obtener datos de {url}: {response.status_code}"
                )

        return results_page
