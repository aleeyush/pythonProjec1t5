from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageCalculatorMainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, MortgageCalculator", halign="center")


MortgageCalculatorMainApp().run()