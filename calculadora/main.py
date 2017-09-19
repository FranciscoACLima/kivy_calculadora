# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


titulo = 'Kivy Calculadora'


class Tela(BoxLayout):

    def carregar(self, num):
        self.ids['res'].text += num
        self.ids['tit'].text = titulo

    def limpar(self):
        tx = self.ids['res'].text
        tx = tx[:-1]
        self.ids['res'].text = tx
        self.ids['tit'].text = titulo

    def calcular(self):
        val = self.ids['res'].text
        if val:
            try:
                if '/' in val:
                    val = '1.0*' + val
                calc = eval(val)
                self.ids['res'].text = str(calc)
            except ZeroDivisionError:
                self.msg_erro('Erro ao dividir por zero')
            except SyntaxError:
                self.msg_erro('Expressão Inválida')

    def msg_erro(self, msg):
        msg = '[color=ff0000]' + msg + '[/color]'
        label = self.ids['tit']
        label.text = msg
        label.markup = True


class Calculadora(App):
    pass


Calculadora().run()
