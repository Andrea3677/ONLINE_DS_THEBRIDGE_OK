from Variables import *
from Funciones import *
import os
import shutil

os.chdir(ruta_abs)
lista_archivos = os.listdir(ruta_abs)
comprobacion = ['Documentos','Imagenes', 'Software','Otros']
for elemento in comprobacion:
    if elemento not in lista_archivos:
        os.mkdir(elemento)
    else:
        continue

for elemento in lista_archivos:
    ruta_completa = os.path.join(ruta_abs, elemento)
    if os.path.isdir(ruta_completa):
        pass
    else:
        if type_doc(elemento, doc_types):
            ruta_doc = "Documentos\\"
            ruta_orden = os.path.join(ruta_abs, ruta_doc)
            shutil.move(elemento, ruta_orden)
        elif type_img(elemento, img_types):
            ruta_doc = "Imagenes\\"
            ruta_orden = os.path.join(ruta_abs, ruta_doc)
            shutil.move(elemento, ruta_orden)
        elif type_software(elemento, software_types):
            ruta_doc = "Software\\"
            ruta_orden = os.path.join(ruta_abs, ruta_doc)
            shutil.move(elemento, ruta_orden)
        else:
            ruta_doc = "Otros\\"
            ruta_orden = os.path.join(ruta_abs, ruta_doc)
            shutil.move(elemento, ruta_orden)