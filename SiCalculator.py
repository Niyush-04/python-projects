# Import the necessary libraries
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import cmath


# Create a class for the simple interest calculator
class PolarFormConverter(GridLayout):

    # Initialize the layout
    def __init__(self, **kwargs):
        super(PolarFormConverter, self).__init__(**kwargs)
        self.cols = 2
        
        # Add the necessary widgets
        self.add_widget(Label(text="Realpart:"))
        self.Realpart = TextInput(multiline=False)
        self.add_widget(self.Realpart)
        
        self.add_widget(Label(text="imaginarypart:"))
        self.imaginary = TextInput(multiline=False)
        self.add_widget(self.imaginary)
        
        #self.add_widget(Label(text="Time (in years):"))
        #self.time = TextInput(multiline=False)
        #self.add_widget(self.time)
        
        self.add_widget(Label(text="Simple Interest:"))
        self.simple_interest = Label(text="")
        self.add_widget(self.simple_interest)
        
        self.add_widget(Label(text=""))
        self.calculate = Button(text="Calculate")
        self.add_widget(self.calculate)
        
        # Bind the button's on_press event to the calculate_simple_interest function
        self.calculate.bind(on_press=self.calculate_simple_interest)

    # Define the function to calculate simple interest
    def rectangular_to_polar(self, instance):
        Realpart = float(self.Realpart.text)
        imaginary = float(self.imaginary.text)
        angle = cmath.phase(self, instance)
        magnitude = abs(self, instance)
       
        
        rectangular_to_polar = (magnitude, angle*180/3.14)
        self.rectangular_to_polar.text = str(rectangular_to_polar)

# Create the app class
class SimpleInterestApp(App):
    def build(self):
        return PolarFormConverter()

# Run the app
if __name__ == "__main__":
    SimpleInterestApp().run()
