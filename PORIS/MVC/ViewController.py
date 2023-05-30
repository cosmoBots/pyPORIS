from Observer import Observer
from Model import Model
from Controller import Controller
from View import View

class ViewController(View):

    def __init__(self, model: Model):
        super().__init__(model)
        
    def __init__(self, model: Model, controller: Controller):
        super().__init__(model,controller)
    
    def handleEvent(self):
        print("Handled!")

