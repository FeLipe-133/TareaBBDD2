from datetime import date
from typing import Union

#============================================================================================================
class Ticket:
    def __init__(self, numero: int, atraccion: str, precio: float, fecha_compra: date):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra

#============================================================================================================
class Visitante:
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket], vip_flag: bool):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets
        self.vip_flag = False

    def comprar_ticket(self, atraccion):
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(numero=len(self.tickets) + 1, atraccion=atraccion.nombre, precio=atraccion.precio, fecha_compra=date.today())
            self.tickets.append(ticket)
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
class VisitanteVip(Visitante):
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket], vip_flag: bool):
        super().__init__(nombre, edad, altura, dinero, tickets, vip_flag=True)
    
    def comprar_ticket(self, atraccion):
        ticket = Ticket(numero=len(self.tickets) + 1, atraccion=atraccion.nombre, precio=atraccion.precio, fecha_compra=date.today())
        self.tickets.append(ticket)
            
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
            cont_cola = len(self.cola)
            if cont_cola <= self.capacidad:
                for _ in range(cont_cola):
                    self.cola.pop(0)
            else:
                for _ in range(10):
                    self.cola.pop(0)
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
class Atraccion_Infantil(Atraccion):
    def verificar_restricciones(self, visitante: Union[Visitante, VisitanteVip]):
        if visitante.edad > 10:
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que excede la edad limite.")
            return False
        else:
            print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================
class Montanha_Rusa(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola, precio: float, velocidad_maxima: int, altura_maxima: int, extension: int):
        super().__init__(nombre, capacidad, duracion, estado, cola, precio)
        self.velocidad_maxima = velocidad_maxima
        self.altura_maxima = altura_maxima
        self.extension = extension

    def verificar_restricciones(self, visitante: Union[Visitante, VisitanteVip]):    
        if visitante.altura < 140:
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que no cumple con la altura minima.")
            return False
        else:
            print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================
class Parque:
    def __init__(self, nombre: str, juegos: list[Union[Atraccion, Atraccion_Infantil, Montanha_Rusa]]):
        self.nombre = nombre
        self.juegos = juegos

    def consultar_juegos_activos(self):
        for atraccion in self.juegos:
            if atraccion.estado == True:
                print(f"el juego '{atraccion}' esta activo.")

    def cobrar_ticket(self, visitante: Union[Visitante, VisitanteVip], atraccion: Atraccion):
        visitante.comprar_ticket(atraccion)

    #def resumen_de_ventas(self, dia):       

#============================================================================================================

#Aqui finalizan las clases :P
#visitante_ejemplo = Visitante("Felipe", 19, 130, 30.2, [])
#atraccion_ejemplo = Atraccion("Noria", 10, 10, True, [], 10)

#cree estas variables con chatgpt para q sea mas aleatorio :D
visitante_felipe = Visitante("Felipe", 19, 172, 30.2, [], False)
visitante_camila = Visitante("Camila", 22, 165, 50.0, [], False)
visitante_juan = Visitante("Juan", 25, 180, 40.5, [], False)
visitante_valentina = Visitante("Valentina", 21, 160, 35.7, [], False)
visitante_javier = Visitante("Javier", 12, 120, 60.3, [], False)
visitante_alejandra = Visitante("Alejandra", 18, 168, 25.8, [], False)
visitante_martin = Visitante("Martin", 30, 182, 55.0, [], False)
visitante_lucia = Visitante("Lucia", 24, 170, 45.9, [], False)
visitante_diego = Visitante("Diego", 7, 105, 38.6, [], False)
visitante_sophia = Visitante("Sophia", 20, 166, 32.1, [], False)
visitante_antonio = Visitante("Antonio", 6, 100, 48.7, [], False)
visitante_carolina = Visitante("Carolina", 23, 162, 37.5, [], False)
visitante_pablo = Visitante("Pablo", 29, 177, 52.4, [], False)
visitante_maria = Visitante("Maria", 9, 140, 29.3, [], False)
visitante_roberto = Visitante("Roberto", 31, 135, 62.0, [], False)

noria = Atraccion("Noria", 10, 10, True, [], 8.0)  
carrusel = Atraccion("Carrusel", 8, 5, True, [], 6.0) 
casa_del_terror = Atraccion("Casa del Terror", 6, 15, True, [], 14.4) 
tirolesa = Atraccion("Tirolesa", 4, 5, True, [], 20.0)
sillas_voladoras = Atraccion("Sillas Voladoras", 9, 7, True, [], 9.6)  
barco_pirata = Atraccion("Barco Pirata", 10, 8, True, [], 12.0) 
laberinto = Atraccion("Laberinto", 5, 10, True, [], 8.8) 
torre_caida = Atraccion("Torre de Caída", 10, 10, True, [], 16.0)  
mini_golf = Atraccion("Mini Golf", 8, 12, True, [], 7.2) 
paseo_en_bote = Atraccion("Paseo en Bote", 6, 20, True, [], 11.2)  

infantil = Atraccion_Infantil("Atraccion Infantil", 10, 8, True, [], 5.0)
raptor = Montanha_Rusa("Raptor", 8, 120, True, [], 15.0, 80, 150, 500)

fantasilandia = Parque("Fantasilandia", [noria, carrusel, casa_del_terror, tirolesa, sillas_voladoras, torre_caida, raptor])
DisnyLand = Parque("DisnyLand", [barco_pirata, laberinto, torre_caida, mini_golf, paseo_en_bote, noria, infantil])
