class Contador_Tiempo:
    def __init__(self, tiempo):
        self._tiempo = tiempo
    
    @property
    def tiempo(self):
        """
        Getter de tiempo
        """
        return self._tiempo

    @tiempo.setter
    def tiempo(self, tiempo):
        """
        Setter de tiempo
        """
        self._tiempo = tiempo

    def avanzar_tiempo(self):
        """
        Método que avanza el tiempo en 1
        """
        self._tiempo += 1
        return self._tiempo
    
class Gestor_Turnos:
    def __init__(self, contador_tiempo, cola_admision, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente):
        contador_tiempo = contador_tiempo
        self._cola_admision = cola_admision
        self._cola_general_urgente = cola_general_urgente
        self._cola_general_no_urgente = cola_general_no_urgente
        self._cola_especialidad_urgente = cola_especialidad_urgente
        self._cola_especialidad_no_urgente = cola_especialidad_no_urgente
    
    def asignar_cola(self, paciente):
        """
        Método que asigna una cola a un paciente
        """

        paciente._tiempo_llegada = self._contador_tiempo._tiempo

        if paciente._tipo_consulta == "general":
            if paciente.urgencia == "priority":
                self._cola_general_urgente.enqueue(paciente)
            else:
                self._cola_general_no_urgente.enqueue(paciente)
        else:
            if paciente.urgencia == "priority":
                self._cola_especialidad_urgente.enqueue(paciente)
            else:
                self._cola_especialidad_no_urgente.enqueue(paciente)
    
