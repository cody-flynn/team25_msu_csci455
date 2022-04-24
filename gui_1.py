import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # Set columns
        self.cols = 1

        # Create a second gridlayout
        self.top_grid = GridLayout()
        # Set number of columns in our new top_grid
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="func_1: "))
        # Add Input Box
        self.func_1 = TextInput(multiline=True)
        self.top_grid.add_widget(self.func_1)

        self.top_grid.add_widget(Label(text="func_2: "))
        # Add Input Box
        self.func_2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.func_2)

        self.top_grid.add_widget(Label(text="func_3: "))
        # Add Input Box
        self.func_3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.func_3)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.run = Button(text="Run", font_size=32)
        # Bind the button
        self.run.bind(on_press=self.press)
        self.add_widget(self.run)

    def press(self, instance):
        func_1 = self.func_1.text
        func_2 = self.func_2.text
        func_3 = self.func_3.text

        # print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # Print it to the screen
        self.add_widget(Label(text=f' running {func_1}, {func_2} {func_3}!'))

        # Clear the input boxes
        self.func_1.text = ""
        self.func_2.text = ""
        self.func_3.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
