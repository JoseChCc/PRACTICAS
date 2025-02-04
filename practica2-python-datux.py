##         PRACTICA NRO2
## ALUMNO:JOSE EMERSON CHURATA CCAMA

# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados


class CONDUCTOR:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []


    def asignar_horario(self, horario):

        if horario in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {horario} asignado")
            return False

        self.horarios.append(horario)
        print(f"El horario {horario} ha sido asignado al conductor {self.nombre}")
        return True


class BUSS:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = None
        self.horario = None
        self.conductor = None
 
    def agregar_ruta(self, ruta):
        self.ruta = ruta
        print(f"La ruta {ruta} ha sido asignada al bus con la placa {self.placa}")


    def registrar_horario(self, horario):
        self.horario = horario
        print(f"El horario {horario} ha sido registrado para el bus de placa {self.placa}")

    
    def asignar_conductor(self, conductor):

        if self.horario is None:
            print(f"No puedes asignar un conductor si el bus {self.placa} no tiene horario")
            return False

        if conductor.asignar_horario(self.horario):
            self.conductor = conductor
            print(f"El conductor {conductor.nombre} ha sido asignado al bus de placa {self.placa}")
            return True

        return False


class ADMIN:
    def __init__(self):
        self.buses = []
        self.conductores = []

    
    def agregar_bus(self, placa):
        bus = BUSS (placa)
        self.buses.append(bus)
        print(f"El bus de placa {placa} ha sido agregado")
    

    def agregar_conductor(self, nombre):
        conductor = CONDUCTOR (nombre)
        self.conductores.append(conductor)
        print(f"El conductor {nombre} ha sido agregado")

    
    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus

        print(f"No se encontró un bus de placa {placa}")
        return None


    def buscar_conductor(self, nombre):
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        print(f"No se encontró un conductor llamado {nombre}")
        return None


    def menu(self):
        msg="""
        BIENVENIDO AL MENU
        1.AGREGAR BUS
        2.AGREGAR RUTA A BUS
        3.REGISTRAR HORARIO A BUS
        4.AGREGAR CONDUCTOR
        5.AGREGAR HORARIO A CONDUCTOR
        6.ASIGNAR BUS A CONDUCTOR
        7.SALIR
        """ 
        while True:
            print(msg)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                placa = input("Ingresar la placa del bus: ")
                self.agregar_bus(placa)

            elif opcion == "2":
                placa = input("Ingresar la placa del bus para la ruta: ")
                bus = self.buscar_bus(placa)

                if bus:
                    ruta = input("Ingresar la ruta del bus asignado: ")
                    bus.agregar_ruta(ruta)

            elif opcion == "3":
                placa = input("Ingresar la placa del bus para el horario: ")
                bus = self.buscar_bus(placa)

                if bus:
                    horario = input("Ingresar el horario al bus asignado (00:00-00:00): ")
                    bus.registrar_horario(horario)
                    
            elif opcion == "4":
                nombre = input("Ingresar el nombre del conductor: ")
                self.agregar_conductor(nombre)

            elif opcion == "5":
                nombre = input("Ingrese el nombre del conductor para indicar el horario: ")
                conductor = self.buscar_conductor(nombre)

                if conductor:
                    horario = input("Ingresar el horario al conductor asignado (00:00-00:00): ")
                    conductor.asignar_horario(horario)

            elif opcion == "6":
                placa = input("Ingresar la placa del bus para asignar el conductor: ")
                bus = self.buscar_bus(placa)

                if bus:
                    nombre_conductor = input("Ingrese el nombre del conductor asignado: ")
                    conductor = self.buscar_conductor(nombre_conductor)
                    if conductor:
                        bus.asignar_conductor(conductor)
                
            elif opcion == "7":
                print("ESPERAMOS VERLO PRONTO, BYEEEEE!!!")
                break
            else:
                print("==ERROR==, INSERTE LA OPCION NUEVAMENTE")


admin = ADMIN()
admin.menu()