

class boss():  
    def __init__(self,monstro):
        self._monstro=monstro
        self._vida=30
        self._ataque=10
        self._defesa=5
        


    def classes(self):
           
            if(self._monstro==1):
                self._vida-10
                self._ataque+5
                self._defesa-2
                nome="Goblin"
                n_classe="combatente"
                return nome,n_classe,self._vida,self._ataque,self._defesa
            else:
            
                self._vida+10
                self._defesa+1
                nome="Bruxa"
                n_classe="Feiticeira"
                return nome,n_classe,self._vida,self._ataque,self._defesa
