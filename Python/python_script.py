import os

#### Carpeta dataset ####
location = 'C:/Users/USUARIO/Documents/Proyecto Parcial/Python/Dataset'

# Validar si exista la carpeta #
if not os.path.exists(location):
    ##Si no existe la creo##
    os.mkdir(location)
else: ##si la carpeta existe..
    ##borrar el contenido
    for root, dirs, files in os.walk(location,topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##Eliminar archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##Eliminar las carpetas
            
##Importar librería kaggle##
from kaggle.api.kaggle_api_extended import KaggleApi

## Autenticarnos en kaggle##
api = KaggleApi()
api.authenticate()

### Descargar dataset ###
#print(api.dataset_list(search=''))

api.dataset_download_files('rahulvyasm/netflix-movies-and-tv-shows',path=location, force=True,quiet=False,unzip=True)
