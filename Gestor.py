
class Gestor_Turnos:
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
        self._timpo = tiempo




    def __init__(self, consulta_general, consulta_especialidad, cola_general_urgente, cola_general_no_urgente, cola_especialidad_urgente, cola_especialidad_no_urgente, tiempo: int=1):
        self._tiempo = tiempo
        self._cola_general_urgente = cola_general_urgente
        self._cola_general_no_urgente = cola_general_no_urgente
        self._cola_especialidad_urgente = cola_especialidad_urgente
        self._cola_especialidad_no_urgente = cola_especialidad_no_urgente



    def avanzar_tiempo(self):
        self._tiempo += 1
        self._cola_general_urgente._tiempo += 1
        self._cola_general_no_urgente._tiempo += 1
        self._cola_especialidad_urgente._tiempo += 1
        self._cola_especialidad_no_urgente._tiempo += 1
        self._consulta_general._tiempo += 1
        self._consulta_especialidad._tiempo += 1


    def asignar_consulta(self):
        """
        Método que asigna una consulta a un paciente
        """
        if consulta_general.consulta_acabada()
            if cola_general_urgente.is_empty():
                paciente = cola_general_no_urgente.first()
                if self._tiempo - paciente._tiempo_llegada > 7:
                    paciente._prioridad_activa = True   
                consulta_general.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC} entra general/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            else:
                paciente = cola_general_urgente.first()
                if paciente._prioridad_activa:
                    print(f"{self._tiempo}: Priorización aplicada {paciente._IDPac} ")
                consulta_general.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC}} entra general/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
        if consulta_especialidad.consulta_acabada()
            if cola_especialidad_urgente.is_empty():
                paciente = cola_especialidad_no_urgente.first()
                if self._tiempo - paciente._tiempo_llegada > 7:
                    paciente._prioridad_activa = True
                consulta_especialidad.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC}} entra especialidad/not priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
            else:
                paciente = cola_especialidad_urgente.first()
                if paciente._prioridad_activa:
                    print(f"{self._tiempo}: Priorización aplicada {paciente._IDPac} ")
                consulta_especialidad.enqueue(paciente)
                print(f"{self._tiempo}: {paciente._IDPAC}} entra especialidad/priority ADM:{paciente._tiempo_llegada}, INI: {self._tiempo}, EST: {paciente._tiempo_estimado}")
   
    def asignar_cola(self, paciente):
        """
        Método que asigna una cola a un paciente
        """

        paciente._tiempo_llegada = self._contador_tiempo._tiempo

       if paciente._prioridad_activa:
            if paciente._urgencia == "not priority"
                paciente._urgencia = "priority"
                print(f"{self._tiempo}: Priorización activa {IDPac} ")

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

    




        
    
    
