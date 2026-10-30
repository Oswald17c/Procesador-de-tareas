import xml.etree.ElementTree as ET
from clases.classTareas import Tarea
import threading
import os 
import time

class ProcesadorTareas:
    def leer_xml_y_crear_tareas(self, archivo_xml):

        lista_de_tareas = []

        # Leer archivo XML
        arbol = ET.parse(archivo_xml)
        raiz = arbol.getroot()

        for tarea_xml in raiz.findall("Tarea"):

            id_tarea = tarea_xml.get("iD")

            fecha = tarea_xml.find("FechaCreacion").text
            hora = tarea_xml.find("HoraCreacion").text
            descripcion = tarea_xml.find("Descripcion").text
            estado = tarea_xml.find("Estado").text

            tarea = Tarea(id_tarea, fecha, hora, descripcion, estado)
            lista_de_tareas.append(tarea)

        return lista_de_tareas
    
#Clase de Hilo Monitor
class MonitorXML(threading.Thread):
        def __init__(self, nombre_archivo, intervalo, aplicacion):
            super().__init__()
            self.nombre_archivo = nombre_archivo
            self.intervalo = intervalo
            self.aplicacion = aplicacion # Referencia a la clase AplicacionTareas
            self.ultima_modificacion = 0
            self._detener_hilo = threading.Event()
        def run(self):
            """Método que se ejecuta al iniciar el hilo."""
            print(f"MonitorXML iniciado. Verificando cada {self.intervalo} segundos.")
            while not self._detener_hilo.is_set():
                try:
                    tiempo_actual = os.path.getmtime(self.nombre_archivo)

                    if tiempo_actual > self.ultima_modificacion:
                        if self.ultima_modificacion != 0:
                            print("¡Cambio detectado en el archivo XML! Actualizando tareas...")

                        self.ultima_modificacion = tiempo_actual    

                    # Usa la función de lectura de este módulo
                    procesador= ProcesadorTareas()
                    nuevas_tareas = procesador.leer_xml_y_crear_tareas(self.nombre_archivo)

                    # Llama al método de actualización de la GUI de forma segura
                    self.aplicacion.ventana.after(0, self.aplicacion.actualizar_tabla, nuevas_tareas)
                except FileNotFoundError:
                    pass # Ignorar temporalmente si el archivo no existe al inicio
                except Exception as e:
                    print(f"Error inesperado en el hilo MonitorXML: {e}")

            self._detener_hilo.wait(self.intervalo)

        def detener(self):
            """Detiene el bucle del hilo de forma segura."""
            self._detener_hilo.set()