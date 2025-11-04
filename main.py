from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label


class HelloApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.input_name = TextInput(
            hint_text="اكتب اسمك هنا",
            multiline=False,
            size_hint=(1, 0.2)
        )
        
        self.label = Label(text="أهلاً بك 👋", font_size='20sp', size_hint=(1, 0.2))
        
        btn = Button(
            text="قل مرحباً 👇",
            size_hint=(1, 0.2),
            on_press=self.say_hello
        )
        
        layout.add_widget(self.input_name)
        layout.add_widget(btn)
        layout.add_widget(self.label)
        
        return layout

    def say_hello(self, instance):
        name = self.input_name.text.strip()
        if name:
            self.label.text = f"Hello, {name} 👋"
        else:
            self.label.text = "اكتب اسمك أولاً 😊"


if __name__ == "__main__":
    HelloApp().run()

