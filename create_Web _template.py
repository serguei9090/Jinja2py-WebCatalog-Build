#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import fnmatch
import sys
import shutil
from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

# #nombre cliente de la carpeta y tipo template
cliente = "3RTVpaket"
type_temp = "index-c.html"

# Capture our current directory
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# get info from File for the catalog
# Variables
imagenes = []
txt = []
n = 1
r = 2
s = 0
check_list = 0

# getting path of files


def get_catalog_info(cat_path):
    imagenes = []
    imagenes_path = []
    txt = []
    Nombres = []
    Pais = []
    Canal = []
    Temporadas = []
    Capitulos = []
    Año = []
    Sinopsis = []
    Genero = []
    s = 0
    check_list = 0
    for dirpath, dirnames, filenames in os.walk(cat_path):
        for filename in filenames:
            if fnmatch.fnmatch(filename, "*.txt"):
                txt.append(os.path.join(dirpath, filename))
            if fnmatch.fnmatch(filename, "*.jpg"):
                imagenes.append(os.path.join(filename))
                imagenes_path.append(os.path.abspath(os.path.join(dirpath, filename)))
    # reading and put text info in array
    for content in txt:
        line = 0
        # Array Corection if needed
        if len(Nombres) < check_list:
            Nombres.append("NE")
        if len(Pais) < check_list:
            Pais.append("NE")
        if len(Canal) < check_list:
            Canal.append("NE")
        if len(Temporadas) < check_list:
            Temporadas.append("NE")
        if len(Capitulos) < check_list:
            Capitulos.append("NE")
        if len(Año) < check_list:
            Año.append("NE")
        if len(Sinopsis) < check_list:
            Sinopsis.append("NE")

        # Getting Info
        with open(txt[s], "r", encoding="utf-8") as ins:
            content_line = ins.readlines()
            for content_lines in content_line:
                if content_lines.split(":")[0].lower() == "nombre":
                    Nombres.append(
                        content_line[line].split(":")[1].rstrip("\n").rstrip("\t")
                    )
                elif content_lines.split(":")[0].lower() == "pais":
                    Pais.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "país":
                    Pais.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "canal":
                    Canal.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "temporadas":
                    Temporadas.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "capitulos":
                    Capitulos.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "capítulos":
                    Capitulos.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "episodios":
                    Capitulos.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "año":
                    Año.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "sinopsis":
                    Sinopsis.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "genero":
                    Genero.append(content_line[line].split(":")[1].rstrip("\n"))
                elif content_lines.split(":")[0].lower() == "género":
                    Genero.append(content_line[line].split(":")[1].rstrip("\n"))
                line += 1
        s += 1
        check_list += 1
    return (
        Nombres,
        Pais,
        Canal,
        Temporadas,
        Capitulos,
        Año,
        Sinopsis,
        Genero,
        imagenes,
        imagenes_path,
    )


# Arrays
text = []
icon = []
portadas = []
imagenes = []
imagenes_path = []
# declarar variables del negocio
categoria = "na"
nombre = "na"
# =================================
lema = "na"
sobre_nosotros_l1 = "na"
caracteristica_1 = "na"
caracteristica_2 = "na"
caracteristica_3 = "na"
sobre_nosotros_l2 = "na"
# =================================
total_doramas = "na"
total_novelas = "na"
total_series = "na"
total_animes = "na"
# =================================
info_corta_servicios = "na"
servicio_1 = "na"
info_servicio_1 = "na"
servicio_2 = "na"
info_servicio_2 = "na"
servicio_3 = "na"
info_servicio_3 = "na"
servicio_4 = "na"
info_servicio_4 = "na"
servicio_5 = "na"
info_servicio_5 = "na"
servicio_6 = "na"
info_servicio_6 = "na"
# =================================
llamada_accion = "na"
llada_accion_info = "na"
# =================================
pricing_info = "na"
titulo_precio_1 = "na"
precio_1 = "na"
tiempo_1 = "na"
info_servicio_1_0 = "na"
info_servicio_1_1 = "na"
info_servicio_1_2 = "na"
info_servicio_1_3 = "na"
info_servicio_1_4 = "na"
# =================================
titulo_precio_2 = "na"
precio_2 = "na"
tiempo_2 = "na"
info_servicio_2_0 = "na"
info_servicio_2_1 = "na"
info_servicio_2_2 = "na"
info_servicio_2_3 = "na"
info_servicio_2_4 = "na"
# =================================
titulo_precio_3 = "na"
precio_3 = "na"
tiempo_3 = "na"
info_servicio_3_0 = "na"
info_servicio_3_1 = "na"
info_servicio_3_2 = "na"
info_servicio_3_3 = "na"
info_servicio_3_4 = "na"
# =================================
preguntas_freq_info = "na"
pregunta_1 = "na"
respuesta_1 = "na"
pregunta_2 = "na"
respuesta_2 = "na"
pregunta_3 = "na"
respuesta_3 = "na"
pregunta_4 = "na"
respuesta_4 = "na"
pregunta_5 = "na"
respuesta_5 = "na"
# =================================
info_general_contacto = "na"
coordenadas = "na"
direccion = "na"
provincia = "na"
email = "na"
telefono = "na"
grupo_whatsapp = "na"
link_grupo_whatsapp = "na"
# =================================
twitter = "na"
facebook = "na"
instagram = "na"
linkedIn = "na"
# =================================
# fin de las variables
s = 0
# asignando info a las variables

