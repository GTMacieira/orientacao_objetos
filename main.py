from ntpath import join
from xml.dom.minidom import Element
from orientacao_objetos import *

titles=[["Mangá","Ajin","亜人, Ajin: Demi-Human","Miura Tsuina e Sakurai Gamon",2012,"Ajin são seres humanos que não podem morrer. Dezessete anos atrás, eles apareceram pela primeira vez em um campo de batalha na África. Desde então, mais de sua espécie são descobertos no seio da sociedade humana. Sua raridade na aparência significa que, para fins experimentais, o governo vai recompensar generosamente quem capturar um. Nos dias atuais, para que um determinado estudante do ensino médio que espera ter um feriado típico de verão, a sua vida está prestes a virar algo inesperado...",97,0,"13/09/2022","Digital","Não"],["Mangá","Akame ga Kill! Zero","アカメが斬る！零","Takahiro",2013,"A história 'dark action' terá lugar alguns anos antes dos eventos da série original da fantasia. A prequel será centrada no personagem principal Akame, uma menina comprada, com lavagem cerebral, e que foi criado pelo Império como uma assassina.",60,0,"",'Digital',"Não"],["MAngá","Ao no Exorcist","青の祓魔師〈 エクソシスト〉","Katou Kazue",2009,"Este mundo é composto de duas dimensões que se juntaram como uma só, como um espelho. O primeiro é o mundo em que os seres humanos vivem, Assiah. O outro é o mundo dos demônios, inferno. Normalmente, as viagens entre os dois é impossível. No entanto, os demônios podem passar para este mundo possuindo algo que existe nele. Satan é o deus dos demônios, mas há uma coisa que ele não tem e é um recipiente no mundo humano que seja poderoso o suficiente para segurá.Para essa finalidade, ele criou Rin, seu filho de uma mulher humana, mas seu filho concordará com seus planos?",138,0,"","Digital","Sim"]]
count=0
for title in titles:    
    title_type = title[0] #"Mangá" #input("Qual o tipo de título")
    title_name = title[1] #"Goblin Slayer" #input("Qual o nome do título?\n")
    origin_title_name = title[2] #"ゴブリンスレイヤー" #input("Qaul o neome do titulo em sua língua de origem?\n")
    author_title = title[3] #"Kagyuu Kumo" #input('Qeume é o autor do título?\n')
    pub_year = title[4] #2016 #input('Qual o ano de publicação do título?\n')
    abstract = title[5] #"Um homem deseja tornar-se um 'aventureiro', cujo lema é: 'Eu não vou salvar o mundo, eu apenas vou matar goblins.' Após ouvir rumores sobre ele, uma elfa se aproxima dele com um pedido."#input("Dê um resumo deste título:\n")
    rel_chaps = title[6] #75 #input("Quantos capítulos foram lançados deste titulo?\n")
    acquisition_chaps = title[7] #3 #input("Quantos capítulos você possi deste título?\n")
    acquisition_date = title[8] #"11-09-2022" #input("Quando aquiril o ultimo capítulo?\n")
    dig_phy = title[9] #"Digital" #input("Qual o tipo de midia deste título?\n")
    active = title[10] #"Sim" #input("este título ainda etá ativo?\n")      
    t = 't' + str(count)
    count+=1
    t = Title(title_name, origin_title_name, author_title, pub_year, abstract, rel_chaps, acquisition_chaps, acquisition_date, dig_phy, active)

    print(f"O título adicionado foi:\n \
            Tipo: {t.title_type}\n \
            Nome: {t.title_name}\n \
            Nome original: {t.origin_title_name}\n \
            Nome do autor: {t.author_title}\n \
            Ano de publicação: {t.pub_year}\n \
            Resumo: {t.abstract}\n \
            Capítulos lançados: {t.rel_chaps}\n \
            Capítulos adquiridos: {t.acquisition_chaps}\n \
            Data de aquisição: {t.acquisition_date}\n \
            Tipo de mídia: {t.dig_phy}\n \
            Está ativo: {t.active}\n\
            ")
    
    sit_title = input("As informações do título estão corretas ?\n1 - Sim\n2 - Não\n")
    
    if not sit_title.isnumeric():
        sit_title = "0"
    
    while sit_title.isnumeric(): 
        if  int(sit_title) != 1 or int(sit_title) != 2:
            print ("Valor inválido!\n")
            sit_title = input("As informações do título estão corretas ?\n1- Sim\n2- Não\n")
            if not sit_title.isnumeric():
                sit_title = "0"
        else:
            pass
    
    if int(sit_title) == 1:
        pass
    else:
        alter_date = input('\n O que deve ser alterado?\n\
            1- Tipo \n \
            2- Nome \n \
            3- Nome original \n \
            4- Nome do autor \n \
            5- Ano de publicação \n \
            6- Resumo \n \
            7- Capítulos lançados \n \
            8- Capítulos adquiridos \n \
            9- Data de aquisição\n \
            10- Tipo de mídia \n \
            11- Está ativo:')
        
        if not alter_date.isnumeric():
            alter_date = "0"
            
        while alter_date.isnumeric(): 
            if  int(alter_date) <= 1 or int(alter_date) >= 11:
                print ("Valor inválido!\n")
                alter_date = input('\n O que deve ser alterado?\n\
                    1- Tipo \n \
                    2- Nome \n \
                    3- Nome original \n \
                    4- Nome do autor \n \
                    5- Ano de publicação \n \
                    6- Resumo \n \
                    7- Capítulos lançados \n \
                    8- Capítulos adquiridos \n \
                    9- Data de aquisição\n \
                    10- Tipo de mídia \n \
                    11- Está ativo:')
                
            if not alter_date.isnumeric():
                alter_date = "0"
                
        elements = (t.title_type, t.title_name, t.origin_title_name, t.author_title, t.pub_year, t.abstract, t.rel_chaps, t.acquisition_chaps, t.acquisition_date, t.dig_phy)
        
        element = input("Qual a nova informação")
        
        alter_date = 't.' + elements(int(alter_date)) 
        
        alter_date = element