class car:
    def setBrand(self):
        self.brand = input("brand ")
    def setMaxspeed(self):
        self.maxspeed = input("max speed ")
    def printData(self):
        print("brand of this car is",self.brand,"with maxSpeed",self.maxspeed,"km/h")

i = car()
i.setBrand()
i.setMaxspeed()
i.printData()