from clases.classAplicacion import AplicacionTareas
from clases.classProcesadorTareas import ProcesadorTareas
from tkinter import messagebox
import xml.etree.ElementTree as ET
import tkinter as tk

if __name__ == "__main__":
    nombre_del_archivo = "src/config/reporte_tareas.xml"
    app = AplicacionTareas(nombre_del_archivo)
    app.iniciar()
    print(f"Inciando la lectura del archivo: {nombre_del_archivo}")