for dirpath, dirnames, filenames in os.walk('Clientes/' + cliente + '/01-ClientInfo'):
    for filename in filenames:
        if fnmatch.fnmatch(filename, "*.txt"):
            text.append(os.path.join(dirpath, filename))
        if fnmatch.fnmatch(filename, "*.jpg"):
            portadas.append(os.path.join(dirpath, filename))
        if fnmatch.fnmatch(filename, "*.ico"):
            icon.append(os.path.abspath(os.path.join(dirpath, filename)))

for content in text:
    # asign variables
    with open(text[s], "r", encoding="utf-8") as ins:
        content_line = ins.readlines()
        for content_lines in content_line:
            if content_lines.split(":")[0].lower() == "categoria":
                categoria = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "nombre":
                nombre = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "lema":
                lema = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "sobre_nosotros_l1":
                sobre_nosotros_l1 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "caracteristica_1":
                caracteristica_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "caracteristica_2":
                caracteristica_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "caracteristica_3":
                caracteristica_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "sobre_nosotros_l2":
                sobre_nosotros_l2 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "total_doramas":
                total_doramas = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "total_novelas":
                total_novelas = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "total_series":
                total_series = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "total_animes":
                total_animes = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_corta_servicios":
                info_corta_servicios = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "servicio_1":
                servicio_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_1":
                info_servicio_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "servicio_2":
                servicio_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_2":
                info_servicio_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "servicio_3":
                servicio_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_3":
                info_servicio_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "servicio_4":
                servicio_4 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_4":
                info_servicio_4 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "servicio_5":
                servicio_5 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_5":
                info_servicio_5 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "servicio_6":
                servicio_6 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_6":
                info_servicio_6 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "llamada_accion":
                llamada_accion = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "llada_accion_info":
                llada_accion_info = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "pricing_info":
                pricing_info = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "titulo_precio_1":
                titulo_precio_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "precio_1":
                precio_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "tiempo_1":
                tiempo_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_1_0":
                info_servicio_1_0 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_1_1":
                info_servicio_1_1 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_1_2":
                info_servicio_1_2 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_1_3":
                info_servicio_1_3 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_1_4":
                info_servicio_1_4 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "titulo_precio_2":
                titulo_precio_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "precio_2":
                precio_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "tiempo_2":
                tiempo_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_2_0":
                info_servicio_2_0 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_2_1":
                info_servicio_2_1 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_2_2":
                info_servicio_2_2 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_2_3":
                info_servicio_2_3 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_2_4":
                info_servicio_2_4 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "titulo_precio_3":
                titulo_precio_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "precio_3":
                precio_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "tiempo_3":
                tiempo_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_servicio_3_0":
                info_servicio_3_0 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_3_1":
                info_servicio_3_1 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_3_2":
                info_servicio_3_2 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_3_3":
                info_servicio_3_3 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "info_servicio_3_4":
                info_servicio_3_4 = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "preguntas_freq_info":
                preguntas_freq_info = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "pregunta_1":
                pregunta_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "respuesta_1":
                respuesta_1 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "pregunta_2":
                pregunta_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "respuesta_2":
                respuesta_2 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "pregunta_3":
                pregunta_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "respuesta_3":
                respuesta_3 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "pregunta_4":
                pregunta_4 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "respuesta_4":
                respuesta_4 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "pregunta_5":
                pregunta_5 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "respuesta_5":
                respuesta_5 = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "info_general_contacto":
                info_general_contacto = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "coordenadas":
                coordenadas = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "direccion":
                direccion = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "provincia":
                provincia = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "email":
                email = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "telefono":
                telefono = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "grupo_whatsapp":
                grupo_whatsapp = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "link_grupo_whatsapp":
                link_grupo_whatsapp = (
                    content_lines.split(":")[1].rstrip("\n").rstrip("\t")
                )
            elif content_lines.split(":")[0].lower() == "twitter":
                twitter = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "facebook":
                facebook = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "instagram":
                instagram = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
            elif content_lines.split(":")[0].lower() == "linkedin":
                linkedIn = content_lines.split(":")[1].rstrip("\n").rstrip("\t")
    s += 1


# Nombres,Pais,Canal,Temporadas,Capitulos,Año,Sinopsis,Genero,imagenes,imagenes_path= get_catalog_info("Clientes/3RTVpaket/Catalogo")
(
    Nombres,
    Pais,
    Canal,
    Temporadas,
    Capitulos,
    Año,
    Sinopsis,
    Genero,
    imagenes,
    imagenes_path,
) = get_catalog_info("Clientes/" + cliente + "/Catalogo")
# Nombres,Pais,Canal,Temporadas,Capitulos,Año,Sinopsis,Genero,imagenes,imagenes_path,= get_catalog_info("Clientes/3RTVpaket/Catalogo")
# Nombres,Pais,Canal,Temporadas,Capitulos,Año,Sinopsis,Genero,imagenes,imagenes_path,= get_catalog_info("Clientes/3RTVpaket/Catalogo")
# Create dir func and copy assets
def create_out_folder(nombre):
    out_dir_name = nombre
    if not os.path.exists("Web_output/" + out_dir_name):
        os.mkdir("Web_output/" + out_dir_name)
        shutil.copytree(
            THIS_DIR + "/Template/assets",
            THIS_DIR + "/Web_output/" + nombre + "/assets",
        )


