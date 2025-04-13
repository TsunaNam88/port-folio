class TransformLinks:
    def __init__(self, logger):
        """
        Inicializa una instancia de la clase TransformLinks.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        """
        self.logger = logger

    def add_extra_path(self, base_link, extra_path):
        """
        Añade rutas adicionales a la URL base.

        Parámetros:
        - base_link: La URL base.
        - extra_path: Una lista de rutas adicionales.

        Retorna:
        - Una lista de URLs con las rutas adicionales.
        """
        urls = []
        for path in extra_path:
            new_base_link = base_link.replace("resultados/", f"resultados/{path}")
            urls.append(new_base_link)
        return urls

    def add_paginated_links(self, base_link, extra_pag, extra_path=None):
        """
        Añade enlaces paginados a la URL base.

        Parámetros:
        - base_link: La URL base.
        - extra_pag: Un número que indica la cantidad de páginas adicionales.
        - extra_path: Una lista de rutas adicionales (opcional).

        Retorna:
        - Una lista de URLs paginadas.
        """

        urls = []
        for p in range(2, extra_pag + 1):
            paginated_link = base_link.replace(
                "ordenado-por_reelevancia", f"ordenado-por_reelevancia/pagina_{p}"
            )
            urls.append(paginated_link)
            if extra_path:
                urls.extend(self.add_extra_path(paginated_link, extra_path))
        return urls

    def get_link(self, base_url, data=None, extra_pag=None, extra_path=None):
        """
        Genera una lista de Urls basadas en una url y varios parametros opcionales

        Parametros:
        - base_url (str): la URL base.
        - data (list, opcional): Una lista de datos que se utilizarán para formatear la URL base.
        - extra_pag (list, opcional): Un número que indica la cantidad de páginas adicionales.
        - extra_path (lista, opcional): Una lista opcional de rutas adicionales que se deben concatenar a la URL base.

        Returns:
        -list: Una lista de urls generadas.
        """
        urls = []  # lista vacia
        if data:  # si hay data
            for dato in data:  # por cada dato en data
                base_link = base_url.replace("por_estado", f"por_{dato}")
                if extra_pag:
                    urls.extend(
                        self.add_paginated_links(base_link, extra_pag, extra_path)
                    )
                if extra_path:
                    urls.extend(self.add_extra_path(base_link, extra_path))
                else:
                    urls.append(base_link)
        else:
            urls.append(base_url)
            if extra_pag:
                urls.extend(self.add_paginated_links(base_url, extra_pag, extra_path))

        return urls
