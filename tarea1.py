from datetime import date

#============================================================================================================
class Ticket:
    def __init__(self, numero: int, atraccion: str, precio: float, fecha_compra: date):
        self.numero = numero
        self.atraccion = atraccion
        self.precio = precio
        self.fecha_compra = fecha_compra

#============================================================================================================
class Visitante:
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket]):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets

    def comprar_ticket(self, atraccion: 'Atraccion', parque: 'Parque')-> None:
        if self.dinero >= atraccion.precio:
            self.dinero -= atraccion.precio
            ticket = Ticket(numero=len(self.tickets) + 1, atraccion=atraccion.nombre, precio=atraccion.precio, fecha_compra=date.today())
            self.tickets.append(ticket)
            parque.calcular_venta(ticket)
            print(f"El visitante {self.nombre} compro un ticket para {atraccion.nombre}")
        else:
            print(f"{self.nombre} no tiene el dinero suficiente para comprar el ticket.")
    
    def entregar_ticket(self, atraccion: 'Atraccion')-> None:
        for ticket in self.tickets:
            if atraccion.nombre == ticket.atraccion:
                print(f"{self.nombre} ha entregado su ticket para la atracción {atraccion.nombre}.")
                self.tickets.remove(ticket)
                return
        print(f"{self.nombre} no tiene el ticket para la atraccion {atraccion.nombre}.")

    def hacer_cola(self, atraccion: 'Atraccion')-> None:
        atraccion.cola.append(self.nombre)
        print(f"{self.nombre} se ha puesto en la cola para la atraccion {atraccion.nombre}.")

#============================================================================================================
class VisitanteVip(Visitante):
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket]):
        super().__init__(nombre, edad, altura, dinero, tickets)
    
    def comprar_ticket(self, atraccion: 'Atraccion', parque: 'Parque')-> None:
        ticket = Ticket(numero=len(self.tickets) + 1, atraccion=atraccion.nombre, precio=atraccion.precio, fecha_compra=date.today())
        self.tickets.append(ticket)
        parque.calcular_venta(ticket)
        print(f"El visitante {self.nombre} compro un ticket para {atraccion.nombre}")
            
#============================================================================================================
class Atraccion:
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola: list[str], precio: float):
        self.nombre = nombre
        self.capacidad = capacidad
        self.duracion = duracion
        self.estado = estado      #activo o fuera de servicio
        self.cola = cola
        self.precio = precio

    def iniciar_ronda(self)-> None:
        if self.estado == True:
            cont_cola = len(self.cola)
            if cont_cola <= self.capacidad:
                for _ in range(cont_cola):
                    self.cola.pop(0)
            else:
                for _ in range(self.capacidad):
                    self.cola.pop(0)
        else:
            print(f"la atraccion {self.nombre} esta fuera de servicio")

    def comenzar_mantenimiento(self)-> None:
        print(f"La atraccion {self.nombre} entra en mantenimiento")
        self.estado = False

    def finalizar_mantenimiento(self)-> None:
        if self.estado == True:
            print(f"La atraccion {self.nombre} no estaba en mantenimiento")
        else:
            print(f"La atraccion {self.nombre} termina su mantenimiento")
            self.estado = True
        
    def verificar_restricciones(self, visitante: 'Visitante')-> bool:
        return True

#============================================================================================================
class Atraccion_Infantil(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola: list[str], precio: float):
        super().__init__(nombre, capacidad, duracion, estado, cola, precio)

    def verificar_restricciones(self, visitante: 'Visitante')-> bool:
        if visitante.edad > 10:
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que excede la edad limite.")
            return False
        else:
            print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
            return True

#============================================================================================================
class Montanha_Rusa(Atraccion):
    def __init__(self, nombre: str, capacidad: int, duracion: int, estado: bool, cola: list[str], precio: float, velocidad_maxima: int, altura_maxima: int, extension: int):
        super().__init__(nombre, capacidad, duracion, estado, cola, precio)
        self.velocidad_maxima = velocidad_maxima
        self.altura_maxima = altura_maxima
        self.extension = extension

    def verificar_restricciones(self, visitante: 'Visitante')-> bool:    
        if visitante.altura < 140:
            print(f"El visitante {visitante.nombre} no tiene permitido ingresar a la atraccion {self.nombre}, ya que no cumple con la altura minima.")
            return False      
        print(f"El visitante {visitante.nombre} puede acceder a la atraccion {self.nombre}")
        return True

#============================================================================================================
class Parque:
    def __init__(self, nombre: str, juegos: list[Atraccion], venta_total: float, ventas: list[Ticket]):
        self.nombre = nombre
        self.juegos = juegos
        self.venta_total = venta_total
        self.ventas = ventas

    def consultar_juegos_activos(self)-> None:
        for atraccion in self.juegos:
            if atraccion.estado == True:
                print(f"el juego '{atraccion.nombre}' esta activo.")

    def cobrar_ticket(self, visitante: 'Visitante', atraccion: 'Atraccion')-> None:
        if atraccion.verificar_restricciones(visitante):
            visitante.comprar_ticket(atraccion, self)
            return
        print(f"no se pudo comprar el ticket para la atraccion {atraccion.nombre}")

    def calcular_venta(self, ticket: 'Ticket')-> None:
        self.venta_total += ticket.precio
        self.ventas.append(ticket)

    def resumen_de_ventas(self, dia)-> None:
        ...

#============================================================================================================

