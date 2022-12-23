# Import the necessary libraries
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# Create a class for the simple interest calculator
class SimpleInterestCalculator(GridLayout):

    # Initialize the layout
    def __init__(self, **kwargs):
        super(SimpleInterestCalculator, self).__init__(**kwargs)
        self.cols = 2
        
        # Add the necessary widgets
        self.add_widget(Label(text="Principal:"))
        self.principal = TextInput(multiline=False)
        self.add_widget(self.principal)
        
        self.add_widget(Label(text="Rate of Interest (%):"))
        self.rate = TextInput(multiline=False)
        self.add_widget(self.rate)
        
        self.add_widget(Label(text="Time (in years):"))
        self.time = TextInput(multiline=False)
        self.add_widget(self.time)
        
        self.add_widget(Label(text="Simple Interest:"))
        self.simple_interest = Label(text="")
        self.add_widget(self.simple_interest)
        
        self.add_widget(Label(text=""))
        self.calculate = Button(text="Calculate")
        self.add_widget(self.calculate)
        
        # Bind the button's on_press event to the calculate_simple_interest function
        self.calculate.bind(on_press=self.calculate_simple_interest)

    # Define the function to calculate simple interest
    def calculate_simple_interest(self, instance):
        principal = float(self.principal.text)
        rate = float(self.rate.text)
        time = float(self.time.text)
        
        simple_interest = (principal * rate * time) / 100
        self.simple_interest.text = str(simple_interest)

# Create the app class
class SimpleInterestApp(App):
    def build(self):
        return SimpleInterestCalculator()

# Run the app
if __name__ == "__main__":
    SimpleInterestApp().run()
