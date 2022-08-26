class Control:
    def __init__(self):
        self.__tv=None

    def turnOn(self):
        self.__tv.turnOn()

    def turnOff(self):
        self.__tv.turnOff()

    def setCanal(self,canal):
        self.__tv.setCanal(canal)

    def canalUp(self):
        self.__tv.canalUp()
        
    def canalDown(self):
        self.__tv.canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()
        
    def volumenDown(self):
        self.__tv.volumenDown()

    def enlazar(self,tv):
        self.__tv=tv
        tv.setControl(self)

    def getTv(self):
        return self.__tv

    def setTv(self,tv):
        self.__tv=tv