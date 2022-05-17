"""
Logging es seguir el rastro de lo que hace el usuario, te pude tirar warnings y excepciones pero hay distintos niveles de 
criticidad en las que podemos evaluar.

EL warning muestra por defecto de nivel de criticidad hacia arriba 

niveles de criticidad 

DEBUG 
INFO 
WARNING 
ERROR 
CRITICAL


para poner el formato de hora es format = '%(asctime)s - %(levelname)s - %(message)s'
"""
import logging

logging.basicConfig(filename='clase.log',
filemode = "w",
format = '%(asctime)s - %(levelname)s - %(message)s',
encoding='utf-8', 
level= logging.INFO)

logging.warning("este es un warning")
logging.info("El programa paso por aquí")
logging.critical("Pasó un desastre")
