
class Gestor_Turnos:
    """
    Clase Gestor_Turnos que gestiona la asignación de turnos a los pacientes en un sistema de salud.
    Atributos
    ----------
    cola_admision : Cola
        Cola de admisión de pacientes
    consulta_general : Consulta
        Cola de consulta general
    consulta_especialidad : Consulta
        Cola de consult de especialidad
    cola_general_urgente : Cola
        Cola de pacientes egenerales de urgencia
    cola_general_no_urgente : Cola
        Cola de pacientes generales no urgentes
    cola_especialidad_urgente : Cola
        Cola de pacientes de especialidad urgentes
    cola_especialidad_no_urgente : Cola
        Cola de pacientes nde especialidad no urgentes
    prioridad_activa : list 
        Lista de pacientes con prioridad activa
    tiempo : int
        Tiempo actual del sistema
    """

    def __init__(self, cola_admision, consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente, prioridad_activa, tiempo):
        
        self._cola_admision = cola_admision
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
    
    @property
    def tiempo(self):
        """
        Getter del atributo tiempo
        """
        return self._tiempo
    @tiempo.setter
    def tiempo(self, tiempo):
        """
        Setter del atributo tiempo
        """
    

    def avanzar_tiempo(self):
        """
        Método que avanza el tiempo del sistema
        
        """
        self._tiempo += 1
        self._cola_general_urgente.incrementar_tiempo()
        self._cola_general_no_urgente.incrementar_tiempo()
        self._cola_especialidad_urgente.incrementar_tiempo()
        self._cola_especialidad_no_urgente.incrementar_tiempo()
        self._consulta_general.incrementar_tiempo()
        self._consulta_especialidad.incrementar_tiempo()


    def acabar_consulta(self, cola):
        """
        Método que verifica si la consulta ha terminado

        Parámetros
        ----------
        cola : Cola
            Cola de pacientes en consulta
        
        Retorna
        -------
        bool
            True si la consulta ha terminado, False en caso contrario
        """

        if self._tiempo >= cola.first()._tiempo_consulta + cola.first()._tiempo_estimado: 
            paciente = cola.dequeue()
            print(f"{self._tiempo}: {paciente._IDPAC} sale {paciente._tipo_consulta}/{paciente._urgencia} ADM:{paciente._tiempo_cola}, INI: {paciente._tiempo_consulta}, EST./TOTAL: {paciente._tiempo_estimado}/{self._tiempo - paciente._tiempo_cola}") 
            return True
    
    def asignar_cola(self, paciente):
        """
        Método que asigna una cola a un paciente
        """

        if paciente._IDPAC in self._prioridad_activa and paciente._bloqueo_prioridad == False:
            if paciente._urgencia == "no_priority":
                paciente._urgencia = "priority"
                print(f"{self._tiempo}: Priorización activa {paciente._IDPAC} ")
                paciente._bloqueo_prioridad = True
                while paciente._IDPAC in self._prioridad_activa:
                    self._prioridad_activa.remove(paciente._IDPAC)
        

        if paciente._tipo_consulta == "general":
            if paciente.urgencia == "priority":
                self._cola_general_urgente.enqueue(paciente)
                paciente._tiempo_cola = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/priority EST:{paciente._tiempo_estimado}")
            else:
                self._cola_general_no_urgente.enqueue(paciente)
                paciente._tiempo_cola = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola general/no_priority EST:{paciente._tiempo_estimado}")
        else:
            if paciente.urgencia == "priority":
                self._cola_especialidad_urgente.enqueue(paciente)
                paciente._tiempo_cola= self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/priority EST:{paciente._tiempo_estimado}")
            else:
                self._cola_especialidad_no_urgente.enqueue(paciente)
                paciente._tiempo_cola = self._tiempo
                print(f"{self._tiempo}: {paciente._IDPAC} en cola especialidad/no_priority EST:{paciente._tiempo_estimado}")


    def asignar_consulta(self):
        """
        Método que asigna una consulta a un paciente

        """


        paciente = None

        if self._consulta_general.is_empty() or self.acabar_consulta(self._consulta_general):
            if self._cola_general_urgente:
                paciente = self._cola_general_urgente.dequeue()
                if self._tiempo - paciente._tiempo_cola > 7:
                        self._prioridad_activa.append(paciente._IDPAC)
                

            elif self._cola_general_no_urgente:
                paciente = self._cola_general_no_urgente.dequeue()
                if self._tiempo - paciente._tiempo_cola> 7:
                        self._prioridad_activa.append(paciente._IDPAC)
                      
     
            if paciente:
                paciente._tiempo_consulta = self._tiempo
                self._consulta_general.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra general/{paciente._urgencia} ADM:{paciente._tiempo_cola}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
                if paciente._IDPAC in self._prioridad_activa:
                    print(f"{self._tiempo}: Priorización activa {paciente._IDPAC} ")


        paciente = None
   
        if self._consulta_especialidad.is_empty() or self.acabar_consulta(self._consulta_especialidad):
            if self._cola_especialidad_urgente:
                paciente = self._cola_especialidad_urgente.dequeue()
                if self._tiempo - paciente._tiempo_cola > 7:
                        self._prioridad_activa.append(paciente._IDPAC)
            if self._cola_especialidad_no_urgente:
                paciente = self._cola_especialidad_no_urgente.dequeue()
                if self._tiempo - paciente._tiempo_cola > 7:
                        self._prioridad_activa.append(paciente._IDPAC)
            if paciente:
                paciente._tiempo_consulta = self._tiempo
                self._consulta_especialidad.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra specialist/{paciente._urgencia} ADM:{paciente._tiempo_cola}, INI: {paciente._tiempo_entrada}, EST: {paciente._tiempo_estimado}")
                if paciente._IDPAC in self._prioridad_activa:
                    print(f"{self._tiempo}: Priorización activa {paciente._IDPAC} ")


    





        
    
    
