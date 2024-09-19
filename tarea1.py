from datetime import date

class Visitante:
    def __init__(self, nombre, edad, altura, dinero, tickets):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = []
    
class Atraccion:
    def __init__(self, nombre, capacidad, duracion, estado, cola):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = True      #activo o fuera de servicio
        self.cola = []

class Ticket:
    def __init__(self, numero, atraccion, precio, fecha_compra):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = date

class Parque:
    def __init__(self, nombre, juegos):
        self.nombre = nombre
        self.juegos = []

class Atraccion_Infantil(Atraccion):
    ...

class Monatanha_Rusa(Atraccion):
    ...