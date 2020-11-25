class car(object):
    def __init__(self,model,color,speedlimit,brand):
        self.color=color
        self.model=model
        self.speedlimit=speedlimit
        self.brand=brand

    def start(self):
        print("started")

    def stop(self):
        print("stopped")    

    def acceleration(self):
        print("accelration")

car1= car("M series","black",270,"BMW")
print(car1.acceleration())        
