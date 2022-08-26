from xml.etree.ElementTree import canonicalize


class TV:
    __numTV=0
    def __init__(self,marca,estado):
        self.__marca=marca
        self.__canal=1
        self.__precio=500
        self.__estado=estado
        self.__volumen=1
        self.__control=None

        TV.__numTV+=1
    
    def getMarca(self):
        return self.__marca

    def setMarca(self,marca):
        self.__marca=marca
    
    def getControl(self):
        return self.__control

    def setControl(self,control):
        self.__control=control
    
    def getPrecio(self):
        return self.__precio

    def setPrecio(self,precio):
        self.__precio=precio
    
    def getVolumen(self):
        return self.__volumen

    def setVolumen(self,volumen):
        if self.__estado and volumen>=0 and volumen<=7:
            self.__volumen=volumen
    
    def getCanal(self):
        return self.__canal

    def setCanal(self,canal):
        if self.__estado and canal>=1 and canal<=120:
            self.__canal=canal

    @classmethod
    def getNumTV(cls):
        return cls.__numTV
        
    @classmethod
    def setNumTV(cls,numTV):
        cls.__numTV=numTV
    
    def turnOn(self):
        self.__estado=True

    def turnOff(self):
        self.__estado=False
    
    


    def canalUp(self):
        if self.__estado and self.__canal<120:
            self.__canal+=1
        
    def canalDown(self):
        if self.__estado and self.__canal>1:
            self.__canal-=1

    def volumenUp(self):
        if self.__estado and self.__volumen<7:
            self.__volumen+=1
        
    def volumenDown(self):
        if self.__estado and self.__volumen>0:
            self.__volumen-=1


    def getEstado(self):
        return self.__estado