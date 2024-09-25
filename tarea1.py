from datetime import date

class Visitante:
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[str]):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets

    def comprar_ticket(self, atraccion):
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            self.tickets.append(atraccion.nombre)
        else:
            print(f"{self.nombre} no tiene el dinero suficiente para comprar el ticket.")
    
    def entregar_ticket(self, atraccion):
        if atraccion.nombre in self.tickets:
            self.tickets.remove(atraccion.nombre)
        else:
            print(f"{self.nombre} no tiene el ticket para la atraccion {atraccion.nombre}.")


    def hacer_cola(self, atraccion):
        atraccion.cola.append(self.nombre)
        print(f"{self.nombre} se ha puesto en la cola para la atraccion {atraccion.nombre}.")
    
#============================================================================================================
class Atraccion:
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola: list[str], precio: float):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = True      #activo o fuera de servicio
        self.cola = cola
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
        self.fecha_compra = fecha_compra

#============================================================================================================

class Parque:
    def __init__(self, nombre: str, juegos: list[Atraccion]):
        self.nombre = nombre
        self.juegos = juegos

    def consultar_juegos_activos(self):
        for atraccion in self.juegos:
            if atraccion.estado == True:
                print(f"el juego {atraccion} esta activo.")

    def cobrar_ticket(self, visitante: Visitante, atraccion: Atraccion):
        ...

    def resumen_de_ventas(self, dia):
        ...

#============================================================================================================
class Atraccion_Infantil(Atraccion):
    def verificar_restricciones(self, visitante: Visitante):
        if visitante.edad > 10:
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que excede la edad limite.")
            return False
        else:
            print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
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
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que no cumple con la altura minima.")
            return False
        else:
            print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================

#Aqui finalizan las clases :P
visitante1 = Visitante("Felipe", 19, 130, 30.2, [])

atraccion1 = Atraccion("Noria", 10, 10, True, [], 10)
montanha = Monatanha_Rusa("Montanha Rusa", 15, 10, True, [], 10, 100, 30, 200)
infantil = Atraccion_Infantil("Infantil", 20, 10, True, [], 20)

fantasilandia = Parque("Fantasilandia", [atraccion1])

Atraccion_Infantil.verificar_restricciones(infantil, visitante1)
Monatanha_Rusa.verificar_restricciones(montanha, visitante1)
