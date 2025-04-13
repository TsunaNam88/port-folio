class Batch:
    def __init__(self, logger, data_instance):
        """
        Inicializa una instancia de la clase ExtractKeys.

        Parámetros:
        - logger: Un objeto de registro para registrar mensajes de depuración o información.
        - data_instance: Una instancia de la clase Data para obtener datos.
        """
        self.logger = logger
        self.data_instance = data_instance

    def lotes(self, data, tamaño_bache, nombre_csv, ruta):
        """
        Procesa los datos en lotes y guarda los resultados
        en un archivo csv

        Parametros:
        - data (list): datos que se procesaran
        -tamaño_bache (int): un numero entero que indica el tamaño del bache
        -nombre_csv (str): nombre del archivo csv que se generara
        -ruta (str): ruta donde se guarda el archivo scv
        """
        batch = []  # almacena los resultados de cada lote
        for i, dato in enumerate(
            data
        ):  # enumerate pata oobtener el indice y el valor (dato)
            self.logger.info(f"Procesando dato (en lotes): {i + 1}/{len(data)}")
            result = self.data_instance.get_data(
                dato, headers_home
            )  # para cada dato se llama a get_data
            if not result:
                self.logger.warning(f"No se obtuvieron datos para {dato}")
            batch.append(result)

            num_bache = i // tamaño_bache
            if (i + 1) % tamaño_bache == 0 or (i + 1) == len(
                data
            ):  # tamaño especificado
                df = pd.json_normalize(batch)  # guardado
                filename = df.to_csv(
                    f"{ruta}/{nombre_csv}_{i // tamaño_bache + 1}.csv", index=False
                )
                self.logger.info(f"Guardado: {filename}")

                df_progreso = pd.DataFrame({"Bache": [num_bache]})  # status de guardado
                df_progreso.to_csv(f"{ruta}status_file.csv", index=False)
                self.logger.info(f"Progreso actualizado: Bache {num_bache}")
                batch = []
