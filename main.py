import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.app import MDApp

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout,self).__init__(**kwargs)
    
        self.icon = 'fruit.jpg'
        # Set column
        self.cols = 1

        # Set middle column
        self.middle_grid = GridLayout()
        self.middle_grid.cols = 3

        # Set buttom column
        self.buttom_grid = GridLayout()
        self.buttom_grid.cols = 2

        # Add widgets picture
        self.add_widget(Image(source="fruitbig.jpg"))

        # Add widgets middle (Item) 
        self.Add_Item1 = Button(text='Add Item1', font_size = 20)
        self.middle_grid.add_widget(self.Add_Item1)
        self.Add_Item1.bind(on_press = self.press_Add_Item1)

        self.Item1 = Label(text = '0')
        self.middle_grid.add_widget(self.Item1)

        self.Subtract_Item1 = Button(text='Subtract Item1', font_size = 20)
        self.middle_grid.add_widget(self.Subtract_Item1)
        self.Subtract_Item1.bind(on_press = self.press_Subtract_Item1)

        self.Add_Item2 = Button(text='Add Item2' , font_size = 20)
        self.middle_grid.add_widget(self.Add_Item2)
        self.Add_Item2.bind(on_press = self.press_Add_Item2)

        self.Item2 = Label(text = '0')
        self.middle_grid.add_widget(self.Item2)

        self.Subtract_Item2 = Button(text='Subtract Item2', font_size = 20)
        self.middle_grid.add_widget(self.Subtract_Item2)
        self.Subtract_Item2.bind(on_press = self.press_Subtract_Item2)
        self.add_widget(self.middle_grid)

        # Add widgets buttom (Sum)
        self.Sum = Label(text = '0')
        self.buttom_grid.add_widget(self.Sum)

        self.Reset = Button(text='Click', font_size = 20)
        self.buttom_grid.add_widget(self.Reset)
        self.Reset.bind(on_press = self.press_reset)

        self.add_widget(self.buttom_grid)


    
    def press_Add_Item1 (self, instance):
        self.Item1.text = str(int(self.Item1.text) + 1 )
        self.Sum_text()

    def press_Subtract_Item1 (self, instance):
        if int(self.Item1.text) > 0 :
            self.Item1.text = str(int(self.Item1.text) - 1 )
            self.Sum_text()

    def press_Add_Item2 (self, instance):
        self.Item2.text = str(int(self.Item2.text) + 1 )
        self.Sum_text()

    def press_Subtract_Item2 (self, instance):
        if int(self.Item2.text) > 0 :
            self.Item2.text = str(int(self.Item2.text) - 1 )
            self.Sum_text()

    def press_reset (self, instance):
        self.Item1.text = '0'
        self.Item2.text = '0'   
        self.Sum_text()

    def Sum_text (self):
        self.Sum.text = str(int(self.Item1.text) + int(self.Item2.text))
    
class MainApp(App):
    def build(self):
        return MyGridLayout()
if __name__ == '__main__':
    MainApp().run()

