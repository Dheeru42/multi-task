from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
import time
class RAMAPP(MDApp):
    def build(self):
        return MDLabel(text=time.strftime("%H:%M:%S"),halign = "center")

RAMAPP().run()
    