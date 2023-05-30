from Observer import Observer
from Model import Model
from Controller import Controller

class View(Observer):
 
    def __init__(self, model: Model):
        self.__model = model
        self.__controller = Controller(model,self)
        model.attach(self)

    def __init__(self, model: Model, controller: Controller):
        self.__model = model
        self.__controller = controller
        model.attach(self)

    def activate(self):
        print("Activate!")

    def display(self):
        print("Display!")

    def getModel(self):
        return self.__model
    
    def getController(self):
        return self.__controller
    
