import tkinter as tk 
import sys
import os
from tkinter import ttk 
from clases.classProcesadorTareas import ProcesadorTareas
from clases.classProcesadorTareas import MonitorXML

class AplicacionTareas: 
    def __init__(self, nombre_archivo="src/config/reporte_tareas.xml"): 
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        self.nombre_archivo = nombre_archivo 
        self.tareas_actuales = []
         
        self.ventana = tk.Tk() 
        self.ventana.title("Actividad 3.1 - Reporte de Tareas") 
        self.ventana.geometry("700x400") 
         
        # Configurar qué hacer al cerrar la ventana 
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion) 
         
        self.crear_widgets() 
         
        # Carga inicial de datos 
        proceso = ProcesadorTareas()
        self.tareas_actuales = proceso.leer_xml_y_crear_tareas(self.nombre_archivo)
        self.actualizar_tabla(self.tareas_actuales)

        #Iniciar el hilo monitor (verifica cada 5 segundos)
        self.monitor_hilo = MonitorXML(self.nombre_archivo, 5, self)
        self.monitor_hilo.start()
                
    def crear_widgets(self): 
        """Define y coloca los elementos de la interfaz (widgets).""" 
        contenedor_principal = ttk.Frame(self.ventana, padding="10") 
        contenedor_principal.pack(fill='both', expand=True) 
         
        ttk.Label(contenedor_principal, text="Reporte de Tareas", font=("Helvetica", 16, "bold")).pack(pady=10) 
         
        # Crear la Tabla (Treeview) 
        columnas = ("ID", "Fecha", "Hora", "Descripción", "Estado") 
        self.tabla = ttk.Treeview(contenedor_principal, columns=columnas, show='headings') 
         
        for col in columnas: 
            self.tabla.heading(col, text=col) 
            if col == "Descripción": 
                self.tabla.column(col, width=250, anchor='w') 
            else: 
                self.tabla.column(col, width=80, anchor='center') 
         
        self.tabla.pack(fill='both', expand=True) 
 
        # Botón para futura funcionalidad 
        boton_agregar = ttk.Button( 
            contenedor_principal,  
            text="  Agregar Nueva Tarea") 
        boton_agregar.pack(pady=15) 
         
    def actualizar_tabla(self, nuevas_tareas): 
        self.tareas_actuales = nuevas_tareas 

        #1. Limpiar tabla existente
        for item in self.tabla.get_children():
            self.tabla.delete(item)
              
        #2. Llenar la tabla con los nuevos datos 
        for tarea in self.tareas_actuales: 
            datos = tarea.obtener_datos_para_tabla() 
            self.tabla.insert('', tk.END, values=datos) 
             
         
    def cerrar_aplicacion(self): 
        """Detiene el hilo antes de cerrar la ventana y destruye la GUI."""
        if self.monitor_hilo:
            self.monitor_hilo.detener()
            self.monitor_hilo.join()
            print("MonitorXML detenido correctamente.")
        self.ventana.destroy
         
    def iniciar(self): 
        """Inicia el bucle principal de la aplicación Tkinter.""" 
        self.ventana.mainloop() 