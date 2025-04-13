import datetime


class EmployerAnalyzer:
    """
    Clase que analiza los datos validados de la empresa
    """

    def __init__(self, valid_employees, total_errores, logger):
        """
        Metodo constructor de la clase EmployerAnalyzer
        Cuenta la cantidad de empleados con datos validos
        cambia el tipo de dato de fecha_contratacion a datetime.date
        """
        self.valid_employees = valid_employees
        self.logger = logger
        self.total_errores = len(total_errores)
        self.total = len(valid_employees)

        # Cambiar el tipo de dato de fecha_contratacion a datetime.date
        for employee in self.valid_employees:
            if "fecha_contratacion" in employee and isinstance(
                employee["fecha_contratacion"], str
            ):
                try:
                    employee["fecha_contratacion"] = datetime.datetime.strptime(
                        employee["fecha_contratacion"], "%Y-%m-%d"
                    ).date()
                except ValueError:
                    employee["fecha_contratacion"] = None
        self.logger.info(
            "Se cambio el tipo de dato 'fecha_contratacion' de str a datetime"
        )

    def get_average_salary(self):
        """
        Metodo que calcula el salario promedio de los empleados
        return: float

        """

        if not self.valid_employees:
            self.logger.warning("No hay datos validos")
        else:
            average_salary = (
                sum([employee["salario"] for employee in self.valid_employees])
                / self.total
            )
            self.logger.info("Se aplico el metodo get_average_salary")
            return round(average_salary, 2)

    def count_by_apartment(self):
        """
        Metodo que cuenta la cantidad de empleados por departamento
        return:dict
        """
        department_counter = {}
        for empleado in self.valid_employees:
            departament = empleado["departamento"]
            if departament not in department_counter:
                department_counter[departament] = 0
            department_counter[departament] += 1
        self.logger.info("Se aplico el metodo count_by_department")
        return department_counter

    def average_performance(self):
        """
        Metodo que calcula el desempeño promedio de los empleados
        return: float
        """
        performance_average = (
            sum([employee["desempeno"] for employee in self.valid_employees])
            / self.total
        )
        self.logger.info("Se aplico el metodo average_performance")
        return round(performance_average, 2)

    def percentage_of_active_employees(self):
        """
        Metodo que calcula el porcentaje de empleados activos
        return: float
        """

        active_employees = sum(
            1 for employee in self.valid_employees if employee["activo"] is True
        )
        percent_active_employees = (active_employees / self.total) * 100
        self.logger.info("Se aplico el metodo percentage_of_active_employees")
        return round(percent_active_employees, 2)

    def average_days_employed(self):
        """
        Metodo para calcular el promedio de dias trabajados en la empresa
        return:float
        """
        today = datetime.date.today()
        total_days = sum(
            (today - employee["fecha_contratacion"]).days
            for employee in self.valid_employees
            if employee["fecha_contratacion"] is not None
        )
        average_days = total_days / self.total
        self.logger.info("Se aplico el metodo average_days_employeed")
        return round(average_days, 2)
