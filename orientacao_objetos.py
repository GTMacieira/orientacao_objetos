from dataclasses import replace
from tkinter import E
from turtle import home
from functions import*
from datetime import datetime
#criação da classe
class Title():
    title_type = "Mangá"
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    '''Criar títulos para biblioteca, no qual criará os títulos de acordo com nome do título, nome do tílo no ligua original, autor,
    resumo do título, capitulos lançados, capitulos adquiridos, qual tipo de midia que está o título, se o título esta ou não ativo'''
    def __init__(self,title_name, origin_title_name, author_title, pub_year, abstract, rel_chaps, acquisition_chaps, acquisition_date, dig_phy, active):
        self.title_name = title_name
        self.origin_title_name = origin_title_name
        self.author_title = author_title
        self.pub_year= pub_year
        self.abstract=abstract
        self.rel_chaps = rel_chaps
        self.acquisition_chaps = acquisition_chaps
        self.acquisition_date = acquisition_date
        self.dig_phy = dig_phy 
        self.active = active

        cls_term()

    @property                       
    def title_name(self):
        return self._title_name #Para não criar um loop infinito este nome não pode ser igual ao do metodo construtor

    @title_name.setter
    def title_name(self, new_name):
        self._title_name = new_name.title() #Para não criar um loop infinito este nome não pode ser igual ao do metodo construtor

    @property
    def acquisition_date(self):
        try:
            if self._acquisition_date:
                return self._acquisition_date                
        except:
            self._acquisition_date =""

    @acquisition_date.setter
    def acquisition_date(self, new_ac_date):
        if new_ac_date:
            self._acquisition_date = datetime.strptime(new_ac_date,'%d/%m/%Y')
        
        