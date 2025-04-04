from abc import ABC


class Patient(ABC):
    """
    Clase abstracta Paciente

    Atributos
    ---------- 
    IDPAC : int
        Identificador del paciente 
    tipo_consulta : str
        Tipo de consulta del paciente
    urgencia : str
        Urgencia del paciente
    tiempo_llegada : int
        Tiempo de llegada del paciente

    """

    def __init__(self, IDPAC, tipo_consulta, urgencia, tiempo_estimado: int = 1, tiempo_cola: int = 1, tiempo_consulta: int = 1, bloqueo_prioridad: bool = False):
        self._IDPAC = IDPAC
        self._tipo_consulta = tipo_consulta
        self._urgencia = urgencia
        self._tiempo_estimado = tiempo_estimado
        self._tiempo_llegada = tiempo_cola
        self._tiempo_entrada = tiempo_consulta
        self._bloqueo_prioridad = bloqueo_prioridad
    
    @property
    def IDPAC(self):
        """
        Getter del atributo IDPAC
        """
        return self._IDPAC
    @IDPAC.setter
    def IDPAC(self, IDPAC):
        """
        Setter del atributo IDPAC
        """
        self._IDPAC = IDPAC
    
    @property
    def tipo_consulta(self):
        """
        Getter del atributo tipo_consulta
        """
        return self._tipo_consulta
    @tipo_consulta.setter
    def tipo_consulta(self, tipo_consulta):
        """
        Setter del atributo tipo_consulta
        """
        self._tipo_consulta = tipo_consulta
    
    @property
    def urgencia(self):
        """
        Getter del atributo urgencia
        """
        return self._urgencia
    @urgencia.setter
    def urgencia(self, urgencia):
        """
        Setter del atributo urgencia
        """
        self._urgencia = urgencia
    
    @property
    def tiempo_estimado(self):
        """
        Getter del atributo tiempo_estimado
        """
        return self._tiempo_estimado
    @tiempo_estimado.setter
    def tiempo_estimado(self, tiempo_estimado):
        """
        Setter del atributo tiempo_estimado
        """
        self._tiempo_estimado = tiempo_estimado

    @property
    def tiempo_llegada(self):
        """
        Getter del atributo tiempo_llegada
        """
        return self._tiempo_llegada
    @tiempo_llegada.setter
    def tiempo_llegada(self, tiempo_llegada):
        """
        Setter del atributo tiempo_llegada
        """
        self._tiempo_llegada = tiempo_llegada

    @property
    def tiempo_entrada(self):
        """
        Getter del atributo tiempo_entrada
        """
        return self._tiempo_entrada
    @tiempo_entrada.setter
    def tiempo_entrada(self, tiempo_entrada):
        """
        Setter del atributo tiempo_entrada
        """
        self._tiempo_entrada = tiempo_entrada
    
    @property
    def bloqueo_prioridad(self):
        """
        Getter del atributo bloqueo_prioridad
        """
        return self._bloqueo_prioridad
    @bloqueo_prioridad.setter
    def bloqueo_prioridad(self, bloqueo_prioridad):
        """
        Setter del atributo bloqueo_prioridad
        """
        self._bloqueo_prioridad = bloqueo_prioridad    
    