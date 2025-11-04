from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        self.display = TextInput(
            text='0', 
            font_size=32,
            halign='right',
            readonly=True,
            multiline=False
        )
        main_layout.add_widget(self.display)
        
        buttons_layout = GridLayout(cols=4, spacing=5)
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        for button in buttons:
            btn = Button(text=button, font_size=24)
            btn.bind(on_press=self.on_button_press)
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_button_press(self, instance):
        current = self.display.text
        if instance.text == 'C':
            self.display.text = '0'
        elif instance.text == '=':
            try:
                self.display.text = str(eval(current))
            except:
                self.display.text = 'Error'
        else:
            self.display.text = instance.text if current == '0' else current + instance.text

if __name__ == '__main__':
    CalculatorApp().run()
