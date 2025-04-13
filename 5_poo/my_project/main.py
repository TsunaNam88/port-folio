from data_loader import EmployeeDataLoader
from report_generator import EmployeeReportGenerator
from logger import Logger
from read_file import ReadData


def main():
    """
    Funcion principal que ejecuta el programa
    """
    filname = "C:\\Users\\tsuda\\dataelite\\dataelite2025\\02_herramientas_ciencia_de_datos\\Retos\\Soluciones\\my_project"
    json_file = filname + "\\empleados.json"
    filname_report = filname + "\\reporte_empleados.pdf"
    # crear el logger
    logger = Logger().get_logger()
    # Abrir el archivo Json
    data_file = ReadData(json_file, logger)
    employee = data_file.read_json()
    # Validar los datos
    data_loader = EmployeeDataLoader(employee, logger)
    datos_limpios, errores = data_loader.get_clean_data()
    report_generator = EmployeeReportGenerator(datos_limpios, errores, logger)

    # Generar y mostrar el reporte
    report = report_generator.generate_text_report(filname_report)
    print(report)


if __name__ == "__main__":
    main()
