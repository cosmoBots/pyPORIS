from Observer import Observer
from Model import Model
from Controller import Controller
from View import View

class ViewController(View):
    __model = None
    __controller = None

    def __init__(self, model: Model):
        super.init(model)

    def __init__(self, model: Model, controller: Controller):
        super.init(model,controller)

    def activate(self):
        print("Activate!")

    def display(self):
        print("Display!")

    def getModel(self):
        return self.__model
    
    def handleEvent(self):
        print("Handled!")