#Aqui finalizan las clases :P
#visitante_ejemplo = Visitante("Felipe", 19, 130, 30.2, [])
#atraccion_ejemplo = Atraccion("Noria", 10, 10, True, [], 10)

#cree estas variables con chatgpt para q sea mas aleatorio :D
visitante_felipe = Visitante("Felipe", 19, 172, 30.2, [])
noria = Atraccion("Noria", 10, 10, True, [], 8.0)  
carrusel = Atraccion("Carrusel", 8, 5, True, [], 6.0) 
casa_del_terror = Atraccion("Casa del Terror", 6, 15, True, [], 14.4) 
tirolesa = Atraccion("Tirolesa", 4, 5, False, [], 20.0)
raptor = Montanha_Rusa("Raptor", 8, 120, True, [], 15.0, 80, 150, 500)
fantasilandia = Parque("Fantasilandia", [noria, carrusel, casa_del_terror, tirolesa, raptor], 0, [])

fantasilandia.consultar_juegos_activos()
fantasilandia.cobrar_ticket(visitante_felipe, noria)
visitante_felipe.entregar_ticket(noria)

# visitante_camila = Visitante("Camila", 22, 165, 50.0, [])
# visitante_juan = Visitante("Juan", 25, 180, 40.5, [])
# visitante_valentina = Visitante("Valentina", 21, 160, 35.7, [])
# visitante_javier = Visitante("Javier", 12, 120, 60.3, [])
# visitante_alejandra = Visitante("Alejandra", 18, 168, 25.8, [])
# visitante_martin = Visitante("Martin", 30, 182, 55.0, [])
# visitante_lucia = Visitante("Lucia", 24, 170, 45.9, [])
# visitante_sophia = Visitante("Sophia", 20, 166, 32.1, [])
# visitante_carolina = Visitante("Carolina", 23, 162, 37.5, [])
# visitante_pablo = Visitante("Pablo", 29, 177, 52.4, [])
# visitante_roberto = Visitante("Roberto", 31, 135, 62.0, [])

# visitante_diego = Visitante("Diego", 7, 105, 38.6, [])
# visitante_antonio = Visitante("Antonio", 6, 100, 48.7, [])
# visitante_maria = Visitante("Maria", 9, 110, 29.3, [])
# visitante_santiago = Visitante("Santiago", 6, 115, 20.0, [])
# visitante_valeria = Visitante("Valeria", 7, 120, 25.5, [])
# visitante_renato = Visitante("Renato", 8, 130, 15.3, [])
# visitante_mia = Visitante("Mía", 5, 110, 18.0, [])
# visitante_lucas = Visitante("Lucas", 9, 135, 30.0, [])

# visitante_vip_alejandro = VisitanteVip("Alejandro", 25, 180, 50.0, [])
# visitante_vip_sofia = VisitanteVip("Sofía", 30, 165, 70.0, [])
# visitante_vip_gabriel = VisitanteVip("Gabriel", 22, 175, 100.5, [])
# visitante_vip_isabella = VisitanteVip("Isabella", 27, 168, 85.0, [])
# visitante_vip_fernando = VisitanteVip("Fernando", 31, 182, 60.0, [])
# visitante_vip_ana = VisitanteVip("Ana", 29, 160, 45.0, [])
# visitante_vip_pablo = VisitanteVip("Pablo", 24, 178, 55.0, [])
# visitante_vip_camila = VisitanteVip("Camila", 35, 170, 90.0, [])
# visitante_vip_mateo = VisitanteVip("Mateo", 19, 177, 65.0, [])
# visitante_vip_lucia = VisitanteVip("Lucía", 26, 172, 80.0, [])
# visitante_vip_nicolas = VisitanteVip("Nicolás", 32, 185, 75.0, [])
# visitante_vip_valentina = VisitanteVip("Valentina", 28, 163, 40.0, [])
# visitante_vip_juan = VisitanteVip("Juan", 23, 174, 95.0, [])
# visitante_vip_renata = VisitanteVip("Renata", 20, 169, 55.0, [])
# visitante_vip_diego = VisitanteVip("Diego", 33, 180, 68.0, [])

#noria = Atraccion("Noria", 10, 10, True, [], 8.0)  
# carrusel = Atraccion("Carrusel", 8, 5, True, [], 6.0) 
# casa_del_terror = Atraccion("Casa del Terror", 6, 15, True, [], 14.4) 
# tirolesa = Atraccion("Tirolesa", 4, 5, True, [], 20.0)
# sillas_voladoras = Atraccion("Sillas Voladoras", 9, 7, True, [], 9.6)  
# barco_pirata = Atraccion("Barco Pirata", 10, 8, True, [], 12.0) 
# laberinto = Atraccion("Laberinto", 5, 10, True, [], 8.8) 
# torre_caida = Atraccion("Torre de Caída", 10, 10, True, [], 16.0)  
# mini_golf = Atraccion("Mini Golf", 8, 12, True, [], 7.2) 
# paseo_en_bote = Atraccion("Paseo en Bote", 6, 20, True, [], 11.2)  

# infantil = Atraccion_Infantil("Atraccion Infantil", 10, 8, True, [], 5.0)
# raptor = Montanha_Rusa("Raptor", 8, 120, True, [], 15.0, 80, 150, 500)

#fantasilandia = Parque("Fantasilandia", [noria, carrusel, casa_del_terror, tirolesa, sillas_voladoras, torre_caida, raptor])
# DisnyLand = Parque("DisnyLand", [barco_pirata, laberinto, torre_caida, mini_golf, paseo_en_bote, noria, infantil])
