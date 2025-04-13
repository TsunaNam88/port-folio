
import Data from data
import Concat from concat
import ExtractKeys from extractkeys
import Hits from hits
import ExtractData from extractdata
import TransformLinks from transformlinks
import StartData from startdata
import Resultados from resultados
import Batch from batch
import Logger from logger

def main():
    logger_instance = Logger()
    logger = logger_instance.get_logger()
    
    base_url_ = "https://century21mexico.com/v/resultados/ordenado-por_reelevancia/por_estado?json=true"
    url_correcta_propiedad = []
    
    logger.info("Iniciando el proceso de obtención de URLs de propiedades.")
    
    # Crear instancias de las clases necesarias
    data_instance = Data(logger)
    concat_instance = Concat()
    extractkeys_instance = ExtractKeys(logger, data_instance)
    hits_instance = Hits(logger, extractkeys_instance)
    extractdata_instance = ExtractData(logger, extractkeys_instance)
    transformlink_instance = TransformLinks(logger)
    startdata_instance = StartData(logger, transformlink_instance, data_instance, hits_instance, extractkeys_instance)
    resultados_instance = Resultados(logger, startdata_instance, extractdata_instance, transformlink_instance, data_instance, hits_instance)
    batch_instance = Batch(logger, data_instance)
    
    for estado in estados:   
        logger.info(f"Procesando estado: {estado}")
        url_correcta_propiedad.extend(resultados_instance.resultados(base_url_, estado, tipo_propiedad))
        
    #Concatenar para obtener una lista con los links completos
    full_url = concat_instance.concat(url_correcta_propiedad)
    logger.info(f"URLs completas concatenadas: {len(full_url)}")

    batch_instance.lotes(full_url, 100, "century21", ruta = "C:\\Users\\tsuda\\dataelite\\dataelite2024\\05_manipulacion_datos_tradicional\\Retos\\Soluciones\\century21")
    logger.info("Datos procesados y guardados en archivos CSV.")
    
if __name__ == "__main__":
    
    estados= ["Aguascalientes","Baja%20California","baja%20california%20norte","baja%20california%20sur",
    "Campeche","Chiapas","Chihuahua","Ciudad%20de%20Mexico","Coahuila","Colima","Durango",
    "Estado%20de%20Mexico","Guanajuato","Guerrero","Hidalgo","Jalisco","Michoacan",
    "Morelos","Nayarit","Nuevo%20Leon","Oaxaca","Puebla","Queretaro","Quintana%20Roo",
    "San%20Luis%20Potosi","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala",
    "Veracruz","Yucatan","Zacatecas"]

    estados = [estado.lower() for estado in estados]

    tipo_propiedad = ["tipo_casa/", "tipo_casa-duplex/","tipo_casa-en-condominio/","tipo_town-house/",
        "tipo_departamento/", "tipo_penthouse/","tipo_departamento-cuadruplex/", "tipo_departamento-triplex/",
        "tipo_terreno/", "tipo_huerta/", "tipo_quinta/", "tipo_rancho/", "tipo_hacienda/", "tipo_edificio/", "tipo_fraccionamiento/",
        "tipo_escuela/", "tipo_inmueble-productivo/", "tipo_consultorio/", "tipo_local/", "tipo_oficinas/", "tipo_bodega/", "tipo_fabrica/", "tipo_nave/" ]
    main()