from datetime import date

class Visitante:
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []

    def comprar_ticket(self, atraccion):
        ...
    
    def entregar_ticket(self, atraccion):
        for ticket in self.tickets:
            if ticket.atraccion == atraccion.nombre:
                self.tickets.remove(ticket)

    def hacer_cola(self, atraccion):
        atraccion.cola.append(self.nombre)
        print(f"{self.nombre} se ha puesto en la cola para la atraccion {atraccion.nombre}.")
    
#============================================================================================================
class Atraccion:
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola: str, precio: float):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = True      #activo o fuera de servicio
        self.cola = []
        self.precio = precio

    def iniciar_ronda(self):
        if self.estado == True:
            ...
        else:
            print(f"la atraccion {self.nombre} esta fuera de servicio")

    def comenzar_mantenimiento(self):
        print(f"La atraccion {self.nombre} entra en mantenimiento")
        self.estado = False

    def finalizar_mantenimiento(self):
        if self.estado == True:
            print(f"La atraccion {self.nombre} no estaba en mantenimiento")
        else:
            print(f"La atraccion {self.nombre} entra en mantenimiento")
            self.estado = True

#============================================================================================================
class Ticket:
    def __init__(self, numero: int, atraccion: str, precio: float, fecha_compra: date):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = date

#============================================================================================================

class Parque:
    def __init__(self, nombre: str, juegos: Atraccion):
        self.nombre = nombre
        self.juegos = []

    def consultar_juegos_activos(self):
        for atraccion in self.juegos: #hacer bien, consultar
            if atraccion.estado == True:
                ...

    def cobrar_ticket(self, visitante: Visitante, atraccion: Atraccion):
        ...

    def resumen_de_ventas(self, dia):
        ...

#============================================================================================================
class Atraccion_Infantil(Atraccion):
    def verificar_restricciones(self, visitante: Visitante):
        if visitante.edad > 10:
            print(f"El {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que excede la edad limite.")
            return False
        else:
            print(f"El {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================
class Monatanha_Rusa(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola, precio: float, velocidad_maxima: int, altura_maxima: int, extension: int):
        super().__init__(nombre, capacidad, duracion, estado, cola, precio)
        self.velocidad_maxima = velocidad_maxima
        self.altura_maxima = altura_maxima
        self.extension = extension

    def verificar_restricciones(self, visitante: Visitante):    
        if visitante.altura < 140:
            print(f"El {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que no cumple con la altura minima.")
            return False
        else:
            print(f"El {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================

#Aqui finalizan las clases :P

atraccion1 = Atraccion("Noria", 10, 10, True, None, 10)
atraccion2 = Atraccion("Tagada", 10, 10, True, None, 10)

fantasilandia = Parque("Fantasilandia", atraccion2)

