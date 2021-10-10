class Car(object):
    def __init__(self,model,company,color,speedLimit):
        self.model = model,
        self.company = company,
        self.color = color,
        self.speedLimit = speedLimit
    def start(self):
        print("Started")
    def end(self):
        print("Ended")
#main
audi = Car("a8","Audi","Red","80")
print(audi.color)
print(audi.model)
audi.start()