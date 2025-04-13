from fpdf import FPDF


from analyzer import EmployerAnalyzer  # Import the missing class


class EmployeeReportGenerator(EmployerAnalyzer):
    """
    Clase que realiza un reporte en pdf de los empleados de una empresa
    """

    def __init__(self, valid_employees, total_errores, logger):
        """
        Metodo que inicializa la clase EmployeeReportGenerator
        """
        super().__init__(valid_employees, total_errores, logger)
        self.logger = logger
        self.total_empleados = valid_employees + total_errores

    def generate_text_report(self, filename):
        """
        Metodo para generar un reporte en pdf de los empleados de una empresa
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Reporte de Empleados", ln=True, align="C")
        pdf.ln(10)
        self.logger.info("Se aplicaron valores de creacion de reporte en PDF")

        pdf.set_font("Arial", size=12)
        pdf.cell(
            200,
            10,
            txt=f"Empleados con datos incompletos: {self.total_errores}",
            ln=True,
        )
        pdf.cell(200, 10, txt=f"Total de empleados: {self.total_empleados}", ln=True)
        pdf.cell(
            200,
            10,
            txt=f"Total de empleados tomados para las estadisticas: {self.total}",
            ln=True,
        )
        pdf.cell(
            200, 10, txt=f"Salario promedio: ${self.get_average_salary()}", ln=True
        )
        pdf.cell(
            200, 10, txt=f"Desempeño promedio: {self.average_performance()}", ln=True
        )
        pdf.cell(
            200,
            10,
            txt=f"Porcentaje de empleados activos: {self.percentage_of_active_employees()}%",
            ln=True,
        )
        pdf.cell(
            200,
            10,
            txt=f"Promedio de días trabajados: {self.average_days_employed()} días",
            ln=True,
        )

        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="\nCantidad de empleados por departamento:", ln=True)
        pdf.set_font("Arial", size=12)

        for department, quantity in self.count_by_apartment().items():
            pdf.cell(200, 10, txt=f"{department}: {quantity} empleados", ln=True)
        pdf.output(filename)
        self.logger.info("Se aplico el metodo generate_text_report")
        self.logger.info(f"Reporte guardado en:{filename}")
        return filename
