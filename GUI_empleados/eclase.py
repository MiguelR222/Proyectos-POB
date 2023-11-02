class cemp:
    def __init__(self, id=1, name="MIGUEL", ln="RUIZ", sexo='H', depto='A', sueldo=100):
        self.id= id
        self.name= name
        self.ln= ln
        self.sexo= sexo
        self.depto= depto
        self.sueldo= sueldo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, int):
            raise TypeError("El ID debe ser un numero")
        self.__id= id

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        if not isinstance(name,(str)):
            raise TypeError("El nombre de ser str")
        self.__name=name
    
    @property
    def ln(self):
        return self.__ln
    
    @ln.setter
    def ln(self,ln):
        if not isinstance(ln,(str)):
            raise TypeError("El apellido de ser str")
        self.__ln=ln
    
    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,sexo):
        if not isinstance(sexo,(str)):
            raise TypeError("El sexo debe ser del tipo str")
        self.__sexo=sexo

    @property
    def depto(self):
        return self.__depto
    
    @depto.setter
    def depto(self,depto):
        if not isinstance(depto,(str)):
            raise TypeError("El departamento debe ser str")
        self.__depto=depto

    @property
    def sueldo(self):
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        if not isinstance(sueldo, int):
            raise TypeError("El sueldo debe ser un número")
        self.__sueldo = sueldo
    
    def __str__(self):
        return f"{self.id},{self.name},{self.ln},{self.sexo},{self.depto},{self.sueldo}"
    