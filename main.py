#BISMILLAHIR RAHMANIR RAHIM

from kivymd.app import MDApp
from kivy.core import text
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from Additionals import page1, page2, page3, page4, page5, page6, page7, page8, page9, page10, page11, page12


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


class Result:
    def __init__(self):
        self.parent_screen=parent_screen


class App(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'

        screen_manager=ScreenManagement(transition=FadeTransition())
        
        screen_manager.add_widget(page1.FirstPage(name='first'))
        screen_manager.add_widget(page2.SecondPage(name='second'))
        screen_manager.add_widget(page3.ThirdPage(name='third'))
        screen_manager.add_widget(page4.ForthPage(name='forth'))
        screen_manager.add_widget(page5.FifthPage(name='fifth'))
        screen_manager.add_widget(page6.SixthPage(name='sixth'))
        screen_manager.add_widget(page7.SeventhPage(name='seventh'))
        screen_manager.add_widget(page8.EighthPage(name='eighth'))
        screen_manager.add_widget(page9.NinthPage(name='ninth'))
        screen_manager.add_widget(page10.TenthPage(name='tenth'))
        screen_manager.add_widget(page11.EleventhPage(name='eleventh'))
        screen_manager.add_widget(page12.TwelvethPage(name='twelveth'))
        
        return screen_manager

App().run()