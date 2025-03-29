import pandas 
import Colas
import Paciente
import Gestor


def generar_estadisticas(datos_pacientes):
    """
    Genera estadísticas sobre la priorización aplicada y los tiempos de espera.
    """
    df = pandas.DataFrame(datos_pacientes)
    
    # Cálculo de número medio de citas con priorización aplicada
    prioridad_aplicada = df.groupby("type")["prioritization_applied"].mean()
    
    # Cálculo del tiempo medio de permanencia en colas de espera
    tiempos_espera = df.groupby(["type", "priority"])["waiting_time"].agg(['mean', 'std'])
    
    print("****************** NÚMERO MEDIO DE CITAS DE PACIENTES CON PRIORIZACIÓN APLICADA ******************")
    print(prioridad_aplicada, "\n")
    
    print("****************** TIEMPO MEDIO DE PERMANENCIA EN COLAS DE ESPERA ******************")
    print(tiempos_espera)

datos_pacientes = [
    {"type": "general", "priority": "no_priority", "prioritization_applied": 0.142857, "waiting_time": 11},
    {"type": "general", "priority": "priority", "prioritization_applied": 0, "waiting_time": 2.666667},
    {"type": "specialist", "priority": "no_priority", "prioritization_applied": 0, "waiting_time": 0},
    {"type": "specialist", "priority": "priority", "prioritization_applied": 0, "waiting_time": 0}
]

generar_estadisticas(datos_pacientes)
         


# with open(r"C:\Users\Usuario\Desktop\programacion2\p2\patients0.txt", "r", encoding="utf-8") as file:
#     for linea in file:
#         datos = linea.strip().split(" ")
#         IDPAC = str(datos[0])
#         tipo_consulta = datos[1]
#         urgencia = datos[2]
#         tiempo_estimado = int(datos[3])
#         paciente = Patient(IDPAC, tipo_consulta, urgencia, tiempo_estimado)
#         cola_admision.enqueue(paciente)

# gestor_turnos = Gestor_Turnos(cola_admision, consulta_general, consulta_especialidad, 
#                              cola_general_urgente, cola_general_no_urgente, 
#                              cola_especialidad_urgente, cola_especialidad_no_urgente, 
#                              prioridad_activa, 0)

# while not cola_admision.is_empty() or not consulta_general.is_empty() or not consulta_especialidad.is_empty():    
#     gestor_turnos.avanzar_tiempo()
#     if (gestor_turnos._tiempo - 1) % 3 == 0:
#         if not cola_admision.is_empty():
#             gestor_turnos.asignar_cola(cola_admision.dequeue())
#     gestor_turnos.asignar_consulta()

# def generar_estadisticas(datos_pacientes):
#     import pandas
#     df = pandas.DataFrame(datos_pacientes)
    
#     # Calculate prioritization statistics
#     prioridad_aplicada = df.groupby("type")["prioritization_applied"].mean().reset_index()
#     prioridad_aplicada = prioridad_aplicada.set_index('type')
    
#     # Calculate waiting time statistics
#     tiempos_espera = df.groupby(["type", "priority"])["waiting_time"].agg(['mean', 'std'])
    
#     # Format output to match exactly
#     print("******************** NÚMERO MEDIO DE CITAS DE PACIENTES CON PRIORIZACIÓN APLICADA ********************")
#     print(prioridad_aplicada.to_string(formatters={'prioritization_applied': '{:.6f}'.format}), "\n")
    
#     print("******************** TIEMPO MEDIO DE PERMANENCIA EN COLAS DE ESPERA ********************")
#     print(tiempos_espera.to_string(float_format=lambda x: "{:.6f}".format(x)))

# # Generate statistics from collected data
# generar_estadisticas(gestor_turnos._finished_patients)