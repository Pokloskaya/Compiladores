#Clase botom up.


class Bottom_up:

    def __init__(self,First,Follow,Grammar,NoTerminals,cadenas):
        self.First=First
        self.Follow=Follow
        self.Grammar=Grammar
        self.NoTerminals=NoTerminals
        self.cadenas=cadenas
        self.Terminals=set()
        self.extenderGramatica()



    #Extender la gramatica
    def extenderGramatica(self):
        extend =  self.NoTerminals[0]+"'"
        self.Grammar[extend]=[self.NoTerminals[0]]
        print(self.Grammar)
        