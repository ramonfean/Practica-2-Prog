class Contador_Tiempo:
    def __init__(self, tiempo: int=1, gestor_turnos, consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente):
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
        gestor_turnos._tiempo += 1
        cola_general_urgente._tiempo += 1
        cola_general_no_urgente._tiempo += 1
        cola_especialidad_urgente._tiempo += 1
        cola_especialidad_no_urgente._tiempo += 1
        consulta_general._tiempo += 1
        consulta_especialidad._tiempo += 1
    
class Gestor_Turnos:
    def __init__(self, tiempo, cola_admision, consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente):
        self._tiempo = tiempo
        self._cola_admision = cola_admision
        self._cola_general_urgente = cola_general_urgente
        self._cola_general_no_urgente = cola_general_no_urgente
        self._cola_especialidad_urgente = cola_especialidad_urgente
        self._cola_especialidad_no_urgente = cola_especialidad_no_urgente

    def asignar_consulta(self):
        """
        Método que asigna una consulta a un paciente
        """
        if consulta_general.consulta_acabada()
            if cola_general_urgente.is_empty():
                paciente = consulta_general.enqueue(cola_general_no_urgente.first()) 
                print(f"{self._tiempo}: {paciente._IDPAC}} entra general/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            else:
                consulta_general.enqueue(cola_general_urgente.first())
                print(f"{self._tiempo}: {paciente._IDPAC}} entra general/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
        if consulta_especialidad.consulta_acabada()
            if cola_especialidad_urgente.is_empty():
                consulta_especialidad.enqueue(cola_especialidad_no_urgente.first())
                print(f"{self._tiempo}: {paciente._IDPAC}} entra especialidad/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            else:
                consulta_especialidad.enqueue(cola_especialidad_urgente.first())
                print(f"{self._tiempo}: {paciente._IDPAC}} entra especialidad/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_est
   
    def asignar_cola(self, paciente):
        """
        Método que asigna una cola a un paciente
        """

        paciente._tiempo_llegada = self._contador_tiempo._tiempo

        if paciente._tipo_consulta == "general":
            if paciente.urgencia == "priority":
                cola_general_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/priority EST:{paciente._tiempo_estimado}")
            else:
                cola_general_no_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/not priority EST:{paciente._tiempo_estimado}")
        else:
            if paciente.urgencia == "priority":
                cola_especialidad_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/priority EST:{paciente._tiempo_estimado}")
            else:
                cola_especialidad_no_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/not priority EST:{paciente._tiempo_estimado}")

    
    def cambiar_prioridad(self, paciente):
        """
        Método que cambia la prioridad de un paciente
        """
     



        
    
    
