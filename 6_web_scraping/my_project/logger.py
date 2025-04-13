class Logger:
    def __init__(self, log_file="app.log"):
        # Crear logger
        self.logger = logging.getLogger("App_Logger")
        self.logger.setLevel(logging.DEBUG)

        # Evitar duplicación de handlers
        if not self.logger.handlers:
            # Formato del log
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            # Crear manejador para archivo
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            file_handler.setLevel(logging.DEBUG)

            # Crear manejador para imprimir consola
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            console_handler.setLevel(logging.INFO)

            # Agregar handlers al logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger
