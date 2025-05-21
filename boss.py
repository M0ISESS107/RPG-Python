

class boss():  
    def __init__(self,monstro):
        self._monstro=monstro
        self._vida=30
        self._ataque=10
        self._defesa=5
        


    def classes(self):
           
            if(self.monstro==1):
                self.vida-10
                self.ataque+5
                self.defesa-2
                nome="Goblin"
                n_classe="combatente"
                return nome,n_classe,self.vida,self.ataque,self.defesa
            else:
            
                self.vida+10
                self.defesa+1
                nome="Bruxa"
                n_classe="Feiticeira"
                return nome,n_classe,self.vida,self.ataque,self.defesa
