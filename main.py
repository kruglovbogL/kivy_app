from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyCalculator(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')

        label_1 = Label(text='Введите 1:')
        input_1 = TextInput(multiline=False)
        layout.add_widget(label_1)
        layout.add_widget(input_1)

        label_2 = Label(text='Введите 2 БЕЗ умножения на 2:')
        input_2 = TextInput(multiline=False)
        layout.add_widget(label_2)
        layout.add_widget(input_2)

        label_5 = Label(text='Введите 5 БЕЗ умножения на 5:')
        input_5 = TextInput(multiline=False)
        layout.add_widget(label_5)
        layout.add_widget(input_5)

        label_10 = Label(text='Введите 10 БЕЗ умножения на 10 и бумажные тоже!:')
        input_10 = TextInput(multiline=False)
        layout.add_widget(label_10)
        layout.add_widget(input_10)

        label_100 = Label(text='Введите 100 БЕЗ умножения на 100:')
        input_100 = TextInput(multiline=False)
        layout.add_widget(label_100)
        layout.add_widget(input_100)

        label_500 = Label(text='Введите 500 БЕЗ умножения на 500:')
        input_500 = TextInput(multiline=False)
        layout.add_widget(label_500)
        layout.add_widget(input_500)

        result_label = Label(text='')

        def calculate(instance):
            num_1 = int(input_1.text) * 1
            num_2 = int(input_2.text) * 2
            num_5 = int(input_5.text) * 5
            num_10 = int(input_10.text) * 10
            num_100 = int(input_100.text) * 100
            num_500 = int(input_500.text) * 500

            total = num_1 + num_2 + num_5 + num_10 + num_100 + num_500
            result_label.text = f'Всего: {num_1} {num_2} {num_5} {num_10} {num_100} {num_500} all---- {total}'

        calculate_button = Button(text='Посчитать')
        calculate_button.bind(on_press=calculate)

        layout.add_widget(calculate_button)
        layout.add_widget(result_label)

        return layout

if __name__ == '__main__':
    MyCalculator().run()