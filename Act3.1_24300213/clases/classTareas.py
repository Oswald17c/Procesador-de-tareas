class Tarea:
    def __init__(self, iD, fechaCreacion, horaCreacion, descripcion, estado = "PENDIENTE"):
        self.__iD = iD
        self.__fechaCreacion = fechaCreacion
        self.__horaCreacion = horaCreacion
        self.__descripcion = descripcion
        self.__estado = estado
        
    #GETTERS
    def getid(self):
        return self.__iD
    def getfechaCreacion(self):
        return self.__fechaCreacion
    def gethoraCreacion(self):
        return self.__horaCreacion
    def getdescripcion(self):
        return self.__descripcion
    def getestado(self):
        return self.__estado

    #SETTERS
    def setid(self, iD):
        self.__iD = iD
    def setfechaCreacion(self, fechaCreacion):
        self.__fechaCreacion = fechaCreacion
    def sethoraCreacion(self, horaCreacion):
        self.__horaCreacion = horaCreacion
    def setdescripcion(self, descripcion):
        self.__descripcion = descripcion
    def setestado(self, estado):
        self.__estado = estado
    
    #METODO
    def __str__(self):
        return f"ID: {self.__iD} | Fecha de Creacion {self.__fechaCreacion} | Hora de Creacion {self.__horaCreacion} | Descripcion: {self.__descripcion} | Estado: {self.__estado}"
    
    def obtener_datos_para_tabla(self):
        return(self.__iD, self.__fechaCreacion, self.__horaCreacion, self.__descripcion, self.__estado)