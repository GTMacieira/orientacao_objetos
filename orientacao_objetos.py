from pickle import FALSE
from functions import*
#criação da classe
class Title():
    #atributos da classe
    def __init__(self,name,author,rel_chaps, aquis_chaps, active):
        self.name = name
        self.author = author
        self.rel_chaps = rel_chaps
        self.aquis_chaps=aquis_chaps
        self.__active = active

    def status(self):
        self.active = False
        print("Coleção completa")

    @property
    def get_name(self):
        return self.__name
    
    @name.setter
    def set_name(self,name):
        self.__name = name

if __name__=="__main__":
    cls_term()
    title1 = Title("Goblin Slayer","Autor não sei", 75, 3, True)    
    title1.status()
    title1.active = False
    print (title1.active)

    #utilizando geters e setters
    title1.set_name("Spy")
    print(title1.get_name())

    #utilizando propreties
    title1.name = "Spyy"
    print(title1.name)


