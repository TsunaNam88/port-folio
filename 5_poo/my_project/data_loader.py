import re


class EmployeeDataLoader:
    """
    Clase para cargar y limpiar los datos de los empleados
    """

    def __init__(self, employees, logger):
        self.employees = employees
        self.logger = logger

    def get_clean_data(self):
        """
        Metodo que valido las claves y valores de los diccionarios
        -Obtiene una lista de diccionarios
        -Devuelve una lista de diccionarios con los valores adecuados
        para cada clave y una lista de errores de aquellos que no
        contienen todas las claves
        """
        mandatory_keys = {
            "id": str,  # Identificador único del empleado (UUID)
            "nombre": str,  # Nombre completo del empleado
            "edad": int,  # Edad del empleado
            "genero": str,  # Género (Masculino, Femenino, etc.)
            "departamento": str,  # Departamento al que pertenece
            "cargo": str,  # Cargo que desempeña en la empresa
            "email": str,  # Correo electrónico
            "telefono": str,  # Número de teléfono
            "direccion": str,  # Dirección física
            "salario": float,  # Salario base anual (o mensual, según convenga)
            "fecha_contratacion": str,  # Fecha de contratación en formato YYYY-MM-DD
            "desempeno": float,  # Valor numérico que represente el desempeño (ej. 0 a 10)
            "activo": bool,  # Indica si el empleado sigue activo en la empresa
        }

        activo_dict = {
            "activo": True,
            "on": True,
            "1": True,
            "yes": True,
            "y": True,
            1: True,
            "true": True,
            "t": True,
            "inactivo": False,
            "off": False,
            "0": False,
            "no": False,
            "n": False,
            0: False,
            "false": False,
            "f": False,
        }

        valid_employees = []
        errors = []

        for i, dic in enumerate(self.employees):
            # verificar la existencia de claves:
            missing = [clave for clave in mandatory_keys.keys() if clave not in dic]
            if missing:
                errors.append(f"Error en empleado {i}: faltan las claves: {missing}")
                self.logger.warning(
                    f"Error en empleado {i}: faltan las claves: {missing}"
                )
                continue

            # cambiar a boleano
            dic["activo"] = str(dic["activo"]).lower().strip()
            dic["activo"] = activo_dict.get(str(dic["activo"]).strip(), None)

            # ambiar a int/float
            dic["edad"] = int(dic["edad"])
            dic["salario"] = float(dic["salario"])
            dic["desempeno"] = float(dic["desempeno"])

            # comprobar fechas
            if dic.get("fecha_contratacion"):
                if isinstance(dic["fecha_contratacion"], str):
                    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dic["fecha_contratacion"]):
                        errors.append(
                            f"Error en empleado {i}: la fecha de contratación no es válida"
                        )
                        self.logger.warning(
                            f"Error en empleado {i}: faltan las claves: {missing}"
                        )
                        continue

            empleado_valido = True
            for clave, tipo in mandatory_keys.items():
                if not isinstance(dic[clave], tipo):
                    errors.append(
                        f"Error en empleado {i}: la clave '{clave}' no es del tipo {tipo.__name__}"
                    )
                    self.logger.warning(
                        f"Error en empleado {i}: la clave '{clave}' no es del tipo {tipo.__name__}"
                    )
                    empleado_valido = False
            if empleado_valido:
                valid_employees.append(dic)
        self.logger.info("Se creo la lista de empleados validos")
        return valid_employees, errors
