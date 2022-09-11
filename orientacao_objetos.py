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

        #cls_term()

    @property
    def title(self):
        return self._title_name

    @title.setter
    def name(self, nm):
        self.title_name = nm.replace("@","A")
