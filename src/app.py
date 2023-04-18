import os
from glob import glob
import cairosvg
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

# Carpeta donde están los íconos en formato SVG
folder_path = "../svg/"

# Recorre la carpeta y sus subcarpetas en busca de archivos SVG
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".svg"):
            # Ruta completa del archivo SVG
            svg_file_path = os.path.join(root, file)
            
            # Lee el archivo SVG con svglib
            drawing = svg2rlg(svg_file_path)
            
            # Crea un archivo PNG con cairosvg
            png_file_path = os.path.splitext(svg_file_path)[0] + ".png"
            with open(png_file_path, "wb") as png_file:
                renderPM.drawToFile(drawing, png_file, fmt="PNG")