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
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket], vip_flag: bool):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.dinero = dinero
        self.tickets = tickets
        self.vip_flag = vip_flag

    def comprar_ticket(self, atraccion: 'Atraccion', parque: 'Parque')-> None:
        if atraccion.estado:
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
        if atraccion.estado:
            atraccion.cola.append(self.nombre)
            print(f"{self.nombre} se ha puesto en la cola para la atraccion {atraccion.nombre}.")

#============================================================================================================
class VisitanteVip(Visitante):
    def __init__(self, nombre: str, edad: int, altura: int, dinero: float, tickets: list[Ticket], vip_flag: bool):
        super().__init__(nombre, edad, altura, dinero, tickets, vip_flag)
    
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
                    print(f"{self.cola[0]} entro en la atraccion {self.nombre}")
                    self.cola.pop(0)
            if cont_cola == 0:
                print(f"no hay nadie en la cola para la atraccion {self.nombre}")
            if cont_cola > self.capacidad:
                for _ in range(self.capacidad):
                    print(f"{self.cola[0]} entro en la atraccion {self.nombre}")
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
        if atraccion.estado == True:
            if atraccion.verificar_restricciones(visitante):
                visitante.comprar_ticket(atraccion, self)
                return
        else:
            print(f"{atraccion.nombre} no esta activa.")

    def calcular_venta(self, ticket: 'Ticket')-> None:
        self.venta_total += ticket.precio
        self.ventas.append(ticket)

    def resumen_de_ventas(self, dia: date)-> None:
        ingresos_por_atraccion = {}
        for venta in self.ventas:
            if venta.atraccion not in ingresos_por_atraccion:
                ingresos_por_atraccion[venta.atraccion] = {'tickets': 0, 'ingresos': 0.0}

            ingresos_por_atraccion[venta.atraccion]['tickets'] += 1
            ingresos_por_atraccion[venta.atraccion]['ingresos'] += venta.precio
        
        for atraccion in ingresos_por_atraccion:
            tickets_vendidos = ingresos_por_atraccion[atraccion]['tickets']
            ingresos = ingresos_por_atraccion[atraccion]['ingresos']
            print(f"Atracción: {atraccion}, Tickets vendidos: {tickets_vendidos}, Ingresos: {ingresos:.2f} USD")

        print(f"Total de ingresos del día: {self.venta_total:.2f} USD")

#============================================================================================================

#Aqui finalizan las clases :P
#cree estas variables con chatgpt para q sea mas aleatorio :D
visitante_0 = Visitante("Felipe", 19, 172, 30.2, [], False)
visitante_1 = Visitante("Camila", 22, 165, 50.0, [], False)
visitante_2 = Visitante("Juan", 25, 180, 40.5, [], False)

visitante_3 = Visitante("Diego", 7, 105, 38.6, [], False)
visitante_4 = Visitante("Antonio", 6, 100, 48.7, [], False)
visitante_5 = Visitante("Maria", 9, 110, 29.3, [], False)


visitante_vip_1 = VisitanteVip("Alejandro", 25, 180, 50.0, [], True)
visitante_vip_2 = VisitanteVip("Sofía", 30, 165, 70.0, [], True)
visitante_vip_3 = VisitanteVip("Leo", 21, 194, 57.0, [], True)

noria = Atraccion("Noria", 10, 10, True, [], 8.0)  
carrusel = Atraccion("Carrusel", 8, 5, True, [], 6.0)
torre_caida = Atraccion("Torre de Caída", 10, 10, False, [], 16.0)  

infantil = Atraccion_Infantil("Atraccion Infantil", 10, 8, True, [], 5.0)
raptor = Montanha_Rusa("Raptor", 8, 12, True, [], 15.0, 80, 150, 500)

fantasilandia = Parque("Fantasilandia", [noria, carrusel, torre_caida, infantil, raptor], 0, [])

print(f"Bienvenido a {fantasilandia.nombre}, Los juegos que estan activos son los siguientes:\n")
fantasilandia.consultar_juegos_activos()

print(f"\n\nLos visitanes compran sus tickets para los juegos:\n")
fantasilandia.cobrar_ticket(visitante_0, raptor)
fantasilandia.cobrar_ticket(visitante_1, infantil)
fantasilandia.cobrar_ticket(visitante_2, torre_caida)
fantasilandia.cobrar_ticket(visitante_2, raptor)
fantasilandia.cobrar_ticket(visitante_3, infantil)
fantasilandia.cobrar_ticket(visitante_4, carrusel)
fantasilandia.cobrar_ticket(visitante_5, infantil)
fantasilandia.cobrar_ticket(visitante_vip_1, carrusel)
fantasilandia.cobrar_ticket(visitante_vip_2, raptor)
fantasilandia.cobrar_ticket(visitante_vip_3, carrusel)

print(f"\n\nLos visitanes van a hacer cola para la atraccion:\n")
visitante_0.hacer_cola(raptor)
visitante_1.hacer_cola(infantil)
visitante_2.hacer_cola(torre_caida)
visitante_2.hacer_cola(raptor)
visitante_3.hacer_cola(infantil)
visitante_4.hacer_cola(carrusel)
visitante_5.hacer_cola(infantil)
visitante_vip_1.hacer_cola(carrusel)
visitante_vip_2.hacer_cola(raptor)
visitante_vip_3.hacer_cola(carrusel)


print(f"\n\nInicia la ronda de los juegos:\n")
noria.iniciar_ronda()
carrusel.iniciar_ronda()
torre_caida.iniciar_ronda()
infantil.iniciar_ronda()
raptor.iniciar_ronda()



