from Paciente import *
from Colas import *
from Gestor import *

cola_admision = Cola_Admisión()
cola_general_urgente = Cola_Urgente()
cola_general_no_urgente = Cola_General_No_Urgente()
cola_especialidad_urgente = Cola_Urgente()
cola_especialidad_no_urgente = Cola_No_Urgente()


with open(r"C:\Users\ramon\Documents\Práctica 2 Prog\patients1.txt", "r", encoding="utf-8") as file:
    for linea in file:
        datos = linea.strip().split(" ")
        IDPAC = datos[0]
        tipo_consulta = datos[1]
        urgencia = datos[2]
        tiempo_estimado = datos[3]

        paciente = Patient(IDPAC, tipo_consulta, urgencia, tiempo_estimado)

        cola_admision.enqueue(paciente)

contador_tiempo = Contador_Tiempo(1)
gestor_turnos = Gestor_Turnos(cola_admision, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente)

while not cola_admision.is_empty():
    contador_tiempo.avanzar_tiempo()
    if (contador_tiempo._tiempo -1) % 3 == 0:
        gestor_turnos.asignar_cola(cola_admision.dequeue())
    


        



    
