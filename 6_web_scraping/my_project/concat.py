class Concat:
    def __init__(self):
        """
        Inicializa una instancia de la clase URLBuilder.

        Parámetros:
        - base_url: La URL base que se utilizará para construir las URLs completas.
        - extra: Parámetros adicionales que se añadirán al final de cada URL.
        """

    def concat(self, url_list):
        base_url = "https://century21mexico.com"
        extra = "?json=true"
        return [base_url + path + extra for path in url_list]
