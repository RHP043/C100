class Car(object):
    def __init__(self,model,color,brand,speed_limit):
        self.model = model
        self.color = color
        self.brand = brand
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("stopped")

    def accelerate(self):
        print("accelerate")   

    def changeGear(self):
        print("gear changed")

audi = Car("A6","Blue","Audi",66)
print(audi.start())
print(audi.changeGear())