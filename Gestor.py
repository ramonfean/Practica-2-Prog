
class Gestor_Turnos:

    def __init__(self, consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente, prioridad_activa, tiempo):
        
        self._cola_general_urgente = cola_general_urgente
        self._cola_general_no_urgente = cola_general_no_urgente
        self._cola_especialidad_urgente = cola_especialidad_urgente
        self._cola_especialidad_no_urgente = cola_especialidad_no_urgente
        self._consulta_general = consulta_general
        self._consulta_especialidad = consulta_especialidad
        self._prioridad_activa = prioridad_activa 
        self._tiempo = tiempo

    @property
    def prioridad_activa(self):
        """
        Getter del atributo prioridad_activa
        """
        return self._prioridad_activa
    @prioridad_activa.setter
    def prioridad_activa(self, prioridad_activa):
        """
        Setter del atributo prioridad_activa
        """
        self._prioridad_activa = prioridad_activa
    

    def avanzar_tiempo(self):
        self._tiempo += 1
        self._cola_general_urgente.incrementar_tiempo()
        self._cola_general_no_urgente.incrementar_tiempo()
        self._cola_especialidad_urgente.incrementar_tiempo()
        self._cola_especialidad_no_urgente.incrementar_tiempo()
        self._consulta_general.incrementar_tiempo()
        self._consulta_especialidad.incrementar_tiempo()


    def asignar_consulta(self):
        """
        Método que asigna una consulta a un paciente
        """
        if self._consulta_general.is_empty() or self._consulta_general.consulta_acabada():
            if self._cola_general_urgente.is_empty() and not self._cola_general_no_urgente.is_empty():
                paciente = self._cola_general_no_urgente.first()
                if self._tiempo - paciente._tiempo_llegada > 7:
                    self._prioridad_activa.append(paciente._IDPAC)    
                self._consulta_general.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra general/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            elif not self._cola_general_urgente.is_empty():
                paciente = self._cola_general_urgente.first()
                if paciente._IDPAC in self._prioridad_activa:
                    print(f"{self._tiempo}: Priorización aplicada {paciente._IDPac} ")
                self._consulta_general.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra general/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
        
        if self._consulta_especialidad.is_empty() or self._consulta_especialidad.consulta_acabada():
            if self._cola_especialidad_urgente.is_empty() and not self._cola_especialidad_no_urgente.is_empty():
                paciente = self._cola_especialidad_no_urgente.first()
                if self._tiempo - paciente._tiempo_llegada > 7:
                    self._prioridad_activa.append(paciente._IDPAC)
                self._consulta_especialidad.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra especialidad/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            elif not self._cola_especialidad_urgente.is_empty():
                paciente = self._cola_especialidad_urgente.first()
                if paciente._IDPAC in self._prioridad_activa:
                    print(f"{self._tiempo}: Priorización aplicada {paciente._IDPac} ")
                self._consulta_especialidad.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra especialidad/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
   
    def asignar_cola(self, paciente):
        """
        Método que asigna una cola a un paciente
        """

        paciente._tiempo_llegada = self._tiempo

        if paciente._IDPAC in self._prioridad_activa:
            if paciente._urgencia == "not priority":
                paciente._urgencia = "priority"
                print(f"{self._tiempo}: Priorización activa {paciente._IDPac} ")
                self._prioridad_activa.remove(paciente._IDPAC)

        if paciente._tipo_consulta == "general":
            if paciente.urgencia == "priority":
                self._cola_general_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/priority EST:{paciente._tiempo_estimado}")
            else:
                self._cola_general_no_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/not priority EST:{paciente._tiempo_estimado}")
        else:
            if paciente.urgencia == "priority":
                self._cola_especialidad_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/priority EST:{paciente._tiempo_estimado}")
            else:
                self._cola_especialidad_no_urgente.enqueue(paciente)
                paciente._tiempo_llegada = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/not priority EST:{paciente._tiempo_estimado}")

    




        
    
    
