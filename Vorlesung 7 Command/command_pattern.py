from __future__ import annotations
from abc import abstractmethod, ABC

class Ventilator:
    OFF = 0
    ON = 1
    FAST = 2

    def __init__(self):
        self.mode = self.OFF

    def aendere_mode(self, mode):
        if mode == self.OFF:
            print("Ventilator AUS")
        if mode == self.ON:
            print("Ventilator AN")
        if mode == self.FAST:
            print("Ventilator FAST")

   
class VentilatorCommand(ABC):
    def __init__(self, ventilator):
        self.ventilator = ventilator

    @abstractmethod
    def execute(self):
        pass

class Ventilator_aus(VentilatorCommand):
    def execute(self):
        self.ventilator.aendere_mode(self.ventilator.OFF)

class Ventilator_an(VentilatorCommand):
    def execute(self):
        self.ventilator.aendere_mode(self.ventilator.ON)




class Fernbedienung:
    def __init__(self):
        self.buttonMitte = None
        self.buttonUnten = None
        self.memory = []

    def setze_cmd_button_mitte(self, cmd):
        self.buttonMitte = cmd

    def setze_cmd_button_unten(self, cmd):
        self.buttonUnten = cmd

    def druecke_button_mitte(self):
        if self.buttonMitte != None:
            self.buttonMitte.execute()
            self.memory.append(self.buttonMitte)

    def druecke_button_unten(self):
        if self.buttonUnten != None:
            self.buttonUnten.execute()
            self.memory.append(self.buttonUnten)

    def replay(self):
        for cmd in self.memory:
            cmd.execute()

ventilator = Ventilator()
fbx3 = Fernbedienung()
fbx3.druecke_button_mitte()
fbx3.setze_cmd_button_mitte(Ventilator_aus(ventilator))
fbx3.setze_cmd_button_unten(Ventilator_an(ventilator))
fbx3.druecke_button_mitte()
fbx3.druecke_button_mitte()
fbx3.druecke_button_unten()
fbx3.druecke_button_mitte()
fbx3.druecke_button_mitte()
fbx3.druecke_button_unten()
print("Replay")
fbx3.replay()

