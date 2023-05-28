from Observer import Observer
from Model import Model
from View import View

class Controller(Observer):
    __model = None
    __view = None
    
    def __init__(self, model: Model, view: View):
        self.__model = model
        self.__view = view
        model.attach(self)

    def handleEvent(self):
        print("Handled!")

    