from Paciente import *
from Colas import *
from Gestor import *

cola_admision = Cola()
cola_general_urgente = Cola()
cola_general_no_urgente = Cola()
cola_especialidad_urgente = Cola()
cola_especialidad_no_urgente = Cola()
consulta_general = Consulta()
consulta_especialidad = Consulta()
prioridad_activa = []


with open(r"C:\Users\ramon\Documents\Practica_2_Prog\patients0.txt", "r", encoding="utf-8") as file:
    for linea in file:
        datos = linea.strip().split(" ")
        IDPAC = datos[0]
        tipo_consulta = datos[1]
        urgencia = datos[2]
        tiempo_estimado = int(datos[3])

        paciente = Patient(IDPAC, tipo_consulta, urgencia, tiempo_estimado)

        cola_admision.enqueue(paciente)

gestor_turnos = Gestor_Turnos(consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente, prioridad_activa, 0)
while not cola_admision.is_empty():    
    gestor_turnos.avanzar_tiempo()
    if (gestor_turnos._tiempo -1) % 3 == 0:
        gestor_turnos.asignar_cola(cola_admision.dequeue())
        gestor_turnos.asignar_consulta()
    
    

    
    


        



    
