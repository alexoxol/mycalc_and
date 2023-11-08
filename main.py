from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from funcs import *

# Размер приложения
# Window.size = (500, 700)

Builder.load_file('kv_calc.kv')
# Builder.load_string("""
#     Здесь можно kv-файл прям писать
# """)

class MyLayout(Widget):
    last_pressed_equal = False
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)

    def press_C(self):
        self.ids.calc_input.text = '0'

    def press_back(self):
        self.check_if_was_equal()
        prior = self.ids.calc_input.text
        # Назад
        new = f'{prior[:-1]}'
        self.ids.calc_input.text = f'{prior[:-1]}' if len(new) > 0 else '0'

    # Проверка последнего нажатия '='
    def check_if_was_equal(self):
        if self.last_pressed_equal:
            self.ids.calc_input.text = '0'
        self.last_pressed_equal = False

    def button_press(self, str_val):
        self.check_if_was_equal()
        prior = self.ids.calc_input.text
        if prior == '0':
            # Выводим число
            self.ids.calc_input.text = str_val
        else:
            # Присоединяем число справа
            self.ids.calc_input.text = f'{prior}{str_val}'

    # Последний символ - цифра?
    def isLastDigit(self):
        prior = self.ids.calc_input.text
        return prior[-1].isdigit()

    def press_point(self):
        self.check_if_was_equal()
        prior = self.ids.calc_input.text
        if self.isLastDigit():
            # +.
            self.ids.calc_input.text = f'{prior}.'
        else:
            # +0.
            self.ids.calc_input.text = f'{prior}0.'

    def press_plusminus(self):
        self.check_if_was_equal()
        prior = self.ids.calc_input.text
        if prior[0] == '-':
            self.ids.calc_input.text = f'{prior[1:]}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def math_oper(self, prior):
        # Если есть пример, то решаем
        ops = {
            '+': fun_add,
            '–': fun_sub,
            '*': fun_mult,
            '/': fun_div
        }
        for op in ops.keys():
            list_nums = prior.split(op)
            if len(list_nums) > 1:
                res = math_fun(list_nums, ops[op])
                return res
        return prior

    def add_sign(self, sign):
        self.last_pressed_equal = False
        prior = self.ids.calc_input.text
        if self.isLastDigit():
            new = self.math_oper(prior)
            # Присоединяем знак
            self.ids.calc_input.text = f'{new}{sign}'
        else:
            # Меняем последний знак на +
            self.ids.calc_input.text = f'{prior[:-1]}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        if self.isLastDigit():
            new = self.math_oper(prior)
            self.ids.calc_input.text = f'{new}'
            self.last_pressed_equal = True

class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()