# create dir with busines name
create_out_folder(nombre)
# pass and copy img files
item_img_ok = []
l = 0
for img in imagenes_path:
    shutil.copy(
        img,
        THIS_DIR + "/Web_output/" + nombre + "/assets/catalog/" + Nombres[l] + ".jpg",
    )
    item_img_ok.append(Nombres[l] + ".jpg")
    l += 1
# Icon copy to assets
icon_ok = []
l = 0
for img in icon:
    shutil.copy(
        img,
        THIS_DIR + "/Web_output/" + nombre + "/assets/img/" + nombre + ".jpg",
    )
    icon_ok.append(nombre + ".jpg")
    l += 1
# =================Jinja Code=================
file_loader = FileSystemLoader("Template")
env = Environment(loader=file_loader, trim_blocks=True)
template = env.get_template(type_temp)


output = template.render(
    # info del negocio
    fav_icon=icon_ok,
    apple_touch_icon=icon_ok,
    nombre_negocio=nombre,
    categoria=categoria,
    about_us_lema=lema,
    about_us=sobre_nosotros_l1,
    caracteristica_1=caracteristica_1,
    caracteristica_2=caracteristica_2,
    caracteristica_3=caracteristica_3,
    about_us_2=sobre_nosotros_l2,
    series_count=total_series,
    novelas_count=total_novelas,
    doramas_count=total_doramas,
    animes_count=total_animes,
    general_service_info=info_corta_servicios,
    servicio_1=servicio_1,
    servicios_info_1=info_servicio_1,
    servicio_2=servicio_2,
    servicios_info_2=info_servicio_2,
    servicio_3=servicio_3,
    servicios_info_3=info_servicio_3,
    servicio_4=servicio_4,
    servicios_info_4=info_servicio_4,
    servicio_5=servicio_5,
    servicios_info_5=info_servicio_5,
    servicio_6=servicio_6,
    servicios_info_6=info_servicio_6,
    call_to_action=llamada_accion,
    call_to_action_info=llada_accion_info,
    pricing_info=pricing_info,
    price_title_1=titulo_precio_1,
    price_1=precio_1,
    unidad_1=tiempo_1,
    price_serv_info_1_0=info_servicio_1_0,
    price_serv_info_1_1=info_servicio_1_1,
    price_serv_info_1_2=info_servicio_1_2,
    price_serv_info_1_3=info_servicio_1_3,
    price_serv_info_1_4=info_servicio_1_4,
    price_title_2=titulo_precio_2,
    price_2=precio_2,
    unidad_2=tiempo_2,
    price_serv_info_2_0=info_servicio_2_0,
    price_serv_info_2_1=info_servicio_2_1,
    price_serv_info_2_2=info_servicio_2_2,
    price_serv_info_2_3=info_servicio_2_3,
    price_serv_info_2_4=info_servicio_2_4,
    price_title_3=titulo_precio_3,
    price_3=precio_3,
    unidad_3=tiempo_3,
    price_serv_info_3_0=info_servicio_3_0,
    price_serv_info_3_1=info_servicio_3_1,
    price_serv_info_3_2=info_servicio_3_2,
    price_serv_info_3_3=info_servicio_3_3,
    price_serv_info_3_4=info_servicio_3_4,
    preguntas_info=preguntas_freq_info,
    pregunta_1=pregunta_1,
    respuesta_1=respuesta_1,
    pregunta_2=pregunta_2,
    respuesta_2=respuesta_2,
    pregunta_3=pregunta_3,
    respuesta_3=respuesta_3,
    pregunta_4=pregunta_4,
    respuesta_4=respuesta_4,
    pregunta_5=pregunta_5,
    respuesta_5=respuesta_5,
    contacto_info=info_general_contacto,
    coordenadas=coordenadas,
    direction=direccion,
    provincia=provincia,
    email=email,
    telefono=telefono,
    WTAPP_group=grupo_whatsapp,
    WTAPP_group_link=link_grupo_whatsapp,
    twitter=twitter,
    facebook=facebook,
    instagram=instagram,
    linkedIn=linkedIn,
    # pasando info del catalogo
    item_img=item_img_ok,
    Nombre=Nombres,
    Pais=Pais,
    Canal=Canal,
    Temporadas=Temporadas,
    Capitulos=Capitulos,
    age=Año,
    Descripcion=Sinopsis,
    Genero=Genero,
    # info page
    self_href=nombre + "-" + categoria + ".html",
)
# print(output)


# export html
with open(
    "Web_output/" + nombre + "/" + nombre + "-" + categoria + ".html",
    "w",
    encoding="utf-8",
) as file:
    file.write(output)
