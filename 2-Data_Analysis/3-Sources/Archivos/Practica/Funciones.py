def type_doc(archivo, doc_types):
    for tipo in doc_types:
        if archivo.endswith(tipo):
            return True
    return False

def type_img(archivo, img_types):
    for tipo in img_types:
        if archivo.endswith(tipo):
            return True
    return False

def type_software(archivo, software_types):
    for tipo in software_types:
        if archivo.endswith(tipo):
            return True
    return